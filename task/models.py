from django.db import models

from user.models import User


class Task(models.Model):
    TASK_STATUSES = [
        ("NEW", "New"),
        ("IN PROGRESS", "In progress"),
        ("DONE", "Done")
    ]

    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    status = models.CharField(
        max_length=11,
        choices=TASK_STATUSES,
        default="NEW"
    )
    author = models.ManyToManyField(
        to=User, related_name="author"
    )
    doer = models.ManyToManyField(
        to=User, related_name="doer"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return str(self.title)
