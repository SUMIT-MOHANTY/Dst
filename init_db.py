from database import engine, Base
from models import AdminUser, Project

def init_database():
    Base.metadata.create_all(bind=engine)
    print('Database tables created successfully.')

if __name__ == '__main__':
    init_database()
