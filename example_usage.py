from portfolio import create_app, db
from portfolio.models import Profile, Project, Skill, ContactMessage
from datetime import datetime

app = create_app()

with app.app_context():
    # Create a profile
    profile = Profile(
        full_name='John Doe',
        email='john.doe@example.com',
        phone='+1234567890',
        bio='Full Stack Developer with 5+ years of experience',
        linkedin_url='https://linkedin.com/in/johndoe',
        github_url='https://github.com/johndoe'
    )
    db.session.add(profile)
    
    # Create a project
    project = Project(
        profile_id=1,
        title='E-Commerce Platform',
        description='A full-featured e-commerce platform with payment integration',
        project_url='https://demo-store.example.com',
        github_url='https://github.com/johndoe/ecommerce',
        technologies='React, Node.js, PostgreSQL, Stripe',
        is_featured=True
    )
    db.session.add(project)
    
    # Create skills
    skill1 = Skill(profile_id=1, name='Python', category='Backend', proficiency_level='Expert', years_of_experience=5.0)
    skill2 = Skill(profile_id=1, name='JavaScript', category='Frontend', proficiency_level='Advanced', years_of_experience=4.0)
    db.session.add(skill1)
    db.session.add(skill2)
    
    # Create a contact message
    message = ContactMessage(
        name='Jane Smith',
        email='jane.smith@example.com',
        subject='Job Opportunity',
        message='Hi John, we have a great opportunity for you...'
    )
    db.session.add(message)
    
    db.session.commit()
    print('Sample data inserted successfully!')
    print(f'Profile: {profile.full_name}')
    print(f'Project: {project.title}')
    print(f'Skills: {[s.name for s in [skill1, skill2]]}')
    print(f'Message: {message.subject}')
