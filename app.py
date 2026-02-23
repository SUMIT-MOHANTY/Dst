from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    message = request.form.get('message', '')
    return jsonify({'status': 'success', 'message': 'Message received!'})

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/data')
def api_data():
    return jsonify({'users': 125, 'messages': 45, 'sales': 3200})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
