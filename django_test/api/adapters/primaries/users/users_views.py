from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
# from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import DjangoModelPermissions

from apps.backoffice.models import Administrator
from . import users_serializer
from compartidos.serializers import NotFoundSerializer

#Agregado Donovan
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from ....engine.use_cases.services.service_authentication import change_password_user, recovery_password_user
from .users_serializer import ChangePasswordSerializer  # asegúrate de importar bien el serializer
from django.contrib.auth.models import User
from .users_serializer import UserListSerializer
from django.core.exceptions import ValidationError


class UsersViewSet(viewsets.GenericViewSet, APIView):
    # queryset =
    serializer_class = users_serializer.InfoMeSerializer
    # permission_classes = [DjangoModelPermissions]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: users_serializer.InfoMeSerializer(),
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
        },
    )
    def info_me(self, request) -> Response:
        """Get user info"""
        user = request.user

        user_info = {
            "name": user.name,
            "username": user.username,
            "email": user.email,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
            "tools": [],
        }

        serializer = self.serializer_class(data=user_info)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ChangePasswordSerializer,
        responses={
            status.HTTP_200_OK: "Contraseña cambiada correctamente.",
            status.HTTP_400_BAD_REQUEST: "Datos inválidos.",
        },
    )
    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        """Cambia la contraseña del usuario autenticado"""
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            change_password_user(
                user=request.user,
                old_password=serializer.validated_data["old_password"],
                new_password=serializer.validated_data["new_password"],
            )
            return Response({"detail": "Contraseña cambiada correctamente."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list_users(self, request):
        users = Administrator.objects.all()
        serializer = users_serializer.InfoMeSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def recovery_password(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        new_password = request.data.get("new_password")

        if not email or not new_password:
            return Response({"error": "Faltan campos obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            recovery_password_user(username, email, new_password)
        except ValidationError as e:
            return Response({"error": e.message_dict}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Contraseña actualizada exitosamente"}, status=status.HTTP_200_OK)