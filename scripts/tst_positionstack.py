
import http.client, urllib.parse

conn = http.client.HTTPConnection('api.positionstack.com')

params = urllib.parse.urlencode({
    'access_key': 'a8a9e23c51078b7d65b82236902e0764',
    'query': '10 Edgelawn Av, Chelmsford, MA',
    'region': 'Massachusetts',
    'limit': 1,
    })

conn.request('GET', '/v1/forward?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))
