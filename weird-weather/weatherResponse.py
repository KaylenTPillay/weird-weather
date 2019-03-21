class WeatherResponse:
    def __init__(self, response_status, response_data):
        self.response_status = response_status
        self.response_data = response_data

    def get_raw_response_data(self):
        return self.response_data

    def get_response_code(self):
        return self.response_status
