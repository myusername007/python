from fastapi import FastAPI
from routers.users import router as users_router
from routers.auth import router as auth_router

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)