from http import HTTPStatus

import pytest

from todo_list.tests.conftest import (
    ERROR_INFO,
    PASSWORD,
    REFRESH_TOKEN_URL,
    TOKEN_URL,
)

pytestmark = pytest.mark.django_db


class TestTokenAPI:
    """User can get tokens token."""

    def test_get_token_url(self, guest_client, user):
        url = TOKEN_URL
        method = "post"
        status = HTTPStatus.OK
        tokens = ["refresh", "access"]
        data = {"username": user.username, "password": PASSWORD}
        response = getattr(guest_client, method)(url, data=data)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        for token in tokens:
            assert token in response.data, ERROR_INFO.format(
                method=method, url=url, status=status
            )

    def test_get_refresh_token_url(
        self, guest_client, user, user_refresh_token
    ):
        tokens = ["refresh", "access"]
        url = REFRESH_TOKEN_URL
        method = "post"
        status = HTTPStatus.OK
        data = {"refresh": user_refresh_token}
        response = getattr(guest_client, method)(url, data=data)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        for token in tokens:
            assert token in response.data, ERROR_INFO.format(
                method=method, url=url, status=status
            )
