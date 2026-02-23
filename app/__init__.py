from flask import Flask
from .config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .routes import ai_bp
    app.register_blueprint(ai_bp, url_prefix='/api/ai')
    return app
