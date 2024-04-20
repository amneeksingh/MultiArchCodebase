# database.py
# Simulates a database server

from flask import Flask, jsonify, request
from utils import create_db, add_user, get_users
from config import DATABASE_URL

app = Flask(__name__)
engine = create_db(DATABASE_URL)

@app.route('/add_user', methods=['POST'])
def add():
    data = request.get_json()
    add_user(engine, data['name'], data['email'])
    return jsonify(success=True)

@app.route('/get_users', methods=['GET'])
def get():
    users = get_users(engine)
    return jsonify(users=users)

if __name__ == '__main__':
    app.run(port=7000, debug=True)
