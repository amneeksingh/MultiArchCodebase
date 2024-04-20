# application_servers.py
# Simulates application logic servers

from flask import Flask, request, jsonify
import sys

app = Flask(__name__)
port = sys.argv[1] if len(sys.argv) > 1 else 6001

@app.route('/', methods=['POST'])
def process_logic():
    data = request.get_json()
    # Further processing simulation
    return jsonify(message="Logic processed at App Server on port " + str(port), data=data)

if __name__ == '__main__':
    app.run(port=int(port), debug=True)
