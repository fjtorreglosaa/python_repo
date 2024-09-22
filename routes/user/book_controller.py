from utilites.book.create_book_dto import CreateBookDto
from utilites.book.get_book_dto import GetBookDto

class BookController:

    def create_book(self, criteria: CreateBookDto) -> GetBookDto:
        return "The book has been created"

def get_book_controller():
    return BookController()