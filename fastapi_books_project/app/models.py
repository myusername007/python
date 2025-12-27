from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    year: int

class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

class Author(BaseModel):
    name: str
    country: str

    