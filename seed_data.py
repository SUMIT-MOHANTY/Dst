from app import create_app, db
from app.models import Profile, Skill, Project

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    
    # Nitesh Saw's Profile
    profile = Profile(
        name="Nitesh Saw",
        title="Full Stack Developer",
        bio="Passionate full stack developer with expertise in Python, JavaScript and cloud technologies. Building scalable web applications and solving complex problems.",
        email="nitesh.saw@example.com",
        linkedin="https://linkedin.com/in/niteshsaw",
        github="https://github.com/niteshsaw"
    )
    db.session.add(profile)
    
    # Skills
    skills = [
        Skill(name="Python", category="Backend"),
        Skill(name="JavaScript", category="Frontend"),
        Skill(name="React", category="Frontend"),
        Skill(name="Node.js", category="Backend"),
        Skill(name="PostgreSQL", category="Database"),
        Skill(name="MongoDB", category="Database"),
        Skill(name="Docker", category="DevOps"),
        Skill(name="AWS", category="Cloud"),
        Skill(name="Flask", category="Backend"),
        Skill(name="FastAPI", category="Backend")
    ]
    for skill in skills:
        db.session.add(skill)
    
    # Projects
    projects = [
        Project(
            name="E-Commerce Platform",
            description="A full-featured e-commerce platform with payment integration, inventory management, and real-time order tracking.",
            technologies="React, Node.js, PostgreSQL, Stripe, Redis",
            github_url="https://github.com/niteshsaw/ecommerce-platform"
        ),
        Project(
            name="Task Management App",
            description="Collaborative task management tool with real-time updates, team workspaces, and progress analytics.",
            technologies="React, FastAPI, MongoDB, WebSocket",
            github_url="https://github.com/niteshsaw/task-manager"
        ),
        Project(
            name="Data Analytics Dashboard",
            description="Interactive dashboard for visualizing large datasets with custom charts, filters, and export capabilities.",
            technologies="Python, D3.js, Flask, PostgreSQL",
            github_url="https://github.com/niteshsaw/analytics-dashboard"
        )
    ]
    for project in projects:
        db.session.add(project)
    
    db.session.commit()
    print("Successfully seeded Nitesh Saw's profile, skills, and projects!")
