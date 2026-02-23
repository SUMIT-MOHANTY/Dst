import os
from app import create_app

env = os.environ.get('FLASK_ENV', 'production')
if env == 'development':
    from config import DevelopmentConfig
    app = create_app(DevelopmentConfig)
else:
    from config import Config
    app = create_app(Config)

if __name__ == '__main__':
    app.run()
