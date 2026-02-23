from flask import Flask
<<<<<<< HEAD

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-key-123'
=======
from app.security import init_security
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    # Initialize Security Headers
    init_security(app)
    
    @app.route('/')
    def index():
        return 'App Secure'
    
>>>>>>> 7ff1ce1 (Agent: Flask Environment Initialization)
    return app
