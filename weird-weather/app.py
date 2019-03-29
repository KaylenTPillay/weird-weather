"""Weird-Weather.
This application fetches the latest weather data from the internet and
displays that information from the user. Depending on the given location
of the user, he/she will receive relevant information pertaining to said
location.

Authors: [ Darshan Pillay, Kaylen Pillay ]
"""
import keystore
import networkUtils
import dataUtils
import getpass




def display_weather(weather_reponse_dict):
    display_string = f"\nHey {getpass.getuser()}! \n" + \
                     "Here's your weather for today,\n\n" + \
                     f"Looks like its {weather_reponse_dict['title']}, {weather_reponse_dict['description']}\n" + \
                     f"Current temperature - {dataUtils.get_formatted_temp(weather_reponse_dict['temp'])} \u2103 \n" + \
                     f"High - {dataUtils.get_formatted_temp(weather_reponse_dict['temp_max'])} \u2103  \n" + \
                     f"Low - {dataUtils.get_formatted_temp(weather_reponse_dict['temp_min'])} \u2103 \n\n" + \
                     f"Thank you for using weird weather - developed by {dataUtils.__DEVELOPER}"

    print(display_string)


# The request string used to fetch data from the server.
request_url = networkUtils.create_forecast_request_url(keystore.API_KEY["key"],
                                                       forecast_length=1,
                                                       city_name="Durban",
                                                       country_name="ZA")

# Get the WeatherResponse object from the network call
response_object = networkUtils.fetch_weather_json_data(request_url)

# Display the result to the user
if networkUtils.is_response_successful(response_object.get_response_code()):
    # Parse the json response and get a dict of weather response strings back
    # weather_response_dict = dataUtil.parse_weather_data(response_object.get_response_data())
    display_weather(dataUtils.parse_weather_data(response_object.get_response_data()))

else:
    print("Our service is currently down. Please try again later.")

