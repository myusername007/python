#books storage
_books = []
_book_id_counter = 1

#Books operations
def get_books():
    return _books

def add_book(book):
    global _book_id_counter
    book.id = _book_id_counter
    _books.append(book)
    _book_id_counter +=1
    return book

def get_book_by_id(book_id: int):
    for book in _books:
        if book.id == book_id:
            return book
    return None

def delete_book(book_id: int):
    global _books
    _books = [b for b in _books if b.id != book_id]

def update_book(book_id: int, data: dict):
    for book in _books:
        if book.id == book_id:
            for key,value in data.items():
                setattr(book,key,value)
            return book
    return None







#authors storage
_authors = []

#Authors operations
def get_authors():
    return _authors

def add_author(author):
    _authors.append(author)
