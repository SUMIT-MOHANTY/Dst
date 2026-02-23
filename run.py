<<<<<<< HEAD
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
=======
import os
from app import create_app

os.environ['FLASK_ENV'] = 'development'
os.environ['DEBUG'] = 'True'

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 7ff1ce1 (Agent: Flask Environment Initialization)
