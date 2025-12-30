from fastapi import APIRouter
from security.simple_jwt import create_token

router = APIRouter(prefix="/auth-simple")

@router.get("/login")
def login(username: str):
    token = create_token(username)
    return {"token": token}