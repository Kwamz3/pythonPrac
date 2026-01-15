import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import threading

BASE_FILE = os.path.join(os.path.dirname(__file__), 'check_in.json')
_FILE_LOCK = threading.Lock()


def load_list():
    # Load the JSON file safely while holding a lock to avoid read/write races
    if not os.path.exists(BASE_FILE):
        return []

    with _FILE_LOCK:
        with open(BASE_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # If the file is corrupt, return empty list (safe fallback)
                return []


def save_list(checks):
    # Write atomically to avoid partial writes if the process is interrupted.
    dirpath = os.path.dirname(BASE_FILE) or '.'
    tmp_path = BASE_FILE + '.tmp'
    with _FILE_LOCK:
        with open(tmp_path, 'w', encoding='utf-8') as file:
            json.dump(checks, file, indent=4)
            file.flush()
            os.fsync(file.fileno())
        # Replace the target file with the temp file atomically
        os.replace(tmp_path, BASE_FILE)


class CheckinHandler(BaseHTTPRequestHandler):
    server_version = "CheckinHTTP/0.1"

    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def _read_json(self):
        length = int(self.headers.get('Content-Length', 0))
        if length == 0:
            return None
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode('utf-8'))
        except Exception:
            return None

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path != '/checkins':
            self._set_headers(404)
            self.wfile.write(b'{"error":"not found"}')
            return

        query = parse_qs(parsed.query)
        sort = query.get('sort', [None])[0]

        checks = load_list()

        if sort == 'name':
            checks = sorted(checks, key=lambda c: c.get('name', '').lower())
        elif sort == 'latest':
            try:
                checks = sorted(
                    checks,
                    key=lambda chk: datetime.strptime(chk['day'] + ' ' + chk['time'], '%d-%m-%y %H:%M:%S'),
                    reverse=True,
                )
            except Exception:
                pass

        self._set_headers(200)
        self.wfile.write(json.dumps(checks).encode('utf-8'))

    def do_POST(self):
        if self.path != '/checkins':
            self._set_headers(404)
            self.wfile.write(b'{"error":"not found"}')
            return

        body = self._read_json()
        if not body or 'name' not in body or not isinstance(body['name'], str) or body['name'].strip() == '':
            self._set_headers(400)
            self.wfile.write(b'{"error":"name is required"}')
            return

        name = body['name'].strip()
        day_input = datetime.now().strftime('%d-%m-%y')
        time_input = datetime.now().strftime('%H:%M:%S')

        checkin = {'name': name, 'day': day_input, 'time': time_input}
        checks = load_list()
        checks.append(checkin)
        save_list(checks)

        self._set_headers(201)
        self.wfile.write(json.dumps(checkin).encode('utf-8'))

    def do_DELETE(self):
        if self.path != '/checkins':
            self._set_headers(404)
            self.wfile.write(b'{"error":"not found"}')
            return

        save_list([])
        self._set_headers(200)
        self.wfile.write(b'{"status":"cleared"}')

    # Disable logging to stderr by default to keep output tidy
    def log_message(self, format, *args):
        return


def run_server(host='127.0.0.1', port=8000):
    server = ThreadingHTTPServer((host, port), CheckinHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


if __name__ == '__main__':
    print('Starting check-in API on http://127.0.0.1:8000')
    srv = ThreadingHTTPServer(('0.0.0.0', 8000), CheckinHandler)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down')
        srv.shutdown()
