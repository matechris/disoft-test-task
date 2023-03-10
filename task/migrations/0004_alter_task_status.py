# Generated by Django 4.1.2 on 2023-02-05 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0003_task_author_task_doer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "New"),
                    ("IN PROGRESS", "In progress"),
                    ("DONE", "Done"),
                ],
                default="NEW",
                max_length=11,
            ),
        ),
    ]
