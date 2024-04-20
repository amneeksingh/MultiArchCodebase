# load_balancer.py
# Simulates a load balancer to distribute requests across multiple servers

from flask import Flask, request, jsonify
from config import WEB_SERVERS
import itertools
import requests

app = Flask(__name__)
cycle = itertools.cycle(WEB_SERVERS)  # Round-robin scheduling

@app.route('/balance', methods=['POST'])
def balance_load():
    server = next(cycle)
    response = requests.post(server, json=request.get_json())
    return jsonify(server=server, response=response.json())

if __name__ == '__main__':
    app.run(port=4000, debug=True)
