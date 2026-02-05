from fastapi import FastAPI
from app.routers import auth, posts, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(users.router)
