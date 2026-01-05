from sqlalchemy.orm import Session
from app.db.models import User

class UserService:

    def create_user(self, db: Session, email: str) -> User:
        user = User(email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def get_all_users(self, db: Session) -> list[User]:
        return db.query(User).all()
    
    def get_user_by_id(self, db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.id == user_id).first()
    
    def delete_user(self, db: Session, user: User) -> None:
        db.delete(user) 
        db.commit()

    def exists_by_email(self, db: Session, user_email: str) -> User:
        return db.query(User).filter(User.email == user_email).first()


