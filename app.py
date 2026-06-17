from flask import Flask, jsonify
import requests

app = Flask(__name__)

DEVELOPER_NAME = "Rajput Suraj Raj 🚩🇮🇳"

def modify_response(url):
    try:
        r = requests.get(url, timeout=15)
        data = r.json()

        if isinstance(data, dict):
            data["developer"] = DEVELOPER_NAME

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "status": False,
            "error": str(e),
            "developer": DEVELOPER_NAME
        })

@app.route("/pincode=<pincode>")
def pincode_info(pincode):
    return modify_response(
        f"https://abhaykumar.xo.je/api/proxy420.php?tool=pincode_info&query={pincode}"
    )

@app.route("/ip=<ip>")
def ip_info(ip):
    return modify_response(
        f"https://abhaykumar.xo.je/api/proxy420.php?tool=ip_info&query={ip}"
    )

@app.route("/ifsc=<ifsc>")
def ifsc_info(ifsc):
    return modify_response(
        f"https://abhaykumar.xo.je/api/proxy420.php?tool=ifsc_info&query={ifsc}"
    )

@app.route("/")
def home():
    return jsonify({
        "developer": DEVELOPER_NAME,
        "status": True
    })

app = app
