import requests

with open('picklist.csv') as f:
    lines = [line.replace('"', '').rstrip() for line in f]

url = 'http://localhost:8000/api/picklist/'
for line in lines:
    (orderid,PickupDate,route,firstname,lastname,homephone,email,streetaddress,whereisit,comments) = line.split(',')

    picklist_data = {
           'order_id'       : orderid,
           'pickup_date'    : PickupDate,
           'route'          : route,
           'first_name'     : firstname,
           'last_name'      : lastname,
           'home_phone'     : homephone,
           'email'          : email,
           'street_address' : streetaddress,
           'where_is_it'    : whereisit,
           'client_comment' : comments,
    }

    x = requests.post(url, picklist_data)
    print (x.text)
