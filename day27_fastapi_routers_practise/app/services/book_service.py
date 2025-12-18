from database import add_book, get_books
from fastapi import HTTPException, status

def create_book(book):
    add_book(book)
    return book

def list_books():
    books = get_books()
    if not books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No books found."
        )
    return books

