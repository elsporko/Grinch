#from django.test import TestCase
from picklist.models import PickList, Route
import pytest

from picklist.models import *

@pytest.mark.django_db
def test_get_picklist(api_client):

    url = '/api/picklist/702/'
    response = api_client.get(url, format='json')

    payload = response.data
    assert response.status_code == 200

    sample_pick = PickList.objects.get(order_id = 702)
    assert payload['name'] == (f'{sample_pick.first_name} {sample_pick.last_name}')

#TODO Add picklist via API POST and verify the data (including lat/lon) are correct
#   * Ensure proper status code
#   * Check data accuracy
#   * Ensure there is a record in gis_gis for the lon/lat values
#@pytest.mark.django_db
#def test_post_update_picklist(api_client):
#    url = '/api/picklist/'
#
#    street_address =  '47 Mission Road'
#    new_picklist = {
#            'order_id' : 900,
#            'pickup_date' : '2022-12-31',
#            'route' : 'mon',
#            'home_phone' : '+19788461531',
#            'email' : 'elsporko@gmail.com',
#            'street_address' : street_address,
#            'where_is_it' : 'DRIVEWAY',
#            'client_comment' : '',
#            'first_name': 'John',
#            'last_name': 'Spooner',
#    }
#
#    response = api_client.post(url, new_picklist)
#    assert response.status_code == 200
#
#    # Ensure a local record has been written to gis_gis
#    test_rec = PickList.objects.get(order_id = 900)
#    gis_rec = GIS.objects.get(street_address = street_address)
#    assert (test_rec.lat == gis_rec.lat)
#    assert (test_rec.lon == gis_rec.lon)
#
#    new_picklist['route'] = 'thu'
#    response = api_client.put(url, new_picklist)
#    print(f'response: {response}')
#    assert response.status_code == 200
#    
#    test_rec = PickList.objects.put(order_id = 900)
#    assert test_rec.route == 'thu'

@pytest.mark.django_db
def test_get_route(api_client, route_fixture):
    url = '/api/routes/mon/'
    response = api_client.get(url, format='json')

    payload = response.data
    assert response.status_code == 200

    sample_route = Route.objects.get(pk='mon')
    assert payload['name'], sample_route.name

#TODO Add Route via API POST
# * Create new record and validate data, ensure default satus is active
# * Set new route to inactive and validate that only active records are returned
@pytest.mark.django_db
def test_post_update_route(api_client):
    url = '/api/routes/'
    new_route = {
        'order_id': 10,
        'abbrev': 'new',
        'name':'New Route',
    }

    response = api_client.post(url, new_route)
    print(f'response: {response}')
    assert response.status_code == 200
