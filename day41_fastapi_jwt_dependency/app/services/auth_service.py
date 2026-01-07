from sqlalchemy.orm import Session
from app.services.user_service import UserService
from app.core.security import verify_password, create_access_token

class AuthService:

    def login(self, db: Session, email: str, password: str) -> str | None:
        user = UserService().exists_by_email(db, email)
        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return create_access_token(user.id)
