import time
import http.client
import json
from checkin_api import run_server


def request(method, path, body=None, headers=None):
	conn = http.client.HTTPConnection('127.0.0.1', 8000, timeout=5)
	if body is not None:
		body = json.dumps(body)
		if headers is None:
			headers = {'Content-Type': 'application/json'}
	conn.request(method, path, body=body, headers=headers or {})
	resp = conn.getresponse()
	data = resp.read()
	try:
		return resp.status, json.loads(data.decode('utf-8'))
	except Exception:
		return resp.status, data.decode('utf-8')


def run_basic_tests():
	srv = run_server()
	# allow server to start
	time.sleep(0.2)

	print('POST /checkins with name=Alice')
	status, body = request('POST', '/checkins', {'name': 'Alice'})
	print(status, body)

	print('GET /checkins')
	status, body = request('GET', '/checkins')
	print(status, body)

	print('POST /checkins with invalid payload')
	status, body = request('POST', '/checkins', {'wrong': 'x'})
	print(status, body)

	print('DELETE /checkins')
	status, body = request('DELETE', '/checkins')
	print(status, body)

	print('GET /checkins after clear')
	status, body = request('GET', '/checkins')
	print(status, body)

	# shutdown server
	srv.shutdown()


if __name__ == '__main__':
	run_basic_tests()

