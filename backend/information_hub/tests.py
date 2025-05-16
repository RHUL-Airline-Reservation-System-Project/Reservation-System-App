from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class InformationHubTester(APITestCase):
    def setUp(self):
        self.list_url = reverse("informationhub-list")

    def test_endpoint(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)


#https://www.django-rest-framework.org/api-guide/testing/#apitestcase
#https://docs.djangoproject.com/en/5.2/topics/http/urls/#reverse
#https://www.django-rest-framework.org/api-guide/status-codes
#https://docs.python.org/3/library/unittest.html#unittest.TestCase
