from app import app, db
from models import Profile, Skill, Project

def seed_database():
    with app.app_context():
        db.create_all()
        
        # Clear existing data
        Profile.query.delete()
        Skill.query.delete()
        Project.query.delete()
        
        # Create Nitesh Saw's profile
        profile = Profile(
            name='Nitesh Saw',
            title='Full Stack Developer',
            email='nitesh.saw@example.com',
            bio='Passionate full stack developer with 5+ years of experience building scalable web applications. Expert in Python, JavaScript, and cloud technologies.',
            linkedin='https://linkedin.com/in/niteshsaw',
            github='https://github.com/niteshsaw'
        )
        db.session.add(profile)
        
        # Create skills
        skills_data = [
            ('Python', 'Backend', 95),
            ('JavaScript', 'Frontend', 90),
            ('React', 'Frontend', 85),
            ('Node.js', 'Backend', 88),
            ('PostgreSQL', 'Database', 82),
            ('Docker', 'DevOps', 78),
            ('AWS', 'Cloud', 80),
            ('Flask', 'Backend', 92),
            ('TypeScript', 'Frontend', 75),
            ('MongoDB', 'Database', 85)
        ]
        for name, category, level in skills_data:
            db.session.add(Skill(name=name, category=category, level=level))
        
        # Create projects
        projects_data = [
            ('E-Commerce Platform', 'Full-featured e-commerce solution with payment integration and inventory management.', 'React, Node.js, PostgreSQL, Stripe', 'https://github.com/niteshsaw/ecommerce', 'https://demo-ecommerce.com'),
            ('Task Management App', 'Collaborative task manager with real-time updates and team features.', 'Python, Flask, Vue.js, WebSocket', 'https://github.com/niteshsaw/taskmanager', 'https://tasks.example.com'),
            ('Data Analytics Dashboard', 'Interactive dashboard for visualizing business metrics and KPIs.', 'Python, Pandas, D3.js, Flask', 'https://github.com/niteshsaw/analytics', None),
            ('API Gateway Service', 'Microservices API gateway with authentication and rate limiting.', 'Node.js, Express, Redis, JWT', 'https://github.com/niteshsaw/apigateway', None)
        ]
        for name, desc, tech, github, live in projects_data:
            db.session.add(Project(name=name, description=desc, technologies=tech, github_url=github, live_url=live))
        
        db.session.commit()
        print('Database seeded successfully with Nitesh Saw\'s data!')
        print(f'Profile: {profile.name}')
        print(f'Skills: {len(skills_data)}')
        print(f'Projects: {len(projects_data)}')

if __name__ == '__main__':
    seed_database()
