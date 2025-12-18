from fastapi import APIRouter, status
from models.user import User
from services.user_service import create_user, list_users

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return list_users()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    return create_user(user)
