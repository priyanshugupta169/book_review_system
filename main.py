from fastapi import FastAPI, Depends
from book_review.schemas import Book, Review
from sqlalchemy.orm import Session
from database import engine, get_db
import book_review.models as models
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/books/")
def add_book(book: Book, db: Session = Depends(get_db)):
    """
    This method adds a new book to the database using FastAPI.
    
    Args:
        book (Book): The book parameter is of type `Book`, which is Pydantic model representing a book entity. It is used to receive data about a book that needs to be
              added to the database
        db (Session): The db parameter is a dependency that provides a database session.
    Returns:
        The book that was added to the database.
    """
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.post("/reviews/")
def add_review(review: Review, db: Session = Depends(get_db)):
    """
    The method adds a new reviews to the database using the provided Review object.
    
    Args:
        review (Review): It is Pydantic model representing a review entity
        db (Session): The db parameter is a database session object. 
    Returns: 
        return the db_review object that was added to the database.
    """
    db_review = models.Review(**review.model_dump())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


@app.get("/books/", response_model=List[Book])
def get_books(author: str = None, publication_year: int = None, db: Session = Depends(get_db)):
    """
    This method retrieves a list of books from a database based on optional filters for author
    and publication year.
    
    Args:
        author(str): It is used to filter the books based on the author's name. 
        publication_year(int): It is used to filter the books based on the year they were published. 
        db(Session): The db parameter is a database session object. 

    Returns
        A list of books that match the specified criteria (author and/or publication year) from the database.
    """
    query = db.query(models.Book)
    if author:
        query = query.filter(models.Book.author == author)
    if publication_year:
        query = query.filter(models.Book.publication_year == publication_year)
    return query.all()

@app.get("/reviews/{book_id}", response_model=List[Review])
def get_reviews_for_book(book_id: int, db: Session = Depends(get_db)):
    """
    This method retrieves all reviews for a specific book from the database based on the provided
    book_id.
    
    Args:
        book_id (int): unique identifier of a book for which you want to retrieve reviews
        db (Session): The db parameter is a database session object.  
    Returns:
        A list of reviews for the book with the specified book_id.
    """
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()
