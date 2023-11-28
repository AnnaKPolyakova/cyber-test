from http import HTTPStatus

import pytest
from django.urls import reverse

from todo_list.models import Task
from todo_list.tests.conftest import ERROR_INFO, TASK_API_URL, TASKS_API_URL

pytestmark = pytest.mark.django_db


class TestTaskAPI:
    def test_get_tasks(self, user_client, user, user_tasks, user_2_tasks):
        url = TASKS_API_URL
        method = "get"
        status = HTTPStatus.OK
        response = getattr(user_client, method)(url)
        db_count = Task.objects.filter(user=user).count()
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        assert response.data["count"] == min(15, db_count), ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_get_tasks_guest_client(
        self, guest_client, user, user_tasks, user_2_tasks
    ):
        url = TASKS_API_URL
        method = "get"
        status = HTTPStatus.UNAUTHORIZED
        response = getattr(guest_client, method)(url)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_get_task(self, user_client, user_task):
        url = reverse(TASK_API_URL, args=[user_task.id])
        method = "get"
        status = HTTPStatus.OK
        response = getattr(user_client, method)(url)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_post_task(self, user_client):
        url = TASKS_API_URL
        method = "post"
        status = HTTPStatus.CREATED
        data = {"name": "test"}
        db_count = Task.objects.all().count()
        response = getattr(user_client, method)(url, data=data)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        assert Task.objects.all().count() == db_count + 1, ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_delete_task(self, user_client, user_task):
        url = reverse(TASK_API_URL, args=[user_task.id])
        method = "delete"
        status = HTTPStatus.NO_CONTENT
        db_count = Task.objects.all().count()
        response = getattr(user_client, method)(url)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        assert Task.objects.all().count() == db_count - 1, ERROR_INFO.format(
            method=method, url=url, status=status
        )
