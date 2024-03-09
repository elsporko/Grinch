from django.db import models
from django.contrib.auth.models import AbstractUser
from picklist.models import Route
from .managers import CustomUserManager


class GrinchUser(AbstractUser):
    route = models.ForeignKey(Route, null=True, blank=True, on_delete=models.PROTECT)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
