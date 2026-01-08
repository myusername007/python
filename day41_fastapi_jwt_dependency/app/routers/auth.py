from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.deps import get_db

router = APIRouter()
service = UserService()

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if service.exists_by_email(db, user.email):
        raise HTTPException(
            status_code=400, 
            detail="Email already exists"
        )

    return service.create_user(db, user.email, user.password)

@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    token = AuthService().login(
        db,
        form_data.username,
        form_data.password
    )
    if not token:
        raise HTTPException(
            status_code=401, 
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
