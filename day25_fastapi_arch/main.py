from fastapi import FastAPI, status
from models.user import User
from services.user_service import create_user, list_users

app = FastAPI()

@app.get("/users")
def get_users():
    return list_users()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    return create_user(user)
