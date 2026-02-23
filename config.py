import os
from dotenv import load_dotenv

class Config:
    load_dotenv()
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-me'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True
    WTF_CSRF_ENABLED = True
