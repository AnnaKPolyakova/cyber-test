from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from todo_list.models import Job, Task

User = get_user_model()


class JobTaskRelationLine(admin.TabularInline):
    model = Job
    verbose_name_plural = "Users task"
    readonly_fields = ("is_done",)


@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "created_at",
    )
    list_filter = ("name", "user", "created_at")
    inlines = (JobTaskRelationLine,)


@register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "done_at",
        "is_done",
    )
    readonly_fields = ("is_done",)

    list_filter = ("task", "done_at", "is_done")


class TaskUserRelationLine(admin.TabularInline):
    model = Task
    verbose_name_plural = "Users task"


@register(User)
class UserAdmin(UserAdmin):
    ordering = ("username",)
    inlines = (TaskUserRelationLine,)
    list_display = ("email", "username")
    list_filter = ("email", "username")
