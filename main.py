from src.core.settings import settings

try:
    import uvicorn
except ImportError:
    import sys

    sys.exit('INSTALL PYTHON DEPENDENCIES...')

from fastapi import FastAPI

app = FastAPI(
    title=settings.project_name,
    description=settings.description,
    version=settings.version,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
