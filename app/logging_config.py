import logging
import sys
from logging.handlers import RotatingFileHandler
import os

def setup_logger(app_name='security_app', log_level=logging.INFO):
    logger = logging.getLogger(app_name)
    logger.setLevel(log_level)
    
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, f'{app_name}.log'),
            maxBytes=10485760,
            backupCount=5
        )
        file_handler.setLevel(log_level)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    
    return logger

class SecurityAuditLogger:
    def __init__(self, logger):
        self.logger = logger
    
    def log_security_event(self, event_type, details, severity='INFO'):
        self.logger.info(f' SECURITY_EVENT: {event_type} | Details: {details} | Severity: {severity}')
    
    def log_access_attempt(self, ip, endpoint, method, status):
        self.logger.info(f' ACCESS: IP={ip} | Method={method} | Endpoint={endpoint} | Status={status}')
