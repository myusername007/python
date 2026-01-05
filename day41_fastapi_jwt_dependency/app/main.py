from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routers import users, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])