import json

__DEVELOPER = "Darshan Pillay"
__KELVIN_TO_CELSIUS = -273.15

def parse_weather_data(json_response):
    # The weather response dict contains strings that are displayed
    # to the user. The data parsed should be formatted appropriately.
    weather_response_dict = {}
    parsed_json = json.loads(json_response)

    # weather meta details includes the title, description and icon.
    weather_meta_details = parsed_json["weather"][0]
    weather_meta_details_title = weather_meta_details["main"]
    weather_meta_details_description = weather_meta_details["description"]
    weather_meta_details_icon = weather_meta_details["icon"]

    # weather meta main include the current temp, min and max temp and the humidity
    weather_meta_main = parsed_json["main"]
    weather_meta_main_temp = weather_meta_main["temp"]
    weather_meta_main_temp_min = weather_meta_main["temp_min"]
    weather_meta_main_temp_max = weather_meta_main["temp_max"]
    weather_meta_main_humidity = weather_meta_main["humidity"]

    # add all the weather data to the response dict
    weather_response_dict["title"] = weather_meta_details_title
    weather_response_dict["description"] = weather_meta_details_description
    weather_response_dict["icon"] = weather_meta_details_icon
    weather_response_dict["temp"] = weather_meta_main_temp
    weather_response_dict["temp_min"] = weather_meta_main_temp_min
    weather_response_dict["temp_max"] = weather_meta_main_temp_max
    weather_response_dict["humidity"] = weather_meta_main_humidity

    return weather_response_dict


def get_formatted_temp(temp):
    return round(float(temp) + __KELVIN_TO_CELSIUS, 1)
