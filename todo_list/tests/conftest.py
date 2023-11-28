import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from todo_list.tests.factories import JobFactory, TaskFactory

ERROR_INFO = "Error for method: {method}, url: {url}, status: {status}"


DOC_REDOC_URL = reverse("redoc")
DOC_SWAGGER_URL = reverse("swagger-ui")
TOKEN_URL = reverse("token_create")
REFRESH_TOKEN_URL = reverse("token_refresh")
TASKS_API_URL = reverse("tasks-list")
TASK_API_URL = "tasks-detail"
JOBS_API_URL = reverse("jobs-list")
JOB_API_URL = "jobs-detail"


EMAIL = "Test@test.ru"
PASSWORD = "Test"

EMAIL_2 = "Test2@test.ru"
PASSWORD_2 = "Test"

User = get_user_model()

TASKS_COUNT = 3


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


@pytest.fixture
def user_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def user_2():
    user = User(username=EMAIL_2, email=EMAIL_2)
    user.set_password(PASSWORD_2)
    user.save()
    return user


@pytest.fixture
def user_refresh_token(user):
    return str(RefreshToken.for_user(user))


@pytest.fixture
def user_tasks(user):
    return TaskFactory.create_batch(TASKS_COUNT, user=user)


@pytest.fixture
def user_task(user):
    return TaskFactory(user=user)


@pytest.fixture
def user_2_tasks(user_2):
    return TaskFactory.create_batch(TASKS_COUNT, user=user_2)


@pytest.fixture
def user_2_task(user_2):
    return TaskFactory(user=user_2)


@pytest.fixture
def user_jobs(user, user_task):
    return JobFactory.create_batch(TASKS_COUNT, task=user_task)


@pytest.fixture
def user_job(user, user_task):
    return JobFactory(task=user_task)


@pytest.fixture
def user_2_jobs(user_2, user_2_task):
    return JobFactory.create_batch(TASKS_COUNT, task=user_2_task)
