from pydantic import BaseModel

class Book(BaseModel):
    # This Python class represents a book with attributes for title, author, and publication year.
    title: str
    author: str
    publication_year: int

class Review(BaseModel):
    # The class Review defines attributes for a book review including book_id, text, and rating.
    book_id: int
    text: str
    rating: int