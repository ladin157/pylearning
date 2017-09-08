import yweather

client = yweather.Client()
woeid = client.fetch_woeid('Ho Chi Minh City, Vietnam')
print(woeid)
paris_weather = client.fetch_weather("615702", metric=True)
print(paris_weather["atmosphere"]["state"])
#print(weather['guid'])
# print(weather['description'])
# print(weather['condition']['temp'])