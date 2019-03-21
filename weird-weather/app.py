"""Weird-Weather.
This application fetches the latest weather data from the internet and
displays that information from the user. Depending on the given location
of the user, he/she will receive relevant information pertaining to said
location.

Authors: [ Darshan Pillay, Kaylen Pillay ]
"""
import keystore
import networkUtils

# The request string used to fetch data from the server.
request_url = networkUtils.create_forecast_request_url(keystore.API_KEY["key"], forecast_length=1)

# Get the WeatherResponse object from the network call
response_object = networkUtils.fetch_weather_json_data(request_url)

# Display the result to the user
print(f"The response code was {response_object.get_response_code()}")
print(f"The response data was {response_object.get_raw_response_data()}")
