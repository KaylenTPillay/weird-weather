import urllib.parse as urllib
import urllib3
import certifi
from collections import OrderedDict
from weatherResponse import WeatherResponse

__INITIAL_URL__ = "https://api.openweathermap.org/data/2.5/"
__GET_METHOD__ = "GET"


def __is_forecast_length_valid(forecast_length):
    if forecast_length <= 0 or forecast_length > 5:
        return False
    else:
        return True


def __get_city_country(city_name, country_name):
    return city_name + ", " + country_name


def create_forecast_request_url(api_key, city_name="Cape Town", country_name="South Africa", forecast_length=3):
    if not __is_forecast_length_valid(forecast_length):
        valid_forecast_length = 3
    else:
        valid_forecast_length = forecast_length

    api_method = "weather?"
    query_string = urllib.urlencode(OrderedDict(q=__get_city_country(city_name, country_name),
                                                cnt=valid_forecast_length,
                                                APPID=api_key))
    return __INITIAL_URL__ + api_method + query_string


def fetch_weather_json_data(request_url):
    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED",
                               ca_certs=certifi.where())
    response = http.request(__GET_METHOD__, request_url)
    return WeatherResponse(response.status, response.data)


def is_response_successful(response_code):
    response_code_string = str(response_code)
    if response_code_string[0] == '2':
        return True
    else:
        return False

