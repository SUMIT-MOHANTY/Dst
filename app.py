from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'admin-secret-key-2024'

DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'bio': '', 'projects': []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', bio=data['bio'], projects=data['projects'])

@app.route('/admin')
def admin():
    data = load_data()
    return render_template('admin.html', bio=data['bio'], projects=data['projects'])

@app.route('/admin/bio', methods=['POST'])
def update_bio():
    data = load_data()
    data['bio'] = request.form.get('bio', '')
    save_data(data)
    flash('Bio updated successfully!')
    return redirect(url_for('admin'))

@app.route('/admin/project/add', methods=['POST'])
def add_project():
    data = load_data()
    project = {
        'id': len(data['projects']) + 1,
        'title': request.form.get('title', ''),
        'description': request.form.get('description', ''),
        'link': request.form.get('link', '')
    }
    data['projects'].append(project)
    save_data(data)
    flash('Project added successfully!')
    return redirect(url_for('admin'))

@app.route('/admin/project/edit/<int:pid>', methods=['POST'])
def edit_project(pid):
    data = load_data()
    for p in data['projects']:
        if p['id'] == pid:
            p['title'] = request.form.get('title', '')
            p['description'] = request.form.get('description', '')
            p['link'] = request.form.get('link', '')
            break
    save_data(data)
    flash('Project updated successfully!')
    return redirect(url_for('admin'))

@app.route('/admin/project/delete/<int:pid>')
def delete_project(pid):
    data = load_data()
    data['projects'] = [p for p in data['projects'] if p['id'] != pid]
    save_data(data)
    flash('Project deleted successfully!')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
