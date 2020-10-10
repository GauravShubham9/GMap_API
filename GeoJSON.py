import urllib.request, urllib.parse, urllib.error
import json

api_key = False
if api_key is False:
    api_key = 42
    googleurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    googleurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key

    url = googleurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('*****FAILED TO RETRIEVE*****')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lon = js["results"][0]["geometry"]["location"]["lng"]
    print('Latitude: ', lat, 'Longitude: ', lon)
    location = js['results'][0]['formatted_address']
    print(location)
