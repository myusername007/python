from datetime import datetime, timedelta
from typing import Any, Dict
import bcrypt
from jose import jwt
from app.core.config import settings


def hash_password(password: str) -> str:
    """
    Хешує пароль за допомогою bcrypt.
    
    Args:
        password: Пароль у вигляді plain text
        
    Returns:
        Захешований пароль
    """
    # Конвертуємо в байти і обрізаємо до 72 байтів
    password_bytes = password.encode('utf-8')[:72]
    # Генеруємо сіль і хешуємо
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    # Повертаємо як string
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Перевіряє чи відповідає plain text пароль захешованому.
    
    Args:
        plain_password: Пароль у вигляді plain text
        hashed_password: Захешований пароль з БД
        
    Returns:
        True якщо паролі співпадають, False якщо ні
    """
    # Конвертуємо обидва в байти
    password_bytes = plain_password.encode('utf-8')[:72]
    hashed_bytes = hashed_password.encode('utf-8')
    # Перевіряємо
    return bcrypt.checkpw(password_bytes, hashed_bytes)


def create_access_token(data: Dict[str, Any]) -> str:
    """
    Створює JWT access token.
    
    Args:
        data: Дані для кодування в токен (наприклад, {"sub": user_id})
        
    Returns:
        Закодований JWT токен
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt