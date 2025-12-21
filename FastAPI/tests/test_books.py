import pytest
from fastapi.testclient import TestClient
from src import app
from src.books.books_data import books


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def initial_books_count():
    """Store the initial count of books before tests."""
    return len(books)


@pytest.fixture(autouse=True)
def reset_books():
    """Reset books data after each test to maintain test isolation."""
    original_books = books.copy()
    yield
    books.clear()
    books.extend(original_books)


class TestGetAllBooks:
    """Test cases for GET /api/v1/books endpoint."""

    def test_get_all_books_returns_200(self, client):
        """Test that GET /api/v1/books returns 200 status code."""
        response = client.get("/api/v1/books/")
        assert response.status_code == 200

    def test_get_all_books_returns_list(self, client):
        """Test that GET /api/v1/books returns a list of books."""
        response = client.get("/api/v1/books/")
        assert isinstance(response.json(), list)

    def test_get_all_books_returns_all_books(self, client, initial_books_count):
        """Test that GET /api/v1/books returns all books."""
        response = client.get("/api/v1/books/")
        data = response.json()
        assert len(data) == initial_books_count

    def test_get_all_books_has_correct_structure(self, client):
        """Test that each book has the expected fields."""
        response = client.get("/api/v1/books/")
        data = response.json()
        
        if data:
            first_book = data[0]
            expected_fields = ["id", "title", "author", "publisher", "published_date", "page_count", "language"]
            for field in expected_fields:
                assert field in first_book


class TestGetBookById:
    """Test cases for GET /api/v1/books/{book_id} endpoint when book exists."""

    def test_get_book_by_id_returns_200(self, client):
        """Test that GET /api/v1/books/{book_id} returns 200 when book is found."""
        response = client.get("/api/v1/books/1")
        assert response.status_code == 200

    def test_get_book_by_id_returns_specific_book(self, client):
        """Test that GET /api/v1/books/{book_id} returns the correct book."""
        book_id = 1
        response = client.get(f"/api/v1/books/{book_id}")
        data = response.json()
        
        assert data["id"] == book_id
        assert "title" in data
        assert "author" in data

    def test_get_book_by_id_returns_correct_data(self, client):
        """Test that the returned book data matches the expected data."""
        response = client.get("/api/v1/books/1")
        data = response.json()
        
        # Verify against known book data
        assert data["id"] == 1
        assert data["title"] == "Think Python"
        assert data["author"] == "Allen B Downey"
        assert data["publisher"] == "O'Reilly Media"


class TestGetBookByIdNotFound:
    """Test cases for GET /api/v1/books/{book_id} endpoint when book doesn't exist."""

    def test_get_nonexistent_book_returns_404(self, client):
        """Test that GET /api/v1/books/{book_id} returns 404 when book is not found."""
        response = client.get("/api/v1/books/9999")
        assert response.status_code == 404

    def test_get_nonexistent_book_returns_error_detail(self, client):
        """Test that 404 response includes error details."""
        response = client.get("/api/v1/books/9999")
        data = response.json()
        
        assert "detail" in data
        assert data["detail"] == "Book Not Found!"

    def test_get_book_with_negative_id_returns_404(self, client):
        """Test that GET with negative ID returns 404."""
        response = client.get("/api/v1/books/-1")
        assert response.status_code == 404


