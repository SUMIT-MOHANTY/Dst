from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-prod'

contact_messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')
        if name and email and message:
            contact_messages.append({'name': name, 'email': email, 'message': message})
            flash('Message sent successfully!')
            return redirect(url_for('contact'))
        flash('Please fill all fields.')
    return render_template('contact.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', messages=contact_messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
