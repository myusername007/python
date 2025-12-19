from fastapi import APIRouter, status
from models.user import User
from services.user_service import (
    create_user, 
    list_users, 
    get_user, 
    remove_user
)
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return list_users()

@router.get("/{user.id}")
def get_user_by_id(user_id: int):
    return get_user(user_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    return create_user(user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    remove_user(user_id)