from django.db import models
import uuid


# Create your models here.
class Book(models.Model):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("name", max_length=128)
    count = models.IntegerField("count", default=1)

    def __str__(self):
        return self.name + " -> " + str(self.id)

    def isAvailable(self):
        return self.count > 0
