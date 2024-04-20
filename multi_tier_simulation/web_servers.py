# web_servers.py
# Simulates web servers

from flask import Flask, request, jsonify
import sys

app = Flask(__name__)
port = sys.argv[1] if len(sys.argv) > 1 else 5001

@app.route('/', methods=['POST'])
def handle_request():
    data = request.get_json()
    # Simple processing simulation
    return jsonify(message="Request processed at Web Server on port " + str(port), data=data)

if __name__ == '__main__':
    app.run(port=int(port), debug=True)
