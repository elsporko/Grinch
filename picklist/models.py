from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import http.client, urllib.parse
from gis.models import GIS

import logging
import json
logger = logging.getLogger(__name__)

class Route(models.Model):
    """
    Identify routes by name users.groups tie to 1:1 to a route
    """
    #TODO - change name of sort_id to sort_order to distinguish from PickList.order_id
    order_id = models.IntegerField(null=False, blank=False, unique=True) # order of routes for display
    name = models.CharField (max_length=30, null=False, blank=False)
    abbrev = models.CharField (max_length=5, null=False, blank=False, primary_key=True)
    active = models.BooleanField(default=True, blank=False) # Note for initial development the database is sqlite3 which does not have a boolean type so it does not rewpect boolean default values

    @classmethod
    def get_route_id_by_abbrev(self, abbrev):
        return self.objects.get(abbrev = abbrev)

class PickList(models.Model):
    """
    """
    order_id = models.IntegerField(null=False, blank=False, primary_key=True) # PK from signup app. Used to avoid duplicate entries
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
    lat = models.FloatField(null=False, blank=False)
    lon = models.FloatField(null=False, blank=False)

    def save(self, *args, **kwargs):
        """
        Grab latitude and longitude based on given street address and include it in the picklist record
        """
        # Add GIS data to the picklist record
        gis = GIS()
        
        try:
            coords=GIS.objects.get(street_address=self.street_address)
            self.lat = coords.lat
            self.lon = coords.lon
        except GIS.DoesNotExist:
            coords = gis.get_lon_lat_external(self.street_address)
            self.lat = coords['lat']
            self.lon = coords['lon']

        super().save(*args, **kwargs)

