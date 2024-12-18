from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
