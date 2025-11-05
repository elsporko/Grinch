from django.db import models
from grinch.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
import http.client, urllib.parse
from gis.models import GIS

import logging
import json
logger = logging.getLogger(__name__)


class Route(BaseModel):
    """
    Identify routes by name users.groups tie to 1:1 to a route
    """
    #TODO - change name of sort_id to sort_order to distinguish from PickList.order_id
    order_id = models.IntegerField(null=False, blank=False, unique=True) # order of routes for display
    name = models.CharField (max_length=30, null=False, blank=False)
    abbrev = models.CharField (max_length=5, null=False, blank=False, primary_key=True)
    active = models.BooleanField(default=True, blank=False) # Note for initial development the database is sqlite3 which does not have a boolean type so it does not rewpect boolean default values

    def __str__(self):
        return f"{self.name} ({self.abbrev})"

    @classmethod
    def get_route_id_by_abbrev(self, abbrev):
        return self.objects.get(abbrev = abbrev)

