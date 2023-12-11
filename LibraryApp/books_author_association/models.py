from django.db import models

from books.models import Book
from authors.models import Author


# Create your models here.
class BooksAuthorAssociation(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book) + " -> " + str(self.author)