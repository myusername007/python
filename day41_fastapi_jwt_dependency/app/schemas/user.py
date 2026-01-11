from pydantic import BaseModel, EmailStr
from app.schemas.post import PostRead

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserRead(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class UserWithPosts(UserRead):
    posts: list[PostRead] = []