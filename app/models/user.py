from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    full_name = db.Column(db.String(200))
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    projects = db.relationship('Project', back_populates='user', cascade='all, delete-orphan')
    skills = db.relationship('Skill', back_populates='user', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'full_name': self.full_name, 'bio': self.bio}
