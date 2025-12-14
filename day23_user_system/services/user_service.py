from models.user import User
from utils.validators import is_valid_email

def create_user(username, email, age):
    if not is_valid_email(email):
        raise ValueError("Invalid email format")
    return User(username, email, age)

