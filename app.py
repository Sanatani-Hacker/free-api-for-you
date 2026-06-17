from flask import Flask, jsonify
import requests

app = Flask(__name__)

DEVELOPER_NAME = "⏤͟͟͞͞Rᴀᴊᴘᴜᴛ Sᴜʀᴀᴊ </> 🚩"

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
    url = f"https://abhaykumar.xo.je/api/proxy420.php?tool=pincode_info&query={pincode}"
    return modify_response(url)

@app.route("/ip=<ip>")
def ip_info(ip):
    url = f"https://abhaykumar.xo.je/api/proxy420.php?tool=ip_info&query={ip}"
    return modify_response(url)

@app.route("/ifsc=<ifsc>")
def ifsc_info(ifsc):
    url = f"https://abhaykumar.xo.je/api/proxy420.php?tool=ifsc_info&query={ifsc}"
    return modify_response(url)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
