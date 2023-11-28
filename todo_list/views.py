from django.contrib.auth import get_user_model
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from todo_list.models import Job, Task
from todo_list.permissions import IsJobOwnerPermission, IsTaskOwnerPermission
from todo_list.serializers import (
    JobSerializer,
    JobUpdateSerializer,
    TaskSerializer,
    UserCreateSerializer,
)

User = get_user_model()


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = TaskSerializer
    permission_classes = (
        IsAuthenticated,
        IsTaskOwnerPermission,
    )

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = (
        IsAuthenticated,
        IsJobOwnerPermission,
    )

    def get_queryset(self):
        return Job.objects.filter(task__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return JobUpdateSerializer
        return self.serializer_class
