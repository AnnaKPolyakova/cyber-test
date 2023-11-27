import pytest
from django.urls import reverse
from rest_framework.test import APIClient

ERROR_INFO = "Error for method: {method}, url: {url}, status: {status}"


DOC_REDOC_URL = reverse("redoc")
DOC_SWAGGER_URL = reverse("swagger-ui")


@pytest.fixture
def guest_client():
    client = APIClient()
    return client
