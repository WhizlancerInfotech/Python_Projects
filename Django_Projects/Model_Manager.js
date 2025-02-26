from django.db import models

class ActiveUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class CustomUser(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()  # Default Manager
    active_users = ActiveUserManager()  # Custom Manager
