from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

DATA_FILE = "captured_data.txt"

def save_data(data):
    with open(DATA_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat()} - {data}\\n")

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    save_data(data)
    return jsonify({"status": "success"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"data": []})
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()
    return jsonify({"data": lines})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
