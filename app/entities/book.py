from uuid import uuid4

class Book:
    def __init__(self, title: str, author: str, description: str = None, id: int = None):
        self.id = id  
        self.title = title
        self.author = author
        self.description = description

