from app.models import User

def test_new_user_defaults(app):
    with app.app_context():
        user = User(username="testuser", email="test@example.com")
        db.session.add(user)
        db.session.commit()
        assert user.id is not None
        assert user.is_admin is False
