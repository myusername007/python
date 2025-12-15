from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

users = []

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"status": "success", "user": user}

@app.get("/users")
def get_users():
    return users

