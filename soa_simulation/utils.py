# utils.py
# Utility functions for SOA simulation

import requests

def register_service(service_url, service_name, registry_url):
    """ Register a service with the service registry. """
    data = {'name': service_name, 'url': service_url}
    response = requests.post(f"{registry_url}/register", json=data)
    return response.status_code == 200

def deregister_service(service_name, registry_url):
    """ Deregister a service from the service registry. """
    response = requests.delete(f"{registry_url}/deregister/{service_name}")
    return response.status_code == 200

def discover_service(service_name, registry_url):
    """ Discover a service URL using the service registry. """
    response = requests.get(f"{registry_url}/services/{service_name}")
    if response.status_code == 200:
        return response.json()['url']
    return None
