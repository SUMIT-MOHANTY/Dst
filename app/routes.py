from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Placeholder data for the homepage
    context = {
        'title': 'Secure Homepage',
        'content': 'Welcome to the secure application.',
        'items': ['Feature A', 'Feature B', 'Feature C']
    }
    # [RISK 1 MITIGATION] Jinja2 auto-escaping is enabled by default to prevent XSS.
    return render_template('index.html', **context)
