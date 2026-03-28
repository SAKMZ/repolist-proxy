import requests
from http.server import BaseHTTPRequestHandler
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-GB,en;q=0.9",
    "Referer": "https://www.21stmortgage.com/web/21stsite.nsf/locating?OpenForm",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            r = requests.get(
                "https://www.21stmortgage.com/repolist3.json",
                headers=HEADERS,
                timeout=25
            )
            r.raise_for_status()
            data = r.json()

            body = json.dumps(data).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        except Exception as e:
            error = json.dumps({"error": str(e)}).encode()
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(error)))
            self.end_headers()
            self.wfile.write(error)

    def log_message(self, format, *args):
        pass  # suppress default logging
