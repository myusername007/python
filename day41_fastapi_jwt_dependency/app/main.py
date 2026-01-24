from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routers import users, auth, posts

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])