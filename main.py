import uvicorn
from src.config.settings import settings
from src.config.logging import configure_logging

if __name__ == "__main__":
    configure_logging()
    uvicorn.run(
        "src.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True,
    )
