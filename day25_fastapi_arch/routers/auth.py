from fastapi import APIRouter, Depends
from security.jwt import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}