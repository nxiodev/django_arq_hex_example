from abc import ABC
from rest_framework import serializers


class CustomersSerializer(serializers.Serializer):
    """Serializer for Customers"""

    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    paternal_surname = serializers.CharField()
    email = serializers.CharField()


class CustomerQueryParamsSerializer(serializers.Serializer):
    """Serializer for CustomerQueryParams"""

    customer_id = serializers.IntegerField(required=False)


class AlarmSerializer(serializers.Serializer):
    """Serializer for Alarms"""

    id = serializers.IntegerField(required=False)
    product_id = serializers.CharField(required=False)
    alert_type = serializers.CharField(required=False)
    alert_date = serializers.DateField(required=False)
    is_active = serializers.BooleanField(required=False)


class ProductSerializer(serializers.Serializer):
    """Serializer for Products"""

    id = serializers.IntegerField(required=False)
    product_name = serializers.CharField()
    description = serializers.CharField()
    stock = serializers.IntegerField()
    expiry_date = serializers.DateTimeField()
    alarms = AlarmSerializer(required=False, many=True, allow_null=True)


class ProductQueryParamsSerializer(serializers.Serializer):
    """Serializer for ProductsQueryParams"""

    from_date = serializers.CharField(required=False)
    to_date = serializers.CharField(required=False)


class AlarmQueryParamsSerializer(serializers.Serializer):
    """Serializer for AlarmsQueryParams"""

    is_active = serializers.BooleanField(required=False)