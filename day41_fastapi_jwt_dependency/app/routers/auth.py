from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.services.user_service import UserService
from app.core.security import create_access_token
from app.deps import get_db
from app.schemas.user import UserCreate

router = APIRouter()
user_service = UserService()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = user_service.exists_by_email(db, form_data.username)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid Credentials" )
    
    token = create_access_token({"sub": str(db_user.id)})
    return {"access_token": token, "token_type": "bearer"}

