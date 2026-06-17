from flask import Flask, jsonify, Response
import requests
import json

app = Flask(__name__)

DEVELOPER_NAME = "⏤͟͟͞͞Rᴀᴊᴘᴜᴛ Sᴜʀᴀᴊ </> 🚩"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

def fetch_data(url):
    try:
        r = requests.get(
            url,
            headers=HEADERS,
            timeout=30,
            allow_redirects=True
        )

        text = r.text.strip()

        try:
            data = json.loads(text)

            if isinstance(data, dict):
                data["developer"] = DEVELOPER_NAME

            return jsonify(data)

        except:
            return jsonify({
                "status": True,
                "developer": DEVELOPER_NAME,
                "raw_response": text
            })

    except Exception as e:
        return jsonify({
            "status": False,
            "developer": DEVELOPER_NAME,
            "error": str(e)
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
