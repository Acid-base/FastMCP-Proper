# src/mcp_server_package/config.py
import logging
from typing import Literal, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Define log level choices for validation
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

class ServerSettings(BaseSettings):
    """
    Application configuration settings.

    Reads settings from environment variables or a .env file.
    """
    # Example: Optional setting with a default
    log_level: LogLevel = Field(default="INFO", description="Logging level for the server")

    # Example: Optional setting needed by a hypothetical tool
    # If a tool absolutely needs this to function, the tool's logic
    # should check for its presence after config loading.
    # We don't mark it 'required' here to allow the server itself to start.
    example_api_key: Optional[str] = Field(default=None, description="Optional API key for an example tool")

    # Add other required or optional settings here as needed
    # e.g., database_url: str = Field(..., description="REQUIRED: Database connection URL")

    model_config = SettingsConfigDict(
        # Load .env file if present (requires python-dotenv installed)
        env_file='.env',
        env_file_encoding='utf-8',
        # Allow reading variables case-insensitively
        case_sensitive=False,
        # Optional: Prefix environment variables, e.g., MCP_SERVER_LOG_LEVEL
        # env_prefix='MCP_SERVER_'
    )

# Load settings globally on import
try:
    settings = ServerSettings()
    # You can configure logging here based on settings.log_level
    logging.basicConfig(level=settings.log_level)
    logging.info(f"Configuration loaded successfully. Log level: {settings.log_level}")
    if settings.example_api_key:
        logging.debug("Example API Key is set.") # Avoid logging the key itself
    else:
        logging.warning("EXAMPLE_API_KEY is not set. Related tool functionality may be limited.")

except Exception as e: # Catch broader exceptions during initial load if needed
    # Handle critical configuration errors - e.g., if a *truly* required field failed
    # For the starter, we default to optional or INFO level to ensure server starts
    logging.error(f"CRITICAL ERROR loading configuration: {e}", exc_info=True)
    # Depending on severity, you might want to sys.exit(1) here
    # For this starter, we try to load defaults and proceed
    settings = ServerSettings() # Attempt load with defaults
    logging.warning("Falling back to default settings due to loading error.")
