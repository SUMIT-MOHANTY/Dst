from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config

login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    csrf.init_app(app)

    from app.auth.routes import auth as auth_bp
    from app.admin.routes import admin as admin_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app
