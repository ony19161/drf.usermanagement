from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    isActive = models.BooleanField(default=True)
    createdBy = models.IntegerField(null=True)
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedBy = models.IntegerField(null=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
