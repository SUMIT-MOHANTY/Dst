from datetime import datetime
from app import db

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    github_url = db.Column(db.String(500))
    live_url = db.Column(db.String(500))
    image_url = db.Column(db.String(500))
    technologies = db.Column(db.Text)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship('User', back_populates='projects')
    
    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'description': self.description, 'github_url': self.github_url, 'is_featured': self.is_featured}
