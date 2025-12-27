import pytest
from services.book_service import BookService
from models import Book, BookCreate

def test_create_book():
    service = BookService()

    book = Book(
        title = "Crime and Punishment",
        author = "Dostoevskiy",
        year = 1866
    )
    book1 = Book(
        title = "Crime and Punishment",
        author = "Dostoevskiy",
        year = 1867
    )

    result = service.create_book(book)
    result1 = service.create_book(book1)

    assert result.id == 1
    assert result.year == 1866
    assert result1.id == 2
    assert result1.year == 1868
