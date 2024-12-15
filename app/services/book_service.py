from app.repositories.book_repository import BookRepository
from app.entities.book import Book

class BookService:
    def __init__(self):
        self.repository = BookRepository()        

    def add_book(self, title: str, author: str, description: str = None) -> Book:
        book = Book(title=title, author=author, description=description)
        return self.repository.create_book(book)

    def list_books(self) -> list[Book]:
        return self.repository.get_books()