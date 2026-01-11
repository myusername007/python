from sqlalchemy.orm import Session, joinedload
from app.db.models import User
from app.core.security import hash_password
from typing import Optional

class UserService:

    def create_user(self, db: Session, email: str, password: str) -> User:
        user = User(
            email=email,
            hashed_password=hash_password(password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_all_users(
            self, 
            db: Session, 
            limit: int = 10, 
            offset: int = 0, 
            email_contains: str | None = None
        ) -> list[User]:

        query =  db.query(User)

        if email_contains:
            query = query.filter(User.email.contains(email_contains))
        
        return query.offset(offset).limit(limit).all()
    
    def get_user_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
    
    def delete_user(self, db: Session, user: User) -> None:
        db.delete(user) 
        db.commit()

    def exists_by_email(self, db: Session, user_email: str) -> User:
        return db.query(User).filter(User.email == user_email).first()
    
    def get_user_with_posts(
            self,
            db: Session,
            user_id: int
    ):
        return db.query(User).filter(User.id == user_id).options(joinedload(User.posts)).first()


