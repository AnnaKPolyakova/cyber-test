import random

import factory
import pytz
from django.contrib.auth import get_user_model
from faker import Faker

from todo_list.models import Job, Task

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

    @factory.lazy_attribute
    def created_at(self):
        fake = Faker()
        return fake.date_time_this_year(tzinfo=pytz.timezone("Europe/Moscow"))


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
            fake = Faker()
            return fake.date_time_this_year(
                tzinfo=pytz.timezone("Europe/Moscow")
            )
        return None
