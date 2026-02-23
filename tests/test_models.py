from app.models import User, db
from tests.conftest import app

def test_create_user(app):
    with app.app_context():
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        assert user.id is not None
        assert user.username == 'testuser'

def test_user_repr(app):
    with app.app_context():
        user = User(username='alice')
        assert repr(user) == '<User alice>'
