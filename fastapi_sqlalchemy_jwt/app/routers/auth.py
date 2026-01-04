from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import create_access_token, hash_password, verify_password
from app.schemas.auth import UserCreate, Token
from app.db.models import User
from app.db.session import SessionLocal

router = APIRouter(prefix="/auth", tags=["auth"])


# 🔹 Dependency для отримання сесії БД
def get_db():
    """
    Створює сесію БД для кожного запиту і закриває після використання.
    """
    db = SessionLocal()
    try:
        yield db  # Передає сесію в ендпоїнт
    finally:
        db.close()  # Закриває з'єднання після завершення


# 🔹 Реєстрація
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Реєстрація нового користувача.
    
    1. Перевіряє чи email вже існує
    2. Хешує пароль
    3. Зберігає в БД
    4. Повертає JWT токен
    """
    # Перевіряємо чи користувач з таким email вже існує
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Хешуємо пароль
    hashed_pwd = hash_password(user.password)
    
    # Створюємо нового користувача
    new_user = User(
        email=user.email,
        hashed_password=hashed_pwd
    )
    
    # Зберігаємо в БД
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Оновлює об'єкт (отримує id з БД)
    
    # Створюємо JWT токен
    access_token = create_access_token(data={"sub": str(new_user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}


# 🔹 Логін
@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    """
    Авторизація користувача.
    
    1. Знаходить користувача за email
    2. Перевіряє пароль
    3. Повертає JWT токен
    """
    # Шукаємо користувача в БД
    db_user = db.query(User).filter(User.email == user.email).first()
    
    # Якщо користувача не знайдено
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    # Перевіряємо пароль
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    # Створюємо JWT токен
    access_token = create_access_token(data={"sub": str(db_user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}
