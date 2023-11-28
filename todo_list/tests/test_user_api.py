from http import HTTPStatus

import pytest
from django.contrib.auth import get_user_model

from todo_list.tests.conftest import (
    EMAIL,
    ERROR_INFO,
    PASSWORD,
    USER_REG_API_URL
)

User = get_user_model()

pytestmark = pytest.mark.django_db


class TestUserAPI:
    def test_user_reg_url(self, guest_client):
        url = USER_REG_API_URL
        method = "post"
        status = HTTPStatus.CREATED
        data = {
            "username": EMAIL,
            "password": PASSWORD,
            "email": EMAIL,
        }
        db_count = User.objects.all().count()
        response = getattr(guest_client, method)(url, data=data)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        assert User.objects.all().count() == db_count + 1, ERROR_INFO.format(
            method=method, url=url, status=status
        )
