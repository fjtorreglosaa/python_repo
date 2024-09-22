from fastapi import APIRouter

from routes.user.book_routes import BookRoutes

class AppRoutes:
    
    @staticmethod
    def routes() -> APIRouter:
        router = APIRouter()

        router.include_router(
            BookRoutes.routes(),
            prefix='/api/books',
            tags=['Books']
        )

        return router