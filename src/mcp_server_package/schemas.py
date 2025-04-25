# src/mcp_server_package/schemas.py
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# Keep Pydantic for defining complex tool arguments or return types if needed.
# Remove the old API-specific models (DataItem, DataList, ProcessedResult).

class CalculatorResult(BaseModel):
    """Example schema for a structured return value from a tool."""
    operation: str
    result: float | str # Can be float or error string

class SystemInfo(BaseModel):
    """Example schema for a system info tool return."""
    os: str
    cpu_percent: float
    memory_percent: float

# Add other schemas relevant to your MCP tools here
