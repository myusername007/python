from storage.user_storage import add_user, get_all_users
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