class TestCreateBook:
    """Test cases for POST /api/v1/books endpoint."""

    def test_create_book_returns_201(self, client):
        """Test that POST /api/v1/books successfully creates a new book and returns 201 status."""
        new_book = {
            "id": 999,
            "title": "Test Book",
            "author": "Test Author",
            "publisher": "Test Publisher",
            "published_date": "2024-01-01",
            "page_count": 300,
            "language": "English"
        }
        
        response = client.post("/api/v1/books/", json=new_book)
        assert response.status_code == 201

    def test_create_book_returns_created_book(self, client):
        """Test that POST /api/v1/books returns the created book data."""
        new_book = {
            "id": 999,
            "title": "Test Book",
            "author": "Test Author",
            "publisher": "Test Publisher",
            "published_date": "2024-01-01",
            "page_count": 300,
            "language": "English"
        }
        
        response = client.post("/api/v1/books/", json=new_book)
        data = response.json()
        
        assert data["id"] == new_book["id"]
        assert data["title"] == new_book["title"]
        assert data["author"] == new_book["author"]
        assert data["publisher"] == new_book["publisher"]

    def test_create_book_adds_to_collection(self, client, initial_books_count):
        """Test that POST /api/v1/books actually adds the book to the collection."""
        new_book = {
            "id": 999,
            "title": "Test Book",
            "author": "Test Author",
            "publisher": "Test Publisher",
            "published_date": "2024-01-01",
            "page_count": 300,
            "language": "English"
        }
        
        client.post("/api/v1/books/", json=new_book)
        
        # Verify book was added by fetching all books
        response = client.get("/api/v1/books/")
        data = response.json()
        assert len(data) == initial_books_count + 1

    def test_create_book_can_be_retrieved(self, client):
        """Test that a newly created book can be retrieved by ID."""
        new_book = {
            "id": 999,
            "title": "Test Book",
            "author": "Test Author",
            "publisher": "Test Publisher",
            "published_date": "2024-01-01",
            "page_count": 300,
            "language": "English"
        }
        
        client.post("/api/v1/books/", json=new_book)
        
        # Try to retrieve the newly created book
        response = client.get("/api/v1/books/999")
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Test Book"


class TestUpdateBook:
    """Test cases for PATCH /api/v1/books/{book_id} endpoint."""

    def test_update_book_returns_200(self, client):
        """Test that PATCH /api/v1/books/{book_id} successfully updates an existing book and returns 200 status."""
        update_data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "publisher": "Updated Publisher",
            "page_count": 500,
            "language": "Spanish"
        }
        
        response = client.patch("/api/v1/books/1", json=update_data)
        assert response.status_code == 200

    def test_update_book_returns_updated_data(self, client):
        """Test that PATCH /api/v1/books/{book_id} returns the updated book data."""
        update_data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "publisher": "Updated Publisher",
            "page_count": 500,
            "language": "Spanish"
        }
        
        response = client.patch("/api/v1/books/1", json=update_data)
        data = response.json()
        
        assert data["title"] == update_data["title"]
        assert data["author"] == update_data["author"]
        assert data["publisher"] == update_data["publisher"]
        assert data["page_count"] == update_data["page_count"]
        assert data["language"] == update_data["language"]

    def test_update_book_persists_changes(self, client):
        """Test that PATCH /api/v1/books/{book_id} persists the changes."""
        update_data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "publisher": "Updated Publisher",
            "page_count": 500,
            "language": "Spanish"
        }
        
        client.patch("/api/v1/books/1", json=update_data)
        
        # Retrieve the book to verify changes persisted
        response = client.get("/api/v1/books/1")
        data = response.json()
        
        assert data["title"] == "Updated Title"
        assert data["author"] == "Updated Author"

    def test_update_nonexistent_book_returns_404(self, client):
        """Test that PATCH /api/v1/books/{book_id} returns 404 when book doesn't exist."""
        update_data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "publisher": "Updated Publisher",
            "page_count": 500,
            "language": "Spanish"
        }
        
        response = client.patch("/api/v1/books/9999", json=update_data)
        assert response.status_code == 404

    def test_update_book_preserves_id(self, client):
        """Test that updating a book doesn't change its ID."""
        update_data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "publisher": "Updated Publisher",
            "page_count": 500,
            "language": "Spanish"
        }
        
        response = client.patch("/api/v1/books/1", json=update_data)
        data = response.json()
        
        # ID should remain unchanged
        assert data["id"] == 1
