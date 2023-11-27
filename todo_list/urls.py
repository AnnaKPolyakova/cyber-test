from django.urls import include, path

from todo_list.views import RegistrationAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

registration_patterns = [
    path(
        "registration/",
        RegistrationAPIView.as_view(),
        name="registration"
    ),
]

token_patterns = [
    path("token/create/", TokenObtainPairView.as_view(), name="token_create"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

user_urls = [
    path("users/", include(registration_patterns)),
    path("users/", include(token_patterns)),
]

urlpatterns = [
    path("v1/", include(user_urls)),
]