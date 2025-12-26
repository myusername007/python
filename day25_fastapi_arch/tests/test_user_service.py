import pytest
from services.user_service import UserService
from models.user import User

def test_create_user():
    service = UserService()

    user = User(
        id=1,
        username="roma",
        email="roma@mail.com",
        age=21
    )

    result = service.create_user(user)

    assert result.username == "roma"
    assert result.age == 21
    assert result.id != 2
    