from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
