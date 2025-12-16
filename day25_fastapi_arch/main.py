from fastapi import FastAPI
from models.user import User
from services.user_service import create_user, list_users

app = FastAPI()

@app.get("/users")
def get_users():
    return list_users()

@app.post("/users")
def add_user(user: User):
    return create_user(user)
