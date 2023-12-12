from django.db import models
import uuid
from books.models import Book


# Create your models here.
class Author(models.Model):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("name", max_length=128)
    book_count = models.IntegerField("book_count", default=0)
    books_authored = models.ManyToManyField(Book, related_name="authors")

    def __str__(self):
        return self.name + " " + str(self.id) + " " + str(self.book_count)
