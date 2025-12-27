from fastapi.testclient import TestClient
from main import app
from services.book_service import get_book_service, BookService

app.dependency_overrides[get_book_service] = lambda: FakeBookService()

client = TestClient(app)

class FakeBookService(BookService):
    def list_books(self):
        return []
    
def test_get_books_override():
    response = client.get("/books")

    assert response.status_code == 201
    assert response.json() == []
