from app import create_app, db
from app.models import Profile, Skill, Project

app = create_app()

with app.app_context():
    db.create_all()
    
    profile = Profile(
        name='Nitesh Saw',
        title='Full Stack Developer',
        bio='Experienced developer specializing in web applications and database design.',
        email='nitesh.saw@example.com'
    )
    db.session.add(profile)
    
    skills = [
        Skill(name='Python', category='Backend'),
        Skill(name='Flask', category='Backend'),
        Skill(name='PostgreSQL', category='Database'),
        Skill(name='JavaScript', category='Frontend'),
        Skill(name='React', category='Frontend'),
        Skill(name='Docker', category='DevOps')
    ]
    for skill in skills:
        db.session.add(skill)
    
    projects = [
        Project(
            title='Portfolio Website',
            description='Personal portfolio showcasing projects and skills.',
            technologies='Flask, SQLAlchemy, HTML, CSS'
        ),
        Project(
            title='Task Management App',
            description='Full-featured task management application with user authentication.',
            technologies='React, Node.js, MongoDB'
        ),
        Project(
            title='E-commerce Platform',
            description='Online store with payment integration and inventory management.',
            technologies='Python, Django, Stripe'
        )
    ]
    for project in projects:
        db.session.add(project)
    
    db.session.commit()
    print('Database seeded successfully with Nitesh Saw profile data!')
