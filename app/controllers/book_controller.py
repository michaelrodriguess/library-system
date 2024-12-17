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
    return service.get_books()