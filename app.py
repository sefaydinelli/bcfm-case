from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
webhook_url = 'https://webhook.site/29504f6b-4f91-483d-bc21-587c2f203e61'

def webhook(request_data):
    requests.post(webhook_url,
                    data=request_data, 
                    headers={'Content-Type': 'application/json'})

@app.route("/")
def home():
    return jsonify(firstname = "Sefa", lastname = "Aydinelli")

@app.route("/whoami")
def who_am_i():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    return jsonify(firstname = firstname, lastname = lastname)

@app.route("/alert", methods=['POST'])
def alert():
    if request.method == 'POST':
        request_data = request.get_json(force=True)
        print ("test")
        webhook(request_data)
        return 'OK', 200
    else:
        return 'Error'

if __name__ == "__main__":
    app.run(host = '0.0.0.0')