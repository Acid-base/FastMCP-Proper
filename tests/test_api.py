"""Tests for the FastAPI implementation."""
from fastapi.testclient import TestClient
import pytest

from my_package.api import app
from my_package.models import DataItem, DataList, ProcessedResult

client = TestClient(app)


def test_read_root() -> None:
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "version" in data
    assert "documentation" in data


def test_process_valid_data() -> None:
    """Test processing valid data through the API."""
    test_data = DataList(
        items=[
            DataItem(value=1, description="first"),
            DataItem(value=2, description="second"),
            DataItem(value=3, description="third"),
        ],
        name="test_set"
    )

    response = client.post("/process", json=test_data.model_dump())
    assert response.status_code == 200

    result = ProcessedResult(**response.json())
    assert result.average == 2.0
    assert result.maximum == 3
    assert result.item_count == 3


def test_process_empty_data() -> None:
    """Test processing empty data list."""
    test_data = DataList(items=[], name="empty_set")
    response = client.post("/process", json=test_data.model_dump())
    assert response.status_code == 400
    assert "empty" in response.json()["detail"].lower()


def test_process_invalid_data() -> None:
    """Test processing invalid data types."""
    # Invalid data type for value
    invalid_data = {
        "items": [{"value": "not_a_number", "description": "invalid"}],
        "name": "invalid_set"
    }
    response = client.post("/process", json=invalid_data)
    assert response.status_code == 422  # Pydantic validation error
