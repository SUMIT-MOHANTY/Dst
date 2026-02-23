import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-me'
    DEBUG = False
    TESTING = False
