from rest_framework.permissions import BasePermission


class IsTaskOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user == obj.user:
                return True
        return False


class IsJobOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user == obj.task.user:
                return True
        return False
