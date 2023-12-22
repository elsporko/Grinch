import pytest
from rest_framework.test import APIClient
from django.core.management import call_command

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'tests/fixtures/grinchdata.json')

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def picklist_fixture():
    return(
            {
                "order_id": 901,
                "pickup_date": "2022-12-31",
                "route": "fri",
                "first_name": "Max",
                "last_name": "Power",
                "home_phone": "+19783870017",
                "email": "Beetle_sue@comcast.net",
                "street_address": "10 Armand Dr",
                "where_is_it": "DRIVEWAY",
                "client_comment": "",
                "admin_comment": "",
                "got_money": False,
                "got_tree": False,
                "lat": 42.565024,
                "lon": -71.363719
            }
    )

@pytest.fixture
def grinch_data_fixture():
    return(
        [
            {
                "model": "picklist.route",
                "pk": "fri",
                "fields": {
                    "order_id": 5,
                    "name": "Friday",
                    "active": True
                }
            },
            {
                "model": "picklist.route",
                "pk": "mon",
                "fields": {
                    "order_id": 1,
                    "name": "Monday",
                    "active": True
                }
            },
            {
                "model": "picklist.route",
                "pk": "thu",
                "fields": {
                    "order_id": 4,
                    "name": "Thursday",
                    "active": True
                }
            },
            {
                "model": "picklist.route",
                "pk": "tue",
                "fields": {
                    "order_id": 2,
                    "name": "Tuesday",
                    "active": True
                }
            },
            {
                "model": "picklist.route",
                "pk": "wed",
                "fields": {
                    "order_id": 3,
                    "name": "Wednesday",
                    "active": True
                }
            },
#           {
#               "model": "picklist.picklist",
#               "pk": 1,
#               "fields": {
#                   "order_id": 702,
#                   "pickup_date": "2022-12-31",
#                   "route": "fri",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+19783870017",
#                   "email": "Beetle_sue@comcast.net",
#                   "street_address": "10 Armand Dr",
#                   "where_is_it": "DRIVEWAY",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 42.565024,
#                   "lon": -71.363719
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 2,
#               "fields": {
#                   "order_id": 671,
#                   "pickup_date": "2022-12-31",
#                   "route": "fri",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+16174169991",
#                   "email": "jkellybeatty@comcast.net",
#                   "street_address": "117 Park Rd",
#                   "where_is_it": "SIDE",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 3,
#               "fields": {
#                   "order_id": 588,
#                   "pickup_date": "2022-12-31",
#                   "route": "fri",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+19782908444",
#                   "email": "scostantino@verizon.net",
#                   "street_address": "13 Wedgewood Dr",
#                   "where_is_it": "DRIVEWAY",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 4,
#               "fields": {
#                   "order_id": 414,
#                   "pickup_date": "2022-12-31",
#                   "route": "fri",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+19782566018",
#                   "email": "barbbq1@aol.com",
#                   "street_address": "14 Brian Rd",
#                   "where_is_it": "DRIVEWAY",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 5,
#               "fields": {
#                   "order_id": 647,
#                   "pickup_date": "2022-12-31",
#                   "route": "fri",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+17812640525",
#                   "email": "bdalleva1013@gmail.com",
#                   "street_address": "15  Wedgewood Dr",
#                   "where_is_it": "DRIVEWAY",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 6,
#               "fields": {
#                   "order_id": 518,
#                   "pickup_date": "2022-12-31",
#                   "route": "fri",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+19787583644",
#                   "email": "Kate42342@yahoo.com",
#                   "street_address": "150 Park Rd",
#                   "where_is_it": "SIDE",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 7,
#               "fields": {
#                   "order_id": 781,
#                   "pickup_date": "2022-12-31",
#                   "route": "thu",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+19785801258",
#                   "email": "harrislaurel@hotmail.com",
#                   "street_address": "156 Wellman Av",
#                   "where_is_it": "DRIVEWAY",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 8,
#               "fields": {
#                   "order_id": 178,
#                   "pickup_date": "2022-12-31",
#                   "route": "mon",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+17742872666",
#                   "email": "nadineroserichert@gmail.com",
#                   "street_address": "1  Lemay Way",
#                   "where_is_it": "INFRONT",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 9,
#               "fields": {
#                   "order_id": 50,
#                   "pickup_date": "2022-12-31",
#                   "route": "tue",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+19782564796",
#                   "email": "julie_brackett@comcast.net",
#                   "street_address": "10 Clover Hill Dr",
#                   "where_is_it": "DRIVEWAY",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "picklist.picklist",
#               "pk": 10,
#               "fields": {
#                   "order_id": 589,
#                   "pickup_date": "2022-12-31",
#                   "route": "wed",
#                   "first_name": null,
#                   "last_name": null,
#                   "home_phone": "+16174178448",
#                   "email": "Hkleanthous@gmail.com",
#                   "street_address": "1 Peachtree Ln",
#                   "where_is_it": "DRIVEWAY",
#                   "client_comment": "",
#                   "admin_comment": null,
#                   "got_money": false,
#                   "got_tree": false,
#                   "lat": 0.0,
#                   "lon": 0.0
#               }
#           },
#           {
#               "model": "users.grinchuser",
#               "pk": 1,
#               "fields": {
#                   "password": "pbkdf2_sha256$390000$NPQ7Ur6ekMCMJ7ICHrhUlZ$dQV70iHHor4JL2v8lNMe48WAz+4uH5xz8Br/TMOHTMw=",
#                   "last_login": "2023-07-30T01:51:06.733Z",
#                   "is_superuser": true,
#                   "username": "admin",
#                   "first_name": "",
#                   "last_name": "",
#                   "email": "admin@admin.com",
#                   "is_staff": true,
#                   "is_active": true,
#                   "date_joined": "2023-07-30T01:51:00.299Z",
#                   "route": null,
#                   "groups": [],
#                   "user_permissions": []
#               }
#           },
#           {
#               "model": "users.grinchuser",
#               "pk": 2,
#               "fields": {
#                   "password": "Sp0rkfish",
#                   "last_login": null,
#                   "is_superuser": false,
#                   "username": "jspooner",
#                   "first_name": "John",
#                   "last_name": "Spooner",
#                   "email": "elsporko@gmail.com",
#                   "is_staff": false,
#                   "is_active": true,
#                   "date_joined": "2023-07-30T01:51:21Z",
#                   "route": "mon",
#                   "groups": [],
#                   "user_permissions": []
#               }
#           },
#           {
#               "model": "users.grinchuser",
#               "pk": 3,
#               "fields": {
#                   "password": "troop70",
#                   "last_login": null,
#                   "is_superuser": false,
#                   "username": "rspooner",
#                   "first_name": "Ryan",
#                   "last_name": "Spooner",
#                   "email": "ryanmspooner@gmail.com",
#                   "is_staff": false,
#                   "is_active": true,
#                   "date_joined": "2023-07-30T01:52:09Z",
#                   "route": "thu",
#                   "groups": [],
#                   "user_permissions": []
#               }
#           }
        ]
    )



