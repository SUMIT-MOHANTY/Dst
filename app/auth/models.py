from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    _users = {
        1: {'id': 1, 'username': 'admin', 'password_hash': generate_password_hash('secure_password_123')}
    }
    
    def __init__(self, user_id):
        self.id = user_id
        self.username = self._users[user_id]['username']
    
    @classmethod
    def get_by_id(cls, user_id):
        if user_id in cls._users:
            return cls(user_id)
        return None
    
    @classmethod
    def authenticate(cls, username, password):
        for uid, user in cls._users.items():
            if user['username'] == username and check_password_hash(user['password_hash'], password):
                return cls(uid)
        return None
