from fastapi.testclient import TestClient
from main import app
from database import TestSessionLocal, engine
from sqlalchemy.orm import Session
from book_review.models import Book, Review
import pytest

# Set up the test database
def setup_test_db():
    Book.metadata.create_all(bind=engine)
    Review.metadata.create_all(bind=engine)

# Define a fixture to provide a test database session to test cases
@pytest.fixture(scope="module")
def db_session():
    setup_test_db()
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()

client = TestClient(app)


# Test cases for POST method in books API
def test_add_book(db_session: Session):
    book_data = {"title": "New Book", "author": "John Doe", "publication_year": 2022}
    with TestClient(app) as client:
        response = client.post("/books/", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == book_data["title"]


# Test cases for GET methods in books API
def test_get_all_books(db_session: Session):
    with TestClient(app) as client:
        response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_books_by_author(db_session: Session):
    author = "J.K. Rowling"
    with TestClient(app) as client:
        response = client.get(f"/books/?author={author}")
    assert response.status_code == 200
    for book in response.json():
        assert book["author"] == author

def test_get_books_by_publication_year(db_session: Session):
    publication_year = 1997
    with TestClient(app) as client:
        response = client.get(f"/books/?publication_year={publication_year}")
    assert response.status_code == 200
    for book in response.json():
        assert book["publication_year"] == publication_year

def test_get_books_by_author_and_publication_year(db_session: Session):
    author = "J.K. Rowling"
    publication_year = 1997
    with TestClient(app) as client:
        response = client.get(f"/books/?author={author}&publication_year={publication_year}")
    assert response.status_code == 200
    for book in response.json():
        assert book["author"] == author
        assert book["publication_year"] == publication_year

# Test cases for POST method in reviews API
def test_submit_review(db_session: Session):
    review_data = {"text": "This book is amazing!", "rating": 5, "book_id": 1}
    with TestClient(app) as client:
        response = client.post("/reviews/", json=review_data)  
    assert response.status_code == 200

# Test cases for GET method in reviews API
def test_get_reviews_for_book(db_session: Session):
    with TestClient(app) as client:
        response = client.get("/reviews/1")  
    assert response.status_code == 200
    assert len(response.json()) > 0

