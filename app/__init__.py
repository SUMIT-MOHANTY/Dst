from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
import logging
from logging.handlers import RotatingFileHandler

def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['WTF_CSRF_TIME_LIMIT'] = None
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    
    Talisman(app, force_https=True, strict_transport_security=True)
    CORS(app, resources={r"/*": {"origins": os.environ.get('ALLOWED_ORIGINS', '*').split(',')}})
    csrf = CSRFProtect(app)
    
    setup_logging(app)
    
    from .routes import bp
    app.register_blueprint(bp)
    
    return app

def setup_logging(app):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Security Flask application startup')
