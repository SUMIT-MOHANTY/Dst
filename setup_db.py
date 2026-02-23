from portfolio import create_app, db
from portfolio.models import Profile, Project, Skill, ContactMessage

app = create_app()

with app.app_context():
    db.create_all()
    print('Database tables created successfully!')
