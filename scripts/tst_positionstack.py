
import http.client, urllib.parse

conn = http.client.HTTPConnection('api.positionstack.com')

queries = ['112 Westford St, Chelmsford, MA',
           '11 Pine Hill Rd, Chelmsford, MA']

for query in queries:
    params = urllib.parse.urlencode({
        'access_key': 'a8a9e23c51078b7d65b82236902e0764',
        'query': query,
        'region': 'Massachusetts',
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    print(data.decode('utf-8'))
