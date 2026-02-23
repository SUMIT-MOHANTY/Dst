from flask import Flask
from flask_login import LoginManager
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.session_protection = 'strong'
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.auth.models import User
        return User.get_by_id(int(user_id))
    
    from app.auth.routes import auth_bp
    from app.admin.routes import admin_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    return app
