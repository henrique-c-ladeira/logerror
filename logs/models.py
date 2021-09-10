from django.db import models
from django.utils import timezone


class ErrorLog(models.Model):
    app_name = models.CharField(max_length=50)
    datetime = models.DateTimeField(default=timezone.now)
    stack = models.TextField()
    message = models.CharField(max_length=200)
