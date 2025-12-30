from fastapi import HTTPException, APIRouter, Header
from security.simple_jwt import decode_token

router = APIRouter(prefix="/protected")

@router.get("/")
def protected(token: str = Header(...)):
    try:
        payload = decode_token(token)
        return {"user": payload["username"]}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")