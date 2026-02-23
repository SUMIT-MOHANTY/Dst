from flask import Flask, request, jsonify
from app.security.input_sanitizer import sanitize_html_input
from app.security.prompt_injection_guard import validate_prompt
from app.security.headers import apply_security_headers

app = Flask(__name__)

@app.before_request
def security_middleware():
    if request.path.startswith('/static'): return
    # Mockup: Check specific endpoints for validation

@app.after_request
def set_headers(response):
    return apply_security_headers(response)

@app.route('/ai/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    if not validate_prompt(prompt):
        return jsonify({"error": "Invalid request content"}), 400
    
    safe_prompt = sanitize_html_input(prompt)
    return jsonify({"result": f"Processed: {safe_prompt}"})

if __name__ == '__main__':
    app.run(ssl_context='adhoc') # Dev only, use NGINX in prod
