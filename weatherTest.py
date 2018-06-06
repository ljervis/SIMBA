from weather import Weather, Unit

weather = Weather(Unit.FAHRENHEIT)
lookup = weather.lookup_by_latlng(53.3494,-6.2601)
forecasts = lookup.forecast
today = forecasts[0]
print(today.text + "\n" + today.date + "\n" + today.high + "\n" + today.low)
