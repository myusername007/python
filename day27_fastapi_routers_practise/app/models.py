from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    year: int

class Author(BaseModel):
    name: str
    country: str

    