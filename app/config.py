import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    APP_API_KEY = os.getenv("APP_API_KEY")
    MAX_PROMPT_LENGTH = int(os.getenv("MAX_PROMPT_LENGTH", 2000))
    AI_MODEL = os.getenv("AI_MODEL", "gpt-3.5-turbo")

settings = Settings()
