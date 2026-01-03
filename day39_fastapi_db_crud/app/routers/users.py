from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import models
from app.schemas.user import UserCreate, UserRead
from app.deps import get_db

router = APIRouter()

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email = user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[UserRead], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/{id}", response_model=UserRead)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user_id = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user_id

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user_id = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user_id)
    db.commit()
