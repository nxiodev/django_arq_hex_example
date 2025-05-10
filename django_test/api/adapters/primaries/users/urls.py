from django.urls import path
from .users_views import UsersViewSet

info_me = {"get": "info_me"}

urlpatterns = [
    path(
        "users/me", UsersViewSet.as_view({**info_me
                                          }
                                         ),
        name="crud-users"
    ),
]
