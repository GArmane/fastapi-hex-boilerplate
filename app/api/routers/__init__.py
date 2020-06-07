from fastapi.applications import FastAPI

from app.api.routers import root


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(root.router)
    return app
