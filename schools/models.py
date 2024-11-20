from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser


class School(models.Model):
    name = models.CharField(max_length=255)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='school_admin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
