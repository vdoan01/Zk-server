from flask import Flask, request
import requests
import os

app = Flask(__name__)
SHEET_URL = os.environ.get("SHEET_URL")

@app.route('/iclock/cdata', methods=['GET','POST'])
def receive():
    data = request.data.decode('utf-8', errors='ignore')
    for line in data.strip().split('\n'):
        parts = line.split('\t')
        if len(parts) >= 2:
            requests.post(SHEET_URL, json={
                "user_id": parts[0],
                "punch_time": parts[1],
                "punch_type": parts[4] if len(parts) > 4 else "0"
            })
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
