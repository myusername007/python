from fastapi import APIRouter, status, Depends
from models import Book, UpdateBook, BookCreate
from security.api_key import get_api_key
from services.book_service import (
    get_book_service,
    BookService
)

router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.get("/")
def get_books(service: BookService = Depends(get_book_service)):
    return service.list_books()

@router.get("/{book.id}")
def get_book_by_id(book_id: int, service: BookService = Depends(get_book_service)):
    return service.get_book(book_id)

@router.post("/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_api_key)])
def add_book(book: BookCreate, service: BookService = Depends(get_book_service)):
    #BookCreate -> Book
    new_book = Book(**book.model_dump())
    return service.create_book(new_book)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(get_api_key)])
def remove_book(book_id: int, service: BookService = Depends(get_book_service)):
    service.remove_book(book_id)

@router.patch("/{book_id}", dependencies=[Depends(get_api_key)])
def update_book(book_id: int, book_data: UpdateBook, service: BookService = Depends(get_book_service)):
    data = book_data.model_dump(exclude_unset=True)
    return service.update_book_data(book_id, data)

