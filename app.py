from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import json
import os

app = Flask(__name__)
app.secret_key = 'dev-secret-key-123'

MESSAGES_FILE = 'messages.json'
ADMIN_PASSWORD = 'admin123'

def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_messages(messages):
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    data = request.json
    messages = load_messages()
    message = {
        'id': len(messages) + 1,
        'name': data.get('name', ''),
        'email': data.get('email', ''),
        'subject': data.get('subject', ''),
        'message': data.get('message', ''),
        'timestamp': str(os.popen('date').read().strip())
    }
    messages.append(message)
    save_messages(messages)
    return jsonify({'success': True, 'message': 'Message sent successfully!'})

@app.route('/admin-login', methods=['POST'])
def admin_login():
    password = request.json.get('password', '')
    if password == ADMIN_PASSWORD:
        session['logged_in'] = True
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid password'})

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    messages = load_messages()
    return render_template('admin.html', messages=messages)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/delete-message/<int:msg_id>', methods=['POST'])
def delete_message(msg_id):
    if not session.get('logged_in'):
        return jsonify({'success': False})
    messages = load_messages()
    messages = [m for m in messages if m['id'] != msg_id]
    save_messages(messages)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
