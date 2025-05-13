from rest_framework.test import APITestCase
from rest_framework import status

class TicketingTests(APITestCase):
    def test_get_ticketing_list(self):
        response = self.client.get('/api/ticketing/ticketing/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
