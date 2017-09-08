import forecastio

api_key = '14bebed72ee4a10b334d1a6ed8ae7ce1'
lat = -31.967819
lng = 115.87718
forecast = forecastio.load_forecast(api_key, lat, lng)
byHour = forecast.hourly()
print(byHour)