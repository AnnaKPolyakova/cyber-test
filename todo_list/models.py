from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Task(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Name",
        help_text="Set the name of the task",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name="Executor",
        help_text="Set executor",
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        help_text="Set creation date",
        # default=timezone.now,
        auto_now_add=True,
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Name",
        help_text="Set the name of the job",
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="jobs",
        verbose_name="Task",
        help_text="Select the task on which the work was carried out",
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name="Job completion",
        help_text="Set completion of the job",
    )
    done_at = models.DateTimeField(
        verbose_name="Job completion dates",
        blank=True,
        null=True,
        help_text="Set the date of completion of the job",
    )

    def save(self, *args, **kwargs):
        if self.done_at is None:
            self.is_done = False
        else:
            self.is_done = True
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.name
