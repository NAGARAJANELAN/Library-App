from .models import Book


def get_book_authors(book_id):
    return Book.objects.get(id=book_id).authors.all()
