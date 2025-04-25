"""Data models for the API."""
from typing import List, Optional
from pydantic import BaseModel, Field


class DataItem(BaseModel):
    """A single data item with validation."""
    value: int = Field(..., description="The integer value to process")
    description: Optional[str] = Field(None, description="Optional description of the value")


class DataList(BaseModel):
    """A list of data items with validation."""
    items: List[DataItem] = Field(..., description="List of data items to process")
    name: Optional[str] = Field(None, description="Optional name for this data set")


class ProcessedResult(BaseModel):
    """Results from processing data."""
    average: float = Field(..., description="The calculated average")
    maximum: Optional[int] = Field(None, description="The maximum value if available")
    item_count: int = Field(..., description="Number of items processed")
