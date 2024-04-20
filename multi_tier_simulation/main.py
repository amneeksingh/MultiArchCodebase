# main.py
# Main script to run the multi-tier simulation

import subprocess
import sys
import time
from config import WEB_SERVERS, APPLICATION_SERVERS

def start_flask_app(script, ports):
    for port in ports:
        subprocess.Popen([sys.executable, script, str(port)])

if __name__ == '__main__':
    # Start web servers
    start_flask_app('web_servers.py', [5001, 5002, 5003])
    # Start application servers
    start_flask_app('application_servers.py', [6001, 6002, 6003])
    # Start database server
    subprocess.Popen([sys.executable, 'database.py'])

    # Keep the main thread alive to prevent the script from exiting
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Simulation ended.")
