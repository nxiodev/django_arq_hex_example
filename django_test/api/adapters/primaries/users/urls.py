from django.urls import path
from .users_views import UsersViewSet

info_me = {"get": "info_me"}

change_password = {"post": "change_password"}


urlpatterns = [
    path(
        "users/me", UsersViewSet.as_view({**info_me
                                          }
                                         ),
        name="crud-users"
    ),
    path(
        "users/change-password", UsersViewSet.as_view(change_password),
        name="change-password"
    ),
]
