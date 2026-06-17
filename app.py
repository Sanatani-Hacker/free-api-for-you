from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

DEVELOPER_NAME = "⏤͟͟͞͞Rᴀᴊᴘᴜᴛ Sᴜʀᴀᴊ </> 🚩"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
}

def ok(data):
    data["developer"] = DEVELOPER_NAME
    data["status"] = True
    return jsonify(data)

def err(msg):
    return jsonify({"status": False, "developer": DEVELOPER_NAME, "error": msg}), 500


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
    try:
        # India Post official API
        r = requests.get(
            f"https://api.postalpincode.in/pincode/{pincode}",
            headers=HEADERS, timeout=10
        )
        data = r.json()
        if data and data[0]["Status"] == "Success":
            return ok({"data": data[0]["PostOffice"]})
        return err("Pincode not found")
    except Exception as e:
        return err(str(e))


@app.route("/ip=<ip>")
def ip_lookup(ip):
    try:
        # ip-api.com — free, no key needed
        r = requests.get(
            f"http://ip-api.com/json/{ip}",
            headers=HEADERS, timeout=10
        )
        data = r.json()
        if data.get("status") == "success":
            return ok(data)
        return err("IP not found")
    except Exception as e:
        return err(str(e))


@app.route("/ifsc=<ifsc>")
def ifsc(ifsc):
    try:
        # Razorpay IFSC API — free, no key needed
        r = requests.get(
            f"https://ifsc.razorpay.com/{ifsc}",
            headers=HEADERS, timeout=10
        )
        if r.status_code == 200:
            return ok(r.json())
        return err("IFSC not found")
    except Exception as e:
        return err(str(e))


app = app
