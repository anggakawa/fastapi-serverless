from fastapi import FastAPI
from runner.routes import invoke

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(invoke.router)
    return app
