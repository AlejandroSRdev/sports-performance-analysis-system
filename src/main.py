from fastapi import FastAPI

from src.presentation.routes import health
from src.presentation.routes import player_context_routes

app = FastAPI(
    title="Sports Performance Analysis System",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(player_context_routes.router)
