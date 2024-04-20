# config.py
# Configuration for SOA simulation

# Service Registry URL
SERVICE_REGISTRY_URL = 'http://localhost:5000'

# Service Provider URLs
SERVICE_PROVIDER_URLS = {
    'payment': 'http://localhost:5001',
    'order': 'http://localhost:5002',
    'inventory': 'http://localhost:5003'
}
