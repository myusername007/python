from fastapi import APIRouter, status, Depends
from models.user import User, UserUpdate
from services.user_service import (
    create_user, 
    list_users, 
    get_user, 
    remove_user,
    update_user_data,
    get_user_service,
    UserService
)
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users(service: UserService = Depends(get_user_service)):
    return service.list_users()

@router.get("/{user.id}")
def get_user_by_id(user_id: int):
    return get_user(user_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: User, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    remove_user(user_id)

@router.patch("/{user_id}")
def update_user(user_id: int, user_data: UserUpdate):
    data = user_data.model_dump(exclude_unset=True)
    return update_user_data(user_id, data)
    