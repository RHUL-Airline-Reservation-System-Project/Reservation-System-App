from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class CheckInTester(APITestCase):
    def setUp(self):
        self.list_url = reverse("checkin-list")
        self.payload = {"booking_reference":"ABC123", "passenger_name":"Name Lastname", "seat":"12A", "extras":"None"}
    
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