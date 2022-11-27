from django.urls import path
from .customers_views import CustomersViewSet

list_customers = {"get": "list_customers"}

urlpatterns = [
    path(
        "customers", CustomersViewSet.as_view({**list_customers}), name="crud-customers"
    ),
]
