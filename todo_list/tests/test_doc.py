from http import HTTPStatus

from todo_list.tests.conftest import DOC_REDOC_URL, DOC_SWAGGER_URL, ERROR_INFO


class TestDocAPI:
    def test_doc_redoc_get(self, guest_client):
        url = DOC_REDOC_URL
        method = "get"
        status = HTTPStatus.OK
        response = getattr(guest_client, method)(url)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_doc_get(self, guest_client):
        url = DOC_SWAGGER_URL
        method = "get"
        status = HTTPStatus.OK
        response = getattr(guest_client, method)(url)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
