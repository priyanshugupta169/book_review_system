from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Book(Base):
    # Book entity with attributes such as id, title, author, publication
    # year, and a relationship with the Review model.
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    publication_year = Column(Integer)

    # Define relationship with Review model
    reviews = relationship("Review", back_populates="book")


class Review(Base):
    # The Review class defines a model for storing book reviews with attributes such as text, rating,
    # and a relationship with the Book model.
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    text = Column(String)
    rating = Column(Integer)

    # Define relationship with Book model
    book = relationship("Book", back_populates="reviews")
