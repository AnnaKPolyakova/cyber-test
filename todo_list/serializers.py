from django.contrib.auth import get_user_model
from rest_framework import serializers

from todo_list.models import Job, Task

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "User with this email already exists."
            )
        return value

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ["user"]
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

    def validate_task(self, value):
        if self.context["request"].user != value.user:
            raise serializers.ValidationError("Not task owner")
        return value


class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        read_only_fields = ["task", "is_done"]
        fields = "__all__"
