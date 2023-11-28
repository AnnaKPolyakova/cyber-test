import datetime
import random

import factory
from django.contrib.auth import get_user_model
from django.db.models import Q

from todo_list.models import Task, Job

User = get_user_model()


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task
        exclude = ["name_word"]

    name_word = factory.Faker("word", locale="ru_RU")
    name = factory.LazyAttribute(
        lambda a: "{}.{}".format(a.name_word, random.random())
    )
    user = factory.Iterator(User.objects.all())
    created_at = factory.Faker("datetime_this_year")


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job
        exclude = ["name_word"]

    task = factory.Iterator(Task.objects.all())
    name_word = factory.Faker("word", locale="ru_RU")
    name = factory.LazyAttribute(
        lambda a: "{}.{}".format(a.name_word, random.random())
    )
    is_done = random.choice([True, False])

    @factory.lazy_attribute
    def done_at(self):
        if self.is_done:
            return factory.Faker("datetime_this_year")
        return
