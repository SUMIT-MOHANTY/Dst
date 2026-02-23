import os
from app import create_app

env = os.environ.get('FLASK_ENV', 'development')
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc' if env != 'production' else None)
