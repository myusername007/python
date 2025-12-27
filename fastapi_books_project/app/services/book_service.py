from database import (
    add_book, 
    get_books,
    get_book_by_id,
    delete_book,
    update_book
)
from fastapi import HTTPException, status

class BookService:
    def __init__(self):
        pass

    def create_book(self,book):
        add_book(book)
        return book

    def list_books(self):
        books = get_books()
        if not books:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No books found."
            )
        return books

    def get_book(self,book_id: int):
        book = get_book_by_id(book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
        return book

    def remove_book(self,book_id: int):
        book = get_book_by_id(book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
                )
        delete_book(book_id)

    def update_book_data(self, book_id: int, data: dict):
        book = get_book_by_id(book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
                )
        updated_book = update_book(book_id, data)
        return updated_book
    
def get_book_service():
    return BookService()