from flask import Blueprint, render_template
from app.models import Profile, Skill, Project
from app import db

main = Blueprint("main", __name__)

@main.route("/")
def index():
    profile = Profile.query.first()
    skills = Skill.query.all()
    projects = Project.query.all()
    return render_template("index.html", profile=profile, skills=skills, projects=projects)
