from database import init_db
from models import Base, Profile, Project, Skill, ContactMessage

if __name__ == '__main__':
    init_db()
    print('Database tables created successfully!')
