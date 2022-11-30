from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

CUSTOMER_ID = 1


class CustomersAPITest(TestCase):
    """API for testing customer's CRUD"""

    fixtures = [
        "fixtures/customers.json",
    ]

    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_payments(self):
        url = reverse("payments")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
