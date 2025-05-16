from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class BenefitsTester(APITestCase):
    def setUp(self):
        self.list_url = reverse("tierbenefit-list")
        self.payload = {"benefit":"Free lounge access", "description":"+1 allowed", "miles_need":"200", 'discount_rate':"0.1",}

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
   