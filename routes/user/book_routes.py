from fastapi import APIRouter, Depends

from routes.user.book_controller import BookController, get_book_controller
from utilites.book.create_book_dto import CreateBookDto

class BookRoutes:

    @staticmethod
    def routes() -> APIRouter:
        router = APIRouter()

        @router.post('/create')
        def create_book(
            criteria: CreateBookDto,
            controller: BookController = Depends(get_book_controller)
            ):
            return controller.create_book(criteria)

        return router