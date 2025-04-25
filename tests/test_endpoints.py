"""Tests for API endpoints using httpx."""
import pytest
from fastapi.testclient import TestClient

from my_package.api import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client."""
    return TestClient(app)


def test_root_endpoint(client: TestClient) -> None:
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert data["title"] == "Data Processing API"
    assert "version" in data
    assert "documentation" in data


def test_process_data_valid(client: TestClient) -> None:
    """Test processing valid data."""
    test_data = {
        "items": [
            {"value": 1, "description": "first"},
            {"value": 2, "description": "second"},
            {"value": 3, "description": "third"}
        ],
        "name": "test_batch"
    }

    response = client.post("/process", json=test_data)
    assert response.status_code == 200

    result = response.json()
    assert result["average"] == 2.0
    assert result["maximum"] == 3
    assert result["item_count"] == 3


def test_process_data_empty(client: TestClient) -> None:
    """Test processing empty data list."""
    test_data = {
        "items": [],
        "name": "empty_batch"
    }

    response = client.post("/process", json=test_data)
    assert response.status_code == 400
    assert "empty" in response.json()["detail"].lower()


def test_process_data_invalid_type(client: TestClient) -> None:
    """Test processing data with invalid types."""
    test_data = {
        "items": [
            {"value": "not_a_number", "description": "invalid"}
        ],
        "name": "invalid_batch"
    }

    response = client.post("/process", json=test_data)
    assert response.status_code == 422  # Pydantic validation error


def test_process_data_missing_value(client: TestClient) -> None:
    """Test processing data with missing required field."""
    test_data = {
        "items": [
            {"description": "missing_value"}  # missing 'value' field
        ],
        "name": "invalid_batch"
    }

    response = client.post("/process", json=test_data)
    assert response.status_code == 422  # Pydantic validation error


def test_process_data_large_numbers(client: TestClient) -> None:
    """Test processing large numbers."""
    test_data = {
        "items": [
            {"value": 1000000, "description": "large"},
            {"value": 2000000, "description": "larger"},
            {"value": 3000000, "description": "largest"}
        ],
        "name": "large_numbers"
    }

    response = client.post("/process", json=test_data)
    assert response.status_code == 200

    result = response.json()
    assert result["average"] == 2000000.0
    assert result["maximum"] == 3000000
    assert result["item_count"] == 3
