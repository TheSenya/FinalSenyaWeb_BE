from fastapi import FastAPI
from app.core.config import get_settings

# Entrypoint of the application, this is where everything starts

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    debug=settings.DEBUG,
    env=settings.ENV,
)


@app.get("/health")
def health():
    return {"status": "ok"}
