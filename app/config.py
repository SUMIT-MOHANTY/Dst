import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-key-12345')
    MAX_TOKENS = 1000
    MODEL = 'gpt-3.5-turbo'
