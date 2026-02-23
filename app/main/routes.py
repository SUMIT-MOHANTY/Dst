from app.main import bp
from flask import render_template

@bp.route('/')
@bp.route('/index')
def index():
    return 'Hello World'

@bp.route('/health')
def health():
    return {'status': 'ok'}
