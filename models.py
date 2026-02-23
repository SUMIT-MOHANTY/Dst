from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100))
    email = db.Column(db.String(100))
    bio = db.Column(db.Text)
    linkedin = db.Column(db.String(200))
    github = db.Column(db.String(200))

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50))
    level = db.Column(db.Integer)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    technologies = db.Column(db.String(200))
    github_url = db.Column(db.String(200))
    live_url = db.Column(db.String(200))
