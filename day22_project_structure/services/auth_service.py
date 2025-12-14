from models.user import User
from utils.validators import is_valid_email

def register_user(username, email, age):
    if not is_valid_email(email):
        raise ValueError("Invalid email")

    user = User(username, email, age)
    return user
