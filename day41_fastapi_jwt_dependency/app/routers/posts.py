from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.post import PostCreate, PostRead, PostUpdate
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

@router.put("/{post_id}", response_model=PostRead, status_code=status.HTTP_200_OK)
def update_post(
    post_id: int,
    data: PostUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    post = service.get_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )
    return service.update_post(db, post, data.title)

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    post = service.get_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )
    service.delete_post(db, post)
    return None
        