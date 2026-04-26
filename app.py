from flask import Flask, request, jsonify

app = Flask(__name__)

temp = 0

@app.route('/')
def home():
    return "API working"

@app.route('/set', methods=['POST'])
def set_temp():
    global temp
    data = request.json
    temp = data['temperature']
    return "Saved"

@app.route('/get')
def get_temp():
    return jsonify({"temperature": temp})

app.run()