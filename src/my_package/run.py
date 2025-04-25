"""Script to run the FastAPI server."""
import uvicorn

def main() -> None:
    """Run the FastAPI application using uvicorn."""
    uvicorn.run(
        "my_package.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload during development
    )

if __name__ == "__main__":
    main()
