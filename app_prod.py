import os
from flask import Flask, session
from config import ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)

@app.route('/')
def home():
    session['visited'] = True
    return 'Production Flask App'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
