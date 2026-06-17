from flask import Flask, jsonify
import requests

app = Flask(__name__)

DEVELOPER_NAME = "⏤͟͟͞͞Rᴀᴊᴘᴜᴛ Sᴜʀᴀᴊ </> 🚩"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0 Safari/537.36",
    "Accept": "application/json,text/plain,*/*",
    "Connection": "keep-alive"
}

def fetch_data(url):
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30,
            allow_redirects=True
        )

        response.raise_for_status()

        data = response.json()

        if isinstance(data, dict):
            data["developer"] = DEVELOPER_NAME

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "developer": DEVELOPER_NAME,
            "error": str(e),
            "status": False
        })

@app.route("/")
def home():
    return jsonify({
        "status": True,
        "developer": DEVELOPER_NAME,
        "endpoints": {
            "pincode": "/pincode=800026",
            "ip": "/ip=104.23.45.198",
            "ifsc": "/ifsc=SBIN0016645"
        }
    })

@app.route("/pincode=<pincode>")
def pincode(pincode):
    url = f"https://abhaykumar.xo.je/api/proxy420.php?tool=pincode_info&query={pincode}"
    return fetch_data(url)

@app.route("/ip=<ip>")
def ip(ip):
    url = f"https://abhaykumar.xo.je/api/proxy420.php?tool=ip_info&query={ip}"
    return fetch_data(url)

@app.route("/ifsc=<ifsc>")
def ifsc(ifsc):
    url = f"https://abhaykumar.xo.je/api/proxy420.php?tool=ifsc_info&query={ifsc}"
    return fetch_data(url)

app = app
