from .models import Author


def get_author_by_id(author_id):
    return Author.objects.get(id=author_id)


def books_authored(author_id):
    return Author.objects.get(id=author_id).books_authored
