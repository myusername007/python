from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.post import PostCreate, PostRead
from app.services.post_service import PostService
from app.deps import get_current_user, get_db

router = APIRouter()
service = PostService()

@router.post("/", response_model=PostRead)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.create_post(db, current_user, post.title)

@router.get("/me", response_model=list[PostRead])
def my_posts(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.get_posts_by_user(db, current_user.id)