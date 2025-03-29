from django.urls import path
from .customers_views import CustomersViewSet, AlarmViewSet

list_customers = {"get": "list_customers"}
create_customer = {"post": "create_customer"}
update_customer = {"put": "update_customer"}
delete_customer = {"delete": "delete_customer"}

list_alarms = {"get": "list_alarms"}

urlpatterns = [
    path(
        "customers", CustomersViewSet.as_view({**list_customers,
                                               **create_customer,
                                               **update_customer,
                                               **delete_customer
                                               }
                                              ),
        name="crud-customers"
    ),
    path(
        "alarms", AlarmViewSet.as_view(list_alarms), name="list-alarms"
    ),
]
