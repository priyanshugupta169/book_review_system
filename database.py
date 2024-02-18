from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the URL for your production database
SQLALCHEMY_DATABASE_URL = "sqlite:///./book_review.db"

# Define the URL for your test database
TEST_DATABASE_URL = "sqlite:///./test_book_review.db"

# Create an engine for the production database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Create a SessionLocal class for the production database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create an engine for the test database
test_engine = create_engine(TEST_DATABASE_URL)
# Create a SessionLocal class for the test database
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# Create a base class for your models
Base = declarative_base()


def get_db():
    # Dependency to get database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


