from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from app.models import get_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userid')
        password = request.form.get('password')
        user = get_user(user_id)

        if user and user.verify_password(password):
            # Mitigate Session Fixation: clear session before login
            session.clear() 
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
