# service_registry.py
# Simulates a service registry for SOA

from flask import Flask, jsonify, request

app = Flask(__name__)
services = {}

@app.route('/register', methods=['POST'])
def register():
    service_data = request.json
    services[service_data['name']] = service_data['url']
    return jsonify(success=True), 200

@app.route('/deregister/<service_name>', methods=['DELETE'])
def deregister(service_name):
    if service_name in services:
        del services[service_name]
        return jsonify(success=True), 200
    return jsonify(success=False), 404

@app.route('/services/<service_name>', methods=['GET'])
def get_service(service_name):
    if service_name in services:
        return jsonify(url=services[service_name]), 200
    return jsonify(error='Service not found'), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
