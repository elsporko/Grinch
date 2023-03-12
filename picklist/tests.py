from django.test import TestCase

from picklist.models import *

class PicklistTests(TestCase):
    fixtures = ['routes.json', 'picklist.json']

    def test_get_address(self):
        addr = PickList.objects.get(pk=1)
        self.assertEqual(addr.order_id, 178)

    def test_save_picklist(self):
        new_p = PickList()

        new_p.order_id = 1
        new_p.pickup_date = '2023-02-14'
        new_p.route = Route.objects.get(pk=1)
        new_p.first_name = 'John'
        new_p.last_name = 'Spooner'
        new_p.home_phone = '9788461531'
        new_p.email = 'elsporko@gmail.com'
        new_p.street_address = '47 Mission Road'
        new_p.where_is_it = 'DRIVEWAY'
        new_p.client_comment = 'Thanks'

        new_p.save()

        p = PickList.objects.get(pk=4)

        self.assertEqual(p.order_id, 1)
        #self.assertEqual(p.pickup_date, '2023-02-14')
        self.assertEqual(p.route, Route.objects.get(pk=1))
        self.assertEqual(p.first_name, 'John')
        self.assertEqual(p.last_name, 'Spooner')
        self.assertEqual(p.home_phone, '9788461531')
        self.assertEqual(p.email, 'elsporko@gmail.com')
        self.assertEqual(p.street_address, '47 Mission Road')
        self.assertEqual(p.where_is_it, 'DRIVEWAY')
        self.assertEqual(p.client_comment, 'Thanks')

    def test_update_picklist(self):
        p = PickList.objects.get(pk=4)
        p.client_comment = 'Good job!!!'
        p.update_picklist()


class RouteTests(TestCase):
    fixtures = ['routes.json']

    def test_get_route(self):
        route = Route.objects.get(pk=1)
        self.assertEqual(route.name, 'mon')

class RouteNoteTests(TestCase):
    pass
