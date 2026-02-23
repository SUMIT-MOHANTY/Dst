from flask import Flask, render_template, jsonify
from models import db, Profile, Skill, Project
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    profile = Profile.query.first()
    skills = Skill.query.all()
    projects = Project.query.all()
    return render_template('index.html', profile=profile, skills=skills, projects=projects)

@app.route('/api/profile')
def api_profile():
    profile = Profile.query.first()
    return jsonify({'name': profile.name, 'title': profile.title, 'email': profile.email, 'bio': profile.bio} if profile else {})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
