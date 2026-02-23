import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    DEMO_MODE = os.getenv('DEMO_MODE', 'true').lower() == 'true'
    API_KEY = os.getenv('OPENAI_API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')
