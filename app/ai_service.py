import openai
from .config import Config
from typing import Dict, List

class AIService:
    def __init__(self):
        if Config.OPENAI_API_KEY:
            openai.api_key = Config.OPENAI_API_KEY
    
    def validate_request(self, request_data: Dict) -> bool:
        if not request_data:
            return False
        required_fields = ['prompt']
        return all(field in request_data for field in required_fields)
    
    def generate_response(self, prompt: str, messages: List = None) -> Dict:
        try:
            if not openai.api_key:
                return {'error': 'API key not configured'}
            
            msg_list = messages if messages else [{'role': 'user', 'content': prompt}]
            response = openai.chat.completions.create(
                model=Config.MODEL,
                messages=msg_list,
                max_tokens=Config.MAX_TOKENS
            )
            return {'response': response.choices[0].message.content}
        except Exception as e:
            return {'error': str(e)}
