import json
from tests.conftest import client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Welcome' in rv.data

def test_post_data(client):
    payload = {'data': 'input'}
    rv = client.post('/api/process', json=payload)
    assert rv.status_code == 202
    resp = json.loads(rv.data)
    assert 'status' in resp

def test_404_handler(client):
    rv = client.get('/nonexistent')
    assert rv.status_code == 404
