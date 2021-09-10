from django.db import models
from django.utils import timezone


class ErrorLog(models.Model):
    app_name = models.CharField(max_length=50)
    datetime = models.DateTimeField(default=timezone.now)
    stack = models.TextField()
    message = models.CharField(max_length=200)

    @classmethod
    def create(cls, app_name, stack, message):
        error_log = cls(app_name=app_name, stack=stack, message=message)
        return error_log

    def __str__(self) -> str:
        return f'{self.app_name.upper()} at {self.datetime.strftime("%Y-%m-%d%H:%M:%S")}'
