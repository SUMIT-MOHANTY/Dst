from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

# Mock DB for demo
users = {1: User(1, 'admin', 'SecureAdminPassword123!')}

def get_user(user_id):
    return users.get(int(user_id))
