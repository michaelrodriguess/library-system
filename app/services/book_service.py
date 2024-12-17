from app.repositories.book_repository import BookRepository
from app.entities.book import Book

class BookService:
    def __init__(self):
        self.repository = BookRepository()        

    def add_book(self, title: str, author: str, description: str = None) -> Book:
        book = Book(title=title, author=author, description=description)
        return self.repository.create_book(book)

    def get_all_books(self) -> list[Book]:
        return self.repository.get_all_books()
    
    def get_books_by_author(self, author: str) -> list[Book]:
        return self.repository.get_books_by_author(author)
    
    def get_books_by_title(self, title: str) -> list[Book]:
        return self.repository.get_books_by_title(title)
    
    def delete_book(self, book_id: int) -> None:
        self.repository.delete_book(book_id)
        