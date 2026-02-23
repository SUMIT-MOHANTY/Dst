#!/usr/bin/env python3
import os
import requests
import time
import logging
from datetime import datetime
import psutil
import json

def setup_monitor_logger():
    logger = logging.getLogger('monitor')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('logs/monitor.log')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(handler)
    return logger

def check_health_check(url):
    try:
        response = requests.get(f'{url}/health', timeout=10)
        return response.status_code == 200
    except Exception as e:
        return False

def check_ssl_cert(url):
    try:
        response = requests.get(url, timeout=10, verify=True)
        cert = response.raw.peer_certificate
        return True, cert
    except Exception as e:
        return False, str(e)

def monitor_system_resources():
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent
    }

def main():
    logger = setup_monitor_logger()
    url = os.environ.get('APP_URL', 'https://localhost:5000')
    
    while True:
        timestamp = datetime.now().isoformat()
        
        # Health check
        healthy = check_health_check(url)
        status = 'HEALTHY' if healthy else 'UNHEALTHY'
        logger.info(f'{timestamp} | Health: {status}')
        
        # SSL check (hourly)
        if int(time.time()) % 3600 < 60:
            ssl_valid, cert_info = check_ssl_cert(url)
            logger.info(f'{timestamp} | SSL: {"VALID" if ssl_valid else "INVALID"}')
        
        # Resource monitoring
        resources = monitor_system_resources()
        logger.info(f'{timestamp} | CPU: {resources["cpu_percent"]}% | MEM: {resources["memory_percent"]}% | DISK: {resources["disk_percent"]}%')
        
        # Write metrics file for dashboards
        with open('logs/current_metrics.json', 'w') as f:
            json.dump({'timestamp': timestamp, 'health': healthy, 'resources': resources}, f)
        
        time.sleep(60)

if __name__ == '__main__':
    main()
