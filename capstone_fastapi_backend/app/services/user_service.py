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
    
    def get_by_email(self, db: Session, user_email: str) -> User:
        return db.query(User).filter(User.email == user_email).first()

    def get_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
    