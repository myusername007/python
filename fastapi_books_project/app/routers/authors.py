from services.author_service import (
    get_author_service,
    AuthorService
)
from fastapi import APIRouter, status, Depends
from models import Author
from security.api_key import get_api_key

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

@router.get("/")
def get_authors(service: AuthorService = Depends(get_author_service)):
    return service.list_authors()

@router.post("/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_api_key)])
def add_author(author: Author, service: AuthorService = Depends(get_author_service)):
    return service.create_author(author)