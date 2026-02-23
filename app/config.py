import os

class Config:
    ENV = os.environ.get("ENV", "development")
    DEBUG = False