@pytest.fixture
def picklist_fixture_orig():
    return(
        [
            {
                "model": "picklist.picklist",
                "pk": 1,
                "fields": {
                    "order_id": 702,
                    "pickup_date": "2022-12-31",
                    "route": "fri",
                    "first_name": "Max",
                    "last_name": "Power",
                    "home_phone": "+19783870017",
                    "email": "Beetle_sue@comcast.net",
                    "street_address": "10 Armand Dr",
                    "where_is_it": "DRIVEWAY",
                    "client_comment": "",
                    "admin_comment": "",
                    "got_money": False,
                    "got_tree": False,
                    "lat": 42.565024,
                    "lon": -71.363719
                }
            }
        ]
    )

@pytest.fixture
def route_fixture():
    return(
        [
                {
                    "order_id": 1,
                    "abbrev": "mon",
                    "name": "Monday",
                    "active": True,
                },
                {
                    "order_id": 2,
                    "abbrev": "tue",
                    "name": "Tuesday",
                    "active": True,
                },
                {
                    "order_id": 3,
                    "abbrev": "wed",
                    "name": "Wednesday",
                    "active": True,
                },
                {
                    "order_id": 4,
                    "abbrev": "thu",
                    "name": "Thursday",
                    "active": True,
                },
                {
                    "order_id": 5,
                    "abbrev": "fri",
                    "name": "Friday",
                    "active": True,
                },
        ]
)
