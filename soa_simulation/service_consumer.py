# service_consumer.py
# A client that consumes services using dynamic binding
from utils import discover_service
from config import SERVICE_REGISTRY_URL
import requests

def make_request(service_name):
    service_url = discover_service(service_name, SERVICE_REGISTRY_URL)
    if service_url:
        response = requests.get(service_url)
        return response.json()
    return {'error': 'Service not found'}

if __name__ == '__main__':
    print(make_request('payment'))
