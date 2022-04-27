from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class StreamPlatform(models.Model):
    """Model for a streaming platform"""
    name = models.CharField(max_length=30)
    about = models.TextField()
    website = models.URLField(max_length=100)
    # total_shows = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class WatchList(models.Model):
    """Model for entity such as Movie, Podcast, Webseries etc """
    title = models.CharField(max_length=50)
    storyline = models.TextField()
    hashtag = models.CharField(max_length=100)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    avg_rating = models.FloatField(default=0)
    number_rating = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """Model for watchlist review"""
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField()
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + "  |  " + self.watchlist.title


