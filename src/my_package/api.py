"""FastAPI server implementation."""
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import DataList, ProcessedResult
from .module import DataProcessor

app = FastAPI(
    title="Data Processing API",
    description="A reference implementation of FastAPI with Pydantic models",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/process", response_model=ProcessedResult)
async def process_data(data: DataList) -> ProcessedResult:
    """Process a list of data items."""
    if not data.items:
        raise HTTPException(status_code=400, detail="Data list cannot be empty")

    # Extract values from DataItems
    values = [item.value for item in data.items]

    try:
        processor = DataProcessor(values)
        return ProcessedResult(
            average=processor.calculate_average(),
            maximum=processor.find_max(),
            item_count=len(values)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
async def read_root() -> Dict[str, Any]:
    """Root endpoint returning API information."""
    return {
        "title": "Data Processing API",
        "version": "1.0.0",
        "documentation": "/docs"
    }
