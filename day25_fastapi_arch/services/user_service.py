from storage.user_storage import (
    add_user, 
    get_all_users, 
    get_user_by_id, 
    delete_user,
    update_user
)
from fastapi import HTTPException, status

def create_user(user):
    if user.age < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Age must be positive"
        )
    add_user(user)
    return user

def list_users():
    users = get_all_users()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No users found"
        )
    return get_all_users()

def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

def remove_user(user_id: int):
     user = get_user_by_id(user_id)
     if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
            )
     delete_user(user_id)

def update_user_data(user_id: int, data: dict):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    updated_user = update_user(user_id, data)
    return updated_user

class UserService:
    def __init__(self):
        pass

    def create_user(self, user):
        add_user(user)
        return user
    
    def list_users(self):
        users = get_all_users()
        if not users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No users found"
            )
        return users
    
def get_user_service():
    return UserService()