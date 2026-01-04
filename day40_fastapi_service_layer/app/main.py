from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])