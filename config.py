import os

class Config:
    # [RISK 2 MITIGATION] Disable debug mode in production to prevent info leakage
    DEBUG = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-replace-in-prod')
    # [RISK 3 MITIGATION] HTTPOnly cookies prevent XSS from stealing session tokens
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
