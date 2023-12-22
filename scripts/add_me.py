import requests

with open('picklist.csv') as f:
    lines = [line.replace('"', '').rstrip() for line in f]

url = 'http://localhost:8000/api/picklist/'
picklist_data = {
       'order_id'       : 1020,
       'pickup_date'    : '2022-12-31',
       'route'          : 'mon',
       'first_name'     : 'John',
       'last_name'      : 'Spooner',
       'home_phone'     : '+19782517220',
       'email'          : 'elsporko@gmail.com',
       'street_address' : '47 Mission Road',
       'where_is_it'    : 'DRIVEWAY',
       'client_comment' : 'Huzzah',
}

x = requests.post(url, picklist_data)
print (x.text)
