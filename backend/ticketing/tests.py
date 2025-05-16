# from rest_framework.test import APITestCase
# from rest_framework import status

# class TicketingTests(APITestCase):
#     def test_get_ticketing_list(self):
#         response = self.client.get('/api/ticketing/ticketing/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

###The code above was deemed not necessary###
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import FlightTracker

class TicketingTester(APITestCase):
    def setUp(self):
        self.flight = FlightTracker.objects.create(flight_number="XY200",flight_status="On Time",departure_time="2025-05-01T05:30:00", arrival_time="2025-05-01T09:45:00", departure_location= "HND", destination="LHR")
            
        self.list_url = reverse("ticketing-list")
        self.payload = {"flight_number":self.flight.pk, "class_type":"ECONOMY","price":50.00, "discount_code":"NONE","is_available":"True"}

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
