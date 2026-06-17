from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

DEVELOPER_NAME = "⏤͟͟͞͞Rᴀᴊᴘᴜᴛ Sᴜʀᴀᴊ </> 🚩"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://abhaykumar.xo.je/",
}

def fetch_data(url):
    try:
        session = requests.Session()

        r = session.get(url, headers=HEADERS, timeout=30, allow_redirects=True)

        content_type = r.headers.get("Content-Type", "")

        # Agar HTML aa raha hai (anti-bot page) toh clear error do
        if "text/html" in content_type or r.text.strip().startswith("<"):
            return jsonify({
                "status": False,
                "developer": DEVELOPER_NAME,
                "error": "Upstream server ne HTML diya — bot protection block kar raha hai. Baad mein try karo."
            }), 503

        text = r.text.strip()

        try:
            data = json.loads(text)
            if isinstance(data, dict):
                data["developer"] = DEVELOPER_NAME
            return jsonify(data)

        except json.JSONDecodeError:
            return jsonify({
                "status": False,
                "developer": DEVELOPER_NAME,
                "error": "Invalid JSON response from upstream.",
                "raw_preview": text[:200]  # Sirf pehle 200 chars debug ke liye
            }), 502

    except requests.Timeout:
        return jsonify({
            "status": False,
            "developer": DEVELOPER_NAME,
            "error": "Request timeout — upstream server ne jawab nahi diya."
        }), 504

    except Exception as e:
        return jsonify({
            "status": False,
            "developer": DEVELOPER_NAME,
            "error": str(e)
        }), 500


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
def ip_lookup(ip):
    url = f"https://abhaykumar.xo.je/api/proxy420.php?tool=ip_info&query={ip}"
    return fetch_data(url)

@app.route("/ifsc=<ifsc>")
def ifsc(ifsc):
    url = f"https://abhaykumar.xo.je/api/proxy420.php?tool=ifsc_info&query={ifsc}"
    return fetch_data(url)
