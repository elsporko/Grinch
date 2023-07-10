from django.db import models
from django.contrib.auth.models import AbstractUser
from picklist.models import Route

class GrinchUser(AbstractUser):
    route = models.ForeignKey(Route, null=True, blank=True, on_delete=models.PROTECT)
