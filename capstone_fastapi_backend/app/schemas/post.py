from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str

class PostRead(BaseModel):
    id: int
    title: str
    user_id: int

    class Config:
        from_attributes = True