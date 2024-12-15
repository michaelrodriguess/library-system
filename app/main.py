from fastapi import FastAPI
from app.controllers.book_controller import router as book_router

app = FastAPI()

app.include_router(book_router, prefix="/books", tags=["Books"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library System!"}