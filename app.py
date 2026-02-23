import os
from flask import Flask, jsonify
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
app.config['DEBUG'] = False
@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
