from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome! Try /error404 or /error500 to see error pages</h1>'

@app.route('/error404')
def trigger_404():
    from flask import abort
    abort(404)

@app.route('/error500')
def trigger_500():
    from flask import abort
    abort(500)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
