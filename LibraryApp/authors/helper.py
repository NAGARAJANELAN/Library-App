from .models import Author

def get_author_by_id(author_id):
    return Author.objects.get(author_id=author_id)