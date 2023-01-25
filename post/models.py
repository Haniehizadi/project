from django.db import models


# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_date = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return self.title

