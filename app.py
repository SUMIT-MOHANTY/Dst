import os
from flask import Flask, session

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-prod')
app.config['DEBUG'] = False
app.config['TESTING'] = False

@app.route('/')
def home():
    session['secure'] = 'test'
    return 'Flask configured for production'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
