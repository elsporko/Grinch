from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import logging
logger = logging.getLogger(__name__)

class Route(models.Model):
    """
    Identify routes by name users.groups tie to 1:1 to a route
    """
    name = models.CharField (max_length=30, null=False, blank=False)

class PickList(models.Model):
    """
    """
    order_id = models.IntegerField(null=False, blank=False) # PK from signup app. Used to avoid duplicate entries
    pickup_date = models.DateField(null=False, blank=False)
    route = models.ForeignKey(Route, null=False, on_delete=models.PROTECT)
    first_name = models.CharField (max_length=50, null=True, blank=True)
    last_name = models.CharField (max_length=50, null=True, blank=True)
    home_phone = PhoneNumberField(null=False, blank=True, unique=True)
    email = models.EmailField(max_length=254)
    street_address = models.CharField(max_length=100, null=False, blank = False)
    where_is_it = models.CharField (max_length=30, null=True, blank=True)
    client_comment = models.CharField (max_length=256, null=True, blank=True) # Comment that comes from the tree registration app ('Pick up inside the house', etc.)
    admin_comment = models.CharField (max_length=500, null=True, blank=True)
    got_money = models.BooleanField(default=False)
    got_tree = models.BooleanField(default=False)

    #def update_picklist(self, *args, **kwargs):
    #    keys = *kwargs.keys()
    #    print (f'******* keys: {keys}')
