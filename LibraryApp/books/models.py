from django.db import models
import uuid
from authors.models import Author


# Create your models here.
class Book(models.Model):
    book_id = models.UUIDField(
        "id", primary_key=True, default=uuid.uuid4, editable=False
    )
    book_name = models.CharField("name", max_length=128)
    # author_id = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL)
    copies_count = models.IntegerField("copies_count")

    def __str__(self):
        return self.book_name + " -> " + str(self.book_id)

    def isAvailable(self):
        return self.copies_count > 0


# class User(models.Model):
#     user_id=models.IntegerField("id",auto_created=True,primary_key=True)
#     user_name=models.CharField("name",max_length=150)
#     password=models.CharField("name",max_length=150)

# class Transaction(models.Model):
#     transaction_id=models.IntegerField("id",auto_created=True,primary_key=True)
#     user_id=models.IntegerField("id",auto_created=True,primary_key=True)
#     user_id=models.IntegerField("id",auto_created=True,primary_key=True)
#     user_name=models.CharField("name",max_length=150)
#     password=models.CharField("name",max_length=150)
