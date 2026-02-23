from functools import wraps
from flask import jsonify
import re

def validate_input(data, patterns):
    for field, pattern in patterns.items():
        if field in data and not re.match(pattern, str(data[field])):
            return False, f'Invalid {field}'
    return True, None

def rate_limit_exempt(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    decorated_function._rate_limit_exempt = True
    return decorated_function

class SecurityHeaders:
    @staticmethod
    def get_headers():
        return {
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block',
            'Referrer-Policy': 'strict-origin-when-cross-origin',
            'Permissions-Policy': 'geolocation=(), microphone=(), camera=()'
        }
