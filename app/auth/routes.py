from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, current_user
from app.auth.forms import LoginForm
from app.auth.models import User
from functools import wraps
import time

auth_bp = Blueprint('auth', __name__)

login_attempts = {}
MAX_ATTEMPTS = 5
LOCKOUT_TIME = 300

def check_rate_limit(username):
    now = time.time()
    if username in login_attempts:
        attempts = [t for t in login_attempts[username] if now - t < LOCKOUT_TIME]
        if len(attempts) >= MAX_ATTEMPTS:
            return False
        login_attempts[username] = attempts
    return True

def record_login_attempt(username):
    if username not in login_attempts:
        login_attempts[username] = []
    login_attempts[username].append(time.time())

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        if not check_rate_limit(form.username.data):
            flash('Account locked. Try again later.', 'error')
            return render_template('auth/login.html', form=form)
        
        record_login_attempt(form.username.data)
        
        user = User.authenticate(form.username.data, form.password.data)
        if user:
            session.regenerate()
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('admin.dashboard'))
        flash('Invalid username or password.', 'error')
    
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
