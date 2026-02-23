from flask import Blueprint, render_template, jsonify, request
from flask_wtf.csrf import CSRFError

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'status': 'success', 'received': data})
    return jsonify({'message': 'GET request received', 'csrf_token': request.csrf_token() if hasattr(request, 'csrf_token') else 'N/A'})

@bp.errorhandler(CSRFError)
def handle_csrf_error(e):
    return jsonify({'error': 'CSRF token missing or invalid', 'status': 400}), 400
