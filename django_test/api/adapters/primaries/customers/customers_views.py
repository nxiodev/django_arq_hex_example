from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from . import customers_serializer
from compartidos.serializers import NotFoundSerializer


class CustomersViewSet(viewsets.GenericViewSet):
    """
    Customer's CRUD ViewSet
    """
    serializer_class = customers_serializer.CustomersSerializer

    @swagger_auto_schema(
        query_serializer=customers_serializer.CustomerQueryParamsSerializer(),
        responses={
            status.HTTP_200_OK: customers_serializer.CustomersSerializer(),
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
        },
    )
    def list_customers(self, request) -> Response:
        customers = [
            {
                "id": 1,
                "name": "string",
                "paternal_surname": "string",
                "email": "string",
            },
            {
                "id": 2,
                "name": "string",
                "paternal_surname": "string",
                "email": "string",
            },
            {
                "id": 3,
                "name": "string",
                "paternal_surname": "string",
                "email": "string",
            },
        ]

        customer_serializer = customers_serializer.CustomersSerializer(
            data=customers, many=True
        )
        customer_serializer.is_valid(raise_exception=True)

        page = self.paginate_queryset(customers)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(data=customer_serializer.data, status=status.HTTP_200_OK)
