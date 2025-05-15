from django.urls import path
from .users_views import UsersViewSet

info_me = {"get": "info_me"}

change_password = {"post": "change_password"}

crud_users = {"get": "list_users"}

recovery_password = {"post" : "recovery_password"}

urlpatterns = [
    path(
        "users/me", UsersViewSet.as_view({**info_me
                                          }
                                         ),
        name="crud-users"
    ),
    path(
        "users/change-password", UsersViewSet.as_view({**change_password
                                                       }
                                                      ),
        name="change-password"
    ),
    path("users/", UsersViewSet.as_view({**crud_users
                                         }
                                        ),
         name="crud-users"),
    path('recovery-password/', UsersViewSet.as_view({**recovery_password
                                                     }
                                                    ),
         name='recovery-password'),

]
