from flask import Blueprint, request, jsonify
from .ai_service import AIService

ai_bp = Blueprint('ai', __name__)
ai_service = AIService()

@ai_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'ai-backend'}), 200

@ai_bp.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    
    if not ai_service.validate_request(data):
        return jsonify({'error': 'Invalid request. Prompt required.'}), 400
    
    prompt = data.get('prompt', '')
    messages = data.get('messages', None)
    
    result = ai_service.generate_response(prompt, messages)
    
    if 'error' in result:
        return jsonify(result), 500
    
    return jsonify(result), 200

@ai_bp.route('/validate', methods=['POST'])
def validate_config():
    from .config import Config
    is_configured = bool(Config.OPENAI_API_KEY and Config.OPENAI_API_KEY != 'your_openai_api_key_here')
    return jsonify({'api_configured': is_configured}), 200
