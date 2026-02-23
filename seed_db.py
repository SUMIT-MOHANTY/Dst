from app import app, db, Profile, Skill, Project

def seed_database():
    with app.app_context():
        db.create_all()
        
        # Check if data already exists
        if Profile.query.first():
            print('Database already seeded. Skipping.')
            return
        
        # Create Nitesh Saw's profile
        profile = Profile(
            name='Nitesh Saw',
            title='Full Stack Developer',
            bio='Passionate full stack developer with expertise in building scalable web applications. Experienced in Python, JavaScript, and modern web technologies.',
            email='nitesh.saw@example.com',
            location='San Francisco, CA'
        )
        db.session.add(profile)
        
        # Add skills
        skills_data = [
            ('Python', 'Backend', 'Advanced'),
            ('JavaScript', 'Frontend', 'Advanced'),
            ('Flask', 'Backend', 'Advanced'),
            ('React', 'Frontend', 'Intermediate'),
            ('SQL', 'Database', 'Advanced'),
            ('Docker', 'DevOps', 'Intermediate'),
            ('Git', 'Tools', 'Advanced'),
            ('REST APIs', 'Backend', 'Advanced')
        ]
        for name, category, proficiency in skills_data:
            skill = Skill(name=name, category=category, proficiency=proficiency)
            db.session.add(skill)
        
        # Add projects
        projects_data = [
            ('Portfolio Website', 'A personal portfolio website showcasing projects and skills with responsive design.', 'Flask, HTML, CSS', 'https://github.com/niteshsaw/portfolio', 'https://niteshsaw.dev'),
            ('Task Manager App', 'A web-based task management application with user authentication.', 'Flask, SQLAlchemy, JavaScript', 'https://github.com/niteshsaw/taskmanager', None),
            ('E-commerce API', 'RESTful API for an e-commerce platform with product management.', 'Flask, PostgreSQL, JWT', 'https://github.com/niteshsaw/ecommerce-api', None)
        ]
        for title, desc, tech, github, live in projects_data:
            project = Project(title=title, description=desc, technologies=tech, github_url=github, live_url=live)
            db.session.add(project)
        
        db.session.commit()
        print('Database seeded successfully with Nitesh Saw\'s data!')

if __name__ == '__main__':
    seed_database()
