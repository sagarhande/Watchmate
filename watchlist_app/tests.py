from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="testcase", password="test@1234", )
        self.token = Token.objects.get(user__username='testcase')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # create a stream platform
        self.stream = models.StreamPlatform.objects.create(name="Amazon Prime Video",
                                                           about="a streaming platform by Amazon",
                                                           website="https://primevideo.com/")
        self.stream.save()

    def test_streamplatform_create(self):
        data = {"name": "Netflix", "about": "A streaming platform", "website": "https://netflix.com"
                }
        response = self.client.post(reverse('platform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('platform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_item(self):
        response = self.client.get(reverse('platform-details', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_update(self):
        data = {"name": "Prime Video",
                "about": "A streaming platform by Amazon. Has thousands of series, podcasts, movies and many more!",
                "website": "https://primevideo.com"
                }
        response = self.client.put(reverse('platform-details', args=(self.stream.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_delete(self):
        response = self.client.delete(reverse('platform-details', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix", about="Streaming Platform",
                                                           website="https://www.netflix.com")
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                         storyline="Example Movie", active=True)

    def test_watchlist_create(self):
        data = {"platform": self.stream, "title": "Example Movie", "storyline": "Example Story", "active": True
                }
        response = self.client.post(reverse('show-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('show-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_item(self):
        response = self.client.get(reverse('show-details', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')


class ReviewTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix", about="Streaming Platform",
                                                           website="https://www.netflix.com")

        self.watchlist1 = models.WatchList.objects.create(platform=self.stream, title="Example Movie1",
                                                          storyline="Example Movie1", active=True)

        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, title="Example Movie2",
                                                          storyline="Example Movie2", active=True)

        self.review = models.Review.objects.create(review_user=self.user, rating=4.5,
                                                   description="Test-review description", watchlist=self.watchlist2,
                                                   active=True)

    def test_review_create(self):
        data1 = {"review_user": self.user, "rating": 4.5, "description": "sample description",
                 "watchlist": self.watchlist1, "active": True
                 }
        data2 = {"review_user": self.user, "rating": 6, "description": "sample description",
                 "watchlist": self.watchlist2, "active": True
                 }
        data3 = {"review_user": self.user, "rating": -1, "description": "sample description",
                 "watchlist": self.watchlist2, "active": True
                 }
        response = self.client.post(reverse('create-show-reviews', args=(self.watchlist1.id,)), data1, )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # User can't give multiple reviews
        response = self.client.post(reverse('create-show-reviews', args=(self.watchlist1.id,)), data1, )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Wrong ratings
        response = self.client.post(reverse('create-show-reviews', args=(self.watchlist2.id,)), data2, )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.post(reverse('create-show-reviews', args=(self.watchlist2.id,)), data3, )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unautherised(self):
        data = {"review_user": self.user, "rating": 5, "description": "Great Movie!", "watchlist": self.watchlist2,
                "active": True
                }

        self.client.force_authenticate(user=None)  # Not logged in
        response = self.client.post(reverse('create-show-reviews', args=(self.watchlist2.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {"review_user": self.user, "rating": 5, "description": "Great Movie!-updated description",
                "watchlist": self.watchlist2, "active": False
                }
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data, )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_review_list(self):
        response = self.client.get(reverse('user-review-list') )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_delete(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


