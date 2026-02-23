from flask import Blueprint, render_template, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', page_title='Home')

@bp.route('/about')
def about():
    return render_template('about.html', page_title='About Us')

@bp.route('/projects')
def projects():
    return render_template('projects.html', page_title='Projects')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', page_title='Contact')

# JSON Data API
@bp.route('/api/info')
def api_info():
    return jsonify({
        'app_name': 'Secure Flask App',
        'version': '1.0.0',
        'status': 'operational'
    })
