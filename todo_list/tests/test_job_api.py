from http import HTTPStatus

import pytest
from django.urls import reverse

from todo_list.models import Job
from todo_list.tests.conftest import ERROR_INFO, JOB_API_URL, JOBS_API_URL

pytestmark = pytest.mark.django_db


class TestJobAPI:
    def test_get_jobs(self, user_client, user_jobs, user_task, user_2_jobs):
        url = JOBS_API_URL
        method = "get"
        status = HTTPStatus.OK
        response = getattr(user_client, method)(
            url, param={"task": user_task.id}
        )
        db_count = Job.objects.filter(task=user_task).count()
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        assert response.data["count"] == min(15, db_count), ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_get_jobs_guest_client(
        self, guest_client, user_jobs, user_task, user_2_jobs
    ):
        url = JOBS_API_URL
        method = "get"
        status = HTTPStatus.UNAUTHORIZED
        response = getattr(guest_client, method)(url)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_get_job(self, user_client, user_job):
        url = reverse(JOB_API_URL, args=[user_job.id])
        method = "get"
        status = HTTPStatus.OK
        response = getattr(user_client, method)(url)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_post_job(self, user_client, user_task):
        url = JOBS_API_URL
        method = "post"
        status = HTTPStatus.CREATED
        data = {"name": "test", "task": user_task.id}
        db_count = Job.objects.all().count()
        response = getattr(user_client, method)(url, data=data)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        assert Job.objects.all().count() == db_count + 1, ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_delete_job(self, user_client, user_job):
        url = reverse(JOB_API_URL, args=[user_job.id])
        method = "delete"
        status = HTTPStatus.NO_CONTENT
        db_count = Job.objects.all().count()
        response = getattr(user_client, method)(url)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        assert Job.objects.all().count() == db_count - 1, ERROR_INFO.format(
            method=method, url=url, status=status
        )

    def test_update_job(self, user_client, user_job):
        url = reverse(JOB_API_URL, args=[user_job.id])
        method = "patch"
        status = HTTPStatus.OK
        new_name = "test_new"
        data = {"name": new_name}
        response = getattr(user_client, method)(url, data=data)
        assert response.status_code == status, ERROR_INFO.format(
            method=method, url=url, status=status
        )
        assert response.data["name"] == new_name, ERROR_INFO.format(
            method=method, url=url, status=status
        )
