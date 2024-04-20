# config.py
# Configuration for multi-tier simulation

# URLs of web servers (simulated)
WEB_SERVERS = [
    'http://localhost:5001',
    'http://localhost:5002',
    'http://localhost:5003'
]

# URLs for application servers
APPLICATION_SERVERS = [
    'http://localhost:6001',
    'http://localhost:6002',
    'http://localhost:6003'
]

# Database connection string
DATABASE_URL = "sqlite:///simulation.db"
