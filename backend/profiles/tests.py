from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import profile_create_or_update
from django.db.models.signals import post_save

post_save.disconnect(profile_create_or_update, sender=User)

class ProfilesTester(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="caroline", password="pass")
        self.list_url = reverse("profiles-list")
        self.payload = {"user":self.user.id, "miles_balance":1000, "membership":"Gold"}
    
    def test_endpoint(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create(self):
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
#https://www.django-rest-framework.org/api-guide/testing/#apitestcase
#https://docs.djangoproject.com/en/5.2/topics/http/urls/#reverse
#https://www.django-rest-framework.org/api-guide/status-codes
#https://docs.python.org/3/library/unittest.html#unittest.TestCase