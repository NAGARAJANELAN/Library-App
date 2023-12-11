from django.db import models
import uuid

# Create your models here.
class Author(models.Model):
    author_id=models.UUIDField(
        "id", primary_key=True, default=uuid.uuid4, editable=False
    )
    author_name=models.CharField("name",max_length=128)
    book_count=models.IntegerField("book_count",default=0)
    
    def __str__(self):
        return self.author_name+' '+str(self.author_id)