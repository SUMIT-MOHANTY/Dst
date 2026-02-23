from app import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)
    email = db.Column(db.String(100))
    skills = db.relationship('Skill', backref='profile', lazy=True)
    projects = db.relationship('Project', backref='profile', lazy=True)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(20))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    technologies = db.Column(db.String(200))
    link = db.Column(db.String(200))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
