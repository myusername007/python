from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead
from app.deps import get_db
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    exists = user_service.exists_by_email(db, user.email)
    if exists:
        raise HTTPException(
            status_code=400,
            detail="Email already used!"
        )
    return user_service.create_user(db, user.email)

@router.get("/", response_model=list[UserRead], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

@router.get("/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    user_service.delete_user(db, user)
    return {"status": "deleted"}

