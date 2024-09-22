from fastapi import FastAPI

from routes.app_routes import AppRoutes

app = FastAPI()

app.include_router(AppRoutes.routes())