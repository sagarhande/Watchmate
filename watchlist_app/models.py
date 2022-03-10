from django.db import models

# Create your models here.


class Movie(models.Model):
    """Model for Movies entity"""
    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        """Return name of movie"""
        return self.name


