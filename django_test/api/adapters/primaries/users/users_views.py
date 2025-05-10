from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
# from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import DjangoModelPermissions

from . import users_serializer
from compartidos.serializers import NotFoundSerializer


class UsersViewSet(viewsets.GenericViewSet):
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
