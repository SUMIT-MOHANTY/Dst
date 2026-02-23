def test_index_status(client):
    response = client.get("/")
    assert response.status_code == 200

def test_protected_route_redirect(client):
    response = client.get("/dashboard")
    assert response.status_code == 302 or response.status_code == 401

def test_post_request_rejects_invalid(client):
    response = client.post("/api/data", json={"bad": "data"})
    assert response.status_code == 400
