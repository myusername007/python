from database import add_author, get_authors
from fastapi import HTTPException, status

class AuthorService():
    def __init__(self):
        pass

    def create_author(self, author):
        add_author(author)
        return author

    def list_authors(self):
        authors = get_authors()
        if not authors:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No authors found."
            )
        return authors

def get_author_service():
    return AuthorService()