import requests

route_list = [
 {
    'order_id' : 1,
    'name' : 'Monday',
    'abbrev' : 'mon',
    'active' : 'True',
 },
 {
    'order_id' : 2,
    'name' : 'Tuesday',
    'abbrev' : 'tue',
    'active' : 'True',
 },
 {
    'order_id' : 3,
    'name' : 'Wednesday',
    'abbrev' : 'wed',
    'active' : 'True',
 },
 {
    'order_id' : 4,
    'name' : 'Thursday',
    'abbrev' : 'thu',
    'active' : 'True',
 },
 {
    'order_id' : 5,
    'name' : 'Friday',
    'abbrev' : 'fri',
    'active' : 'True',
 },
]

url = 'http://localhost:8000/api/routes/'

for route in route_list:
    print(f'route: {route}')
    route_data={
        'order_id' : route['order_id'],
        'name' : route['name'],
        'abbrev': route['abbrev'],
        'active': route['active'],
    }

    print(f'route_data: {route_data}')
    res = requests.post(url, route_data)
    #print(res.status)
