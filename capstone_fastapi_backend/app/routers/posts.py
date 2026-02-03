from fastapi import APIRouter

router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/ping")
def ping():
    return {"ok": True}

