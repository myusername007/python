from database import add_author, get_authors
from fastapi import HTTPException, status

def create_author(author):
    add_author(author)
    return author

def list_authors():
    authors = get_authors()
    if not authors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No authors found."
        )
    return authors

