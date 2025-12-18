from services.author_service import create_author, list_authors
from fastapi import APIRouter, status
from models import Author

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

@router.get("/")
def get_authors():
    return list_authors()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_author(author: Author):
    return create_author(author)