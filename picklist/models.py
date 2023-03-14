from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#from .models import PickList

import logging
logger = logging.getLogger(__name__)

class Route(models.Model):
    """
    Identify routes by name users.groups tie to 1:1 to a route
    """
    name = models.CharField (max_length=30, null=False, blank=False)

    @classmethod
    def get_route_id_by_name(self, route_name):
        return self.objects.filter(name = route_name).first().id

class PickList(models.Model):
    """
    """
    order_id = models.IntegerField(null=False, blank=False, unique=True) # PK from signup app. Used to avoid duplicate entries
    pickup_date = models.DateField(null=False, blank=False)
    route = models.ForeignKey(Route, null=False, on_delete=models.PROTECT)
    first_name = models.CharField (max_length=64, null=True, blank=True)
    last_name = models.CharField (max_length=64, null=True, blank=True)
    home_phone = PhoneNumberField(null=False, blank=True, unique=True)
    email = models.EmailField(max_length=128)
    street_address = models.CharField(max_length=140, null=False, blank = False)
    where_is_it = models.CharField (max_length=30, null=True, blank=True)
    client_comment = models.CharField (max_length=256, null=True, blank=True) # Comment that comes from the tree registration app ('Pick up inside the house', etc.)
    admin_comment = models.CharField (max_length=500, null=True, blank=True)
    got_money = models.BooleanField(default=False)
    got_tree = models.BooleanField(default=False)

