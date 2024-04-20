# utils.py
# Utility functions for load distribution

import requests
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

meta = MetaData()

# Define a simple table to simulate a database
users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String)
)

def create_db(engine_url):
    engine = create_engine(engine_url)
    meta.create_all(engine)
    return engine

def add_user(engine, name, email):
    conn = engine.connect()
    conn.execute(users.insert().values(name=name, email=email))
    conn.close()

def get_users(engine):
    conn = engine.connect()
    result = conn.execute(users.select())
    users_data = [dict(row) for row in result]
    result.close()
    conn.close()
    return users_data

def send_request(url, data):
    return requests.post(url, json=data).json()
