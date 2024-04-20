# service_provider.py
# Simulates a service provider for SOA

from flask import Flask, jsonify
import random
import sys

app = Flask(__name__)
service_name = sys.argv[1] if len(sys.argv) > 1 else 'default_service'
service_port = sys.argv[2] if len(sys.argv) > 2 else 5001

@app.route('/')
def service():
    return jsonify(service=service_name, status='running', result=random.randint(1, 100))

if __name__ == '__main__':
    app.run(port=int(service_port), debug=True)
