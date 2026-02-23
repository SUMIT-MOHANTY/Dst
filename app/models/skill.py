from datetime import datetime
from app import db

class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    proficiency_level = db.Column(db.Integer)
    years_experience = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', back_populates='skills')
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'category': self.category, 'proficiency_level': self.proficiency_level}
