import pytest
from app import create_app, db

def pytest_configure():
    pytest.secret_key = 'test-secret-key'

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
