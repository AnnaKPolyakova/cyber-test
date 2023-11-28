from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from todo_list.views import JobViewSet, RegistrationAPIView, TaskViewSet

registration_patterns = [
    path("registration/", RegistrationAPIView.as_view(), name="registration"),
]

token_patterns = [
    path("token/create/", TokenObtainPairView.as_view(), name="token_create"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


user_urls = [
    path("users/", include(registration_patterns)),
    path("users/", include(token_patterns)),
]

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"job", JobViewSet, basename="jobs")


urlpatterns = [
    path("v1/", include(user_urls)),
    path("v1/", include(router.urls)),
]
