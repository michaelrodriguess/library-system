from app.entities.book import Book
from app.database import get_connection

class BookRepository:
    def create_book(self, book: Book) -> Book:
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO books (title, author, description) VALUES (%s, %s, %s)",
                        (book.title, book.author, book.description),
                    )
                    book.id = cursor.lastrowid
                    # conn.commit() Only confirms querys if all the above operations are successful
            return book
        except Exception as e:
            print(f"Error creating book: {e}")
            # conn.rollback() Revert changes if something goes wrong
            raise

    def get_all_books(self) -> list[Book]:
        try:
            with get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute("SELECT id, title, author, description FROM books")
                    rows = cursor.fetchall()
                    return [Book(**row) for row in rows]
        except Exception as e:
            print(f"Error getting books: {e}")
            raise

    def get_books_by_author(self, author: str) -> list[Book]:
        try:
            with get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute("SELECT id, title, author, description FROM books WHERE author = %s", (author,))
                    rows = cursor.fetchall()
                    return [Book(**row) for row in rows]
        except Exception as e:
            print(f"Error getting books by author: {e}")
            raise

    def get_books_by_title(self, title: str) -> list[Book]:
        try:
            with get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute("SELECT id, title, author, description FROM books WHERE title = %s", (title,))
                    rows = cursor.fetchall()
                    return [Book(**row) for row in rows]
        except Exception as e:
            print(f"Error getting books by title: {e}")
            raise

    def delete_book(self, book_id: int) -> None:
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        except Exception as e:
            print(f"Error deleting book: {e}")
            raise