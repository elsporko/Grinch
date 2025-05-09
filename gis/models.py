from django.db import models
import http.client, urllib.parse
import json

class GIS(models.Model):
    """
    Local storage of Lat and Long data to reduce the number of outgoing API calls to map GIS coordinates to addresses
    """
    street_address = models.CharField(max_length=140, null=False, blank=False)
    lat = models.FloatField()
    lon = models.FloatField()

    """
    """
    @staticmethod
    def get_coords(street_address):
        try:
            local_coords = GIS.objects.get(street_address=street_address)
            return{'lat': local_coords.lat, 'lon': local_coords.lon, 'address': local_coords.street_address}
        except GIS.DoesNotExist:
            pass

        conn = http.client.HTTPConnection('api.positionstack.com')

        params = urllib.parse.urlencode({
            'access_key': 'a8a9e23c51078b7d65b82236902e0764',
            'query': ''.join([street_address, ', Chemlsford, MA']),
            'region': 'Massachusetts',
            'limit': 1,
            })

        conn.request('GET', '/v1/forward?{}'.format(params))

        res = conn.getresponse()
        coords = json.loads(res.read().decode('utf-8'))


        # TODO review positionstack error handling and change this accordingly
        if 'error' in coords: # (coords['error']):
            # TODO - Gracefully handle error response from positionstack.
            return{'lat': 0, 'lon': 0, 'address': street_address}

        new_record = GIS(
        street_address = street_address
        lat = coords['data'][0]['latitude']
        lon = coords['data'][0]['longitude']
        )

        new_record.save()

        return{'lat': coords['data'][0]['latitude'], 
               'lon': coords['data'][0]['longitude'], 
               'address': coords['data'][0]['name']}
