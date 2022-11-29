# engine
from api.adapters.secondaries.factory import constructor_customers as customers_repo
from api.engine.use_cases import factory as customers_engine
from api.engine.domain.exceptions import exceptions_customers as exceptions

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

# from rest_framework.serializers import Serializer
from . import customers_serializer
from compartidos.serializers import NotFoundSerializer
from apps.webApp.models import customers as customers_models

# engine implementation
customers_repository = customers_repo.constructor_customers(customers_models.Customer)
customers_engine = customers_engine.constructor_manager_customers(customers_repository)


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
        query_params = request.query_params
        query_params_serializer = customers_serializer.CustomerQueryParamsSerializer(
            data=query_params
        )
        query_params_serializer.is_valid(raise_exception=True)

        customer_id = query_params_serializer.validated_data.get("customer_id")

        if customer_id:
            try:
                customer = customers_engine.get_customer(customer_id=customer_id)
                customer = dict(
                    id=customer.id,
                    name=customer.name,
                    paternal_surname=customer.paternal_surname,
                    email=customer.email,
                )
            except Exception as e:
                print(f"'{e}' exception raised in {__name__} at line 45")
                return Response(
                    data=exceptions.CustomerDoesNotExist(customer_id).message,
                    status=status.HTTP_404_NOT_FOUND,
                )

            customer_serializer = customers_serializer.CustomersSerializer(
                data=customer
            )
            customer_serializer.is_valid(raise_exception=True)
            return Response(data=customer_serializer.data, status=status.HTTP_200_OK)

        customers = customers_engine.list_customers()

        customer_serializer = customers_serializer.CustomersSerializer(
            data=customers, many=True
        )
        customer_serializer.is_valid(raise_exception=False)
        # TODO: Check validation on serializer

        page = self.paginate_queryset(customers)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(data=customer_serializer.data, status=status.HTTP_200_OK)
