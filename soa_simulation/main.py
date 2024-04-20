# main.py
# Main driver script for SOA simulation

from utils import register_service, deregister_service
from config import SERVICE_PROVIDER_URLS, SERVICE_REGISTRY_URL
import time

def setup_services():
    for name, url in SERVICE_PROVIDER_URLS.items():
        if register_service(url, name, SERVICE_REGISTRY_URL):
            print(f'Successfully registered {name} service.')
        else:
            print(f'Failed to register {name} service.')

def shutdown_services():
    for name in SERVICE_PROVIDER_URLS.keys():
        if deregister_service(name, SERVICE_REGISTRY_URL):
            print(f'Successfully deregistered {name} service.')
        else:
            print(f'Failed to deregister {name} service.')

if __name__ == '__main__':
    try:
        setup_services()
        # Assuming the services are needed for some duration
        time.sleep(60)  # Keep services registered for 60 seconds
    finally:
        shutdown_services()
