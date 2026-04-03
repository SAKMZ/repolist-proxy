from flask import Flask, Response
import requests
import json

app = Flask(__name__)

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

BASE_IMG_URL = "https://www.21strepos.com"

@app.route("/")
@app.route("/repolist")
def repolist():
    try:
        r = requests.get(
            "https://www.21stmortgage.com/repolist3.json",
            headers=HEADERS,
            timeout=25
        )
        r.raise_for_status()
        data = r.json()

        # Fix PIC field — build full URL
        for listing in data:
            pic = listing.get("PIC", "")
            if pic and not pic.startswith("http"):
                listing["PIC"] = BASE_IMG_URL + "/" + pic.lstrip("/")

        return Response(
            json.dumps(data),
            mimetype="application/json"
        )
    except Exception as e:
        return Response('{"error":"' + str(e) + '"}', status=500, mimetype="application/json")
