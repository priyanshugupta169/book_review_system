# FastAPI Book Review System

This project implements a RESTful API using FastAPI for a hypothetical book review system.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/priyanshugupta169/book_review_system
   cd book_review_system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Features

1. **Endpoints:**
   - Add a new book (title, author, publication year).
   - Submit a review for a book (text review, rating).
   - Retrieve all books with an option to filter by author or publication year.
   - Retrieve all reviews for a specific book.

2. **Data Validation:**
   - Data validation is implemented using Pydantic models.

3. **Documentation:**
   - Comments have been added to the code for better understanding.

4. **Error Handling:**
   - Proper error handling is implemented for invalid requests.

## Usage

1. **Run the FastAPI application:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation:**
   Open your web browser and navigate to `http://localhost:8000/docs` to access the Swagger UI documentation.

3. **Use the provided endpoints to interact with the API.**

## Database Integration

This project currently uses SQLite as the database backend. The database integration and schema design are implemented in the `database.py`, `models.py`, and `schemas.py` files.

## Testing

1. **Testing:**
   - Tests for the API endpoints can be written using FastAPI's test client.

## Contributors

- [Priyanshu Gupta](https://github.com/priyanshugupta169)

## License

This project is licensed under the [MIT License](LICENSE).
