from fastapi import APIRouter
from app.services.book_service import BookService
from app.schemas.book import BookCreate, BookResponse

router = APIRouter()
service = BookService()

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate):
    return service.add_book(**book.dict())

@router.get("/", response_model=list[BookResponse])
def get_books():
    return service.get_all_books()

@router.get("/author/{author}", response_model=list[BookResponse])
def get_books_by_author(author: str):
    return service.get_books_by_author(author)

@router.get("/title/{title}", response_model=list[BookResponse])
def get_books_by_title(title: str):
    return service.get_books_by_title(title)

@router.delete("/{book_id}")
def delete_book(book_id: str):
    service.delete_book(book_id)
    return {"message": "Book with id '{book_id}' was deleted successfully."}