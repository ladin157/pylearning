import requests
import json

url = 'http://api.openweathermap.org/data/2.5/weather?q=London'

response = requests.get(url)

if response.ok:
    jdata = json.loads(response.content)

    print(jdata)
else:
    response.raise_for_status()
