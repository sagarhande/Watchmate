from django.db import models


# Create your models here.
class StreamPlatform(models.Model):
    """Model for a streaming platform"""
    name = models.CharField(max_length=30)
    about = models.TextField()
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    """Model for entity such as Movie, Podcast, Webseries etc """
    title = models.CharField(max_length=50)
    storyline = models.TextField()
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




