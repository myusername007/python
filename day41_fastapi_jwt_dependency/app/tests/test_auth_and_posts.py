from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_posts_me_no_auth():
    response = client.get("/posts/me")
    assert response.status_code == 401

def test_create_post_no_auth():
    response = client.post("/posts/", json={"title": "Test Post"})
    assert response.status_code == 401

def test_login_auth():
    response = client.post(
        "/auth/login", 
        data={"username": "user@example.com", "password": "string"
        
        }
)
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_update_post_auth():
    response = client.put("/posts/1", json={"title": "Updated Title"})
    assert response.status_code == 401

def test_put_with_auth():
    # First, log in to get a token
    login_response = client.post(
        "/auth/login",
        data={
            "username": "user@example.com",
            "password": "string"
        }
    )
    token = login_response.json().get("access_token")
    headers = {"Authorization": f"Bearer {token}"}
    # Now, attempt to update a post with the token
    response = client.put(
        "/posts/1",
        json = {"title": "Updated Title"},
        headers = headers
        )
    assert response.status_code == 200
    

    