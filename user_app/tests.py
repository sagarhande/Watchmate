from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):

        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "password": "sample@123",
            "password2": "sample@123",
            }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="testcase", password="test@1234")

    def test_login(self):
        data = {
            "username": "testcase",
            "password": "test@1234",
            }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username='testcase')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


