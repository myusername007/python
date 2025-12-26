from fastapi.testclient import TestClient
from main import app
from services.user_service import UserService, get_user_service

app.dependency_overrides[get_user_service] = lambda: FakeUserService()

client = TestClient(app)

class FakeUserService(UserService):
    def list_users(self):
        return []
    

def test_get_users_with_override():
    response = client.get("/users")

    assert response.status_code == 200
    assert response.json() == []