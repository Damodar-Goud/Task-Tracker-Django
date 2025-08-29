from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title: str = models.CharField(max_length=100)
    description = models.TextField()
    completed: bool = models.BooleanField(default=False)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
