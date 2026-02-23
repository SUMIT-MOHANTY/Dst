from app import create_app, db
from app.models import User, Project, Skill

app = create_app()

with app.app_context():
    db.create_all()
    print('Database tables created successfully!')
    print(f'Tables: {User.__tablename__}, {Project.__tablename__}, {Skill.__tablename__}')
