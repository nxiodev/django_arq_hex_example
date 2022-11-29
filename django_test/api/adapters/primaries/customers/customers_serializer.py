from abc import ABC
from rest_framework import serializers


class CustomersSerializer(serializers.Serializer):
    """Serializer for Customers"""

    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    paternal_surname = serializers.CharField()
    email = serializers.CharField()


class PaymentsCustomersSerializer(serializers.Serializer):
    """Serializer for PaymentsCustomers"""

    id = serializers.IntegerField()
    customer = CustomersSerializer(read_only=True)
    product_name = serializers.CharField()
    amount = serializers.FloatField()
    quantity = serializers.IntegerField()
    created_at = serializers.DateField()
    updated_at = serializers.DateField()


class CustomerQueryParamsSerializer(serializers.Serializer):
    """Serializer for CustomerQueryParams"""

    customer_id = serializers.IntegerField(required=False)
