from fastapi import FastAPI

from src.api.routes.ping import ping_router

app = FastAPI()


def setup_app():
    app.include_router(ping_router)


setup_app()
