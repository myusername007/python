from services.book_service import create_book, list_books
from fastapi import APIRouter, status
from models import Book

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.get("/")
def get_books():
    return list_books()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    return create_book(book)

