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

    def test_list_customers(self):
        url = reverse("crud-customers")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_customers(self):
        url = reverse("crud-customers")
        payload = {
            "name": "string",
            "paternal_surname": "string",
            "email": "string9"
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_customers(self):
        url_query_params = "%s?customer_id=%s" % (reverse("crud-customers"), CUSTOMER_ID)
        response = self.client.get(url_query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_customers(self):
        url_query_params = "%s?customer_id=%s" % (reverse("crud-customers"), CUSTOMER_ID)
        payload = {
            "name": "string",
            "paternal_surname": "string",
            "email": "string9"
        }
        response = self.client.put(url_query_params, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_customers(self):
        url_query_params = "%s?customer_id=%s" % (reverse("crud-customers"), CUSTOMER_ID)
        response = self.client.delete(url_query_params)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
