from sqlalchemy.orm import Session
from app.db.models import Post, User

class PostService:

    def create_post(
        self,
        db: Session,
        user: User,
        title: str,
    ) -> Post:
        post = Post(
            title=title,
            user_id = user.id
        )
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
    
    def get_posts_by_user(
            self,
            db: Session,
            user_id: int,
            order: str = "desc"
    ) -> list[Post]:
        query = self._base_query(db).filter(Post.user_id == user_id)
    
        if order == "asc":
            query = query.order_by(Post.created_at.asc())
        else:
            query = query.order_by(Post.created_at.desc())
        return query.all()
    
    
    def get_by_id(self, db: Session, post_id: int) -> Post | None:
        return self._base_query(db).filter(Post.id == post_id).first()
    
    def update_post(
            self,
            db: Session,
            post: Post,
            title: str
    ) -> Post:
        post.title = title
        db.commit()
        db.refresh(post)
        return post
    
    def soft_delete_post(
            self,
            db: Session,
            post: Post
    ) -> None:
        post.is_deleted = True
        db.commit()

    def _base_query(self, db: Session):
        return db.query(Post).filter(Post.is_deleted == False)
    