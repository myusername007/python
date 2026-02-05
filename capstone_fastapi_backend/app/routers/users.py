from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead
from app.deps import get_db, get_current_user
from app.services.user_service import UserService

router = APIRouter()

@router.get("/me", response_model=UserRead, status_code=status.HTTP_200_OK)
def me(current_user = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }
