# Generated by Django 4.2.7 on 2023-11-28 16:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo_list", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="job",
            options={
                "ordering": ["name"],
                "verbose_name": "Job",
                "verbose_name_plural": "Jobs",
            },
        ),
    ]
