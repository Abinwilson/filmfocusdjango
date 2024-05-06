from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    about = models.TextField()
    cover = models.ImageField(upload_to="media/cover", null=True, blank=True)

    def __str__(self):
        return self.title
