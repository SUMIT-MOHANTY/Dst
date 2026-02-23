import os
from flask import Flask
from config import config

def create_app(config_name=None):
    app = Flask(__name__)
    
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'production')
    
    app.config.from_object(config[config_name])
    
    @app.route('/')
    def index():
        return 'Flask Production Configured'
    
    @app.route('/health')
    def health():
        return {'status': 'healthy'}, 200
    
    return app

app = create_app()
