import os,requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)

def webhook(request_data):
    requests.post(os.getenv("WEBHOOK_URL"),
                    data=request_data, 
                    headers={'Content-Type': 'application/json'})

@app.route("/")
def home():
    return "<h1> Sefa AYDINELLİ </h1>"

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
    app.run(host='0.0.0.0', port=8080)