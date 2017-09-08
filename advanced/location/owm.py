import pyowm

owm = pyowm.OWM('54c53b2c82717a11d927717b7000aadc')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast('Milan, it')
tomorow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorow)

# Search for current weather in London (UK)
observation = owm.weather_at_place('Hanoi,vn')
w = observation.get_weather()
print(w)

# Weather details
wind = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
print(wind)
humidity = w.get_humidity()              # 87
print(humidity)
temp = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(temp)

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
print(observation_list)
