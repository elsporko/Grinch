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
    def get_lon_lat_external(self, street_address):
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

        
        self.street_address = street_address
        self.lat = coords['data'][0]['latitude']
        self.lon = coords['data'][0]['longitude']

        self.save()

        return{'lat': coords['data'][0]['latitude'], 
               'lon': coords['data'][0]['longitude'], 
               'address': coords['data'][0]['name']}
