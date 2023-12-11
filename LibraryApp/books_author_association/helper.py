from .models import BooksAuthorAssociation

def create_book_author_association(book,author):
    book_author_association=BooksAuthorAssociation(book=book,author=author)
    book_author_association.save()
    
    # update author's book count
    author.book_count+=1
    author.save()