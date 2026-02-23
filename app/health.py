from flask import Blueprint, jsonify
import os

health_bp = Blueprint('health', __name__)

@health_bp.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'security-flask-app',
        'version': '1.0.0',
        'environment': os.environ.get('FLASK_ENV', 'unknown')
    }), 200

@health_bp.route('/ready')
def readiness_check():
    return jsonify({'status': 'ready'}), 200
