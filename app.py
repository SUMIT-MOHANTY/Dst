from flask import Flask, jsonify, render_template, request
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'change-me-in-production'

csrf = CSRFProtect(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulation of secure data fetching
    return jsonify({'status': 'success', 'payload': [1, 2, 3]})

@app.route('/api/update', methods=['POST'])
@csrf.except # In SPA, we handle CSRF manually or via double-submit cookie. Here we simulate setup.
# Real implementation: Requires X-CSRFToken header logic.
def update_data():
    data = request.json
    if not data or 'value' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'status': 'updated', 'received': data['value']})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
