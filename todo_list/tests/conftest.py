import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

ERROR_INFO = "Error for method: {method}, url: {url}, status: {status}"


DOC_REDOC_URL = reverse("redoc")
DOC_SWAGGER_URL = reverse("swagger-ui")
TOKEN_URL = reverse("token_create")
REFRESH_TOKEN_URL = reverse("token_refresh")

EMAIL = "Test"
PASSWORD = "Test"

User = get_user_model()


@pytest.fixture
def guest_client():
    client = APIClient()
    return client


@pytest.fixture
def user():
    user = User(username=EMAIL, email=EMAIL)
    user.set_password(PASSWORD)
    user.save()
    return user
