Check_in API
=============

Simple dependency-free HTTP API for managing check-ins (uses Python standard library only).

Files
- `api.py` - Small HTTP server exposing /checkins (GET, POST, DELETE).
- `api_test.py` - Starts the server and runs simple tests against it.

Run the tests (PowerShell):

```powershell
python .\Working\api_test.py
```

Or run the server manually:

```powershell
python .\Working\api.py
```
