from rest_framework import serializers
# Agregado donovan
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from apps.backoffice.models import Administrator


class InfoMeSerializer(serializers.Serializer):
    """Serializer for Customers"""

    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    is_active = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    tools = serializers.ListField(
        child=serializers.DictField(),
        allow_null=True
    )


class CustomerQueryParamsSerializer(serializers.Serializer):
    """Serializer for CustomerQueryParams"""
    customer_id = serializers.IntegerField(required=False)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=False)
    new_password = serializers.CharField(required=True, validators=[validate_password])


class UserListSerializer(serializers.ModelSerializer):
    queryset = Administrator.objects.all()

    # serializer_class = users_serializer.InfoMeSerializer
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'is_staff']
