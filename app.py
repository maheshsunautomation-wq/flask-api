from flask import Flask, request, jsonify

app = Flask(__name__)

temp = 0

@app.route('/')
def home():
    return "API working on Render"

@app.route('/set', methods=['POST'])
def set_temp():
    global temp
    data = request.get_json()

    temp = data.get('temperature', 0)

    return jsonify({
        "message": "Saved",
        "temperature": temp
    })

@app.route('/get', methods=['GET'])
def get_temp():
    return jsonify({
        "temperature": temp
    })
