from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class InfoMeSerializer(serializers.Serializer):
    """Serializer for Customers"""

    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    is_active = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    tools = serializers.ListField(
        child=serializers.DictField()
    )


class CustomerQueryParamsSerializer(serializers.Serializer):
    """Serializer for CustomerQueryParams"""

    customer_id = serializers.IntegerField(required=False)



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
