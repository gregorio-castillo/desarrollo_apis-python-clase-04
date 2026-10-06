from fastapi import FastAPI

from app.config import settings
from app.routers import projects


app = FastAPI(
    title = settings.app_name,
)

app.include_router(
    projects.router,
)

@app.get("/health")
def read_health():
    return {"status": "ok"}



