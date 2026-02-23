from flask import Flask, jsonify
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    # Explicitly disable debug mode in execution unless env var overrides
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
