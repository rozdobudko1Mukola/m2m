from playwright.sync_api import APIRequestContext, expect


class PositionAPI:
    """Клас для роботи з API Position."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


# Position API -----------------------------------------------------------------
    def retrieve_a_list_of_devices_positions(self, **kwargs):
        """Метод для отримання списку позицій пристроїв."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.post("api/devices/positions/latest", data=data, headers=self.headers)
        return response


    def get_details_the_track_by_speed_and_optional_trips_or_stops(self, device_id, dateFrom, dateTo, **kwargs):
        """Метод для отримання деталей треку за швидкістю та опціональними поїздками або зупинками."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        response = self.api_context.post(f"api/device/{device_id}/track/detail", data=data, params=params, headers=self.headers)
        return response


    def retrieve_a_list_of_device_track_positions_by_interval(self, device_id, dateFrom, dateTo, **kwargs):
        """Метод для отримання списку позицій треку пристрою за інтервалом."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        response = self.api_context.get(f"api/device/{device_id}/track", params=params, headers=self.headers)
        return response


    def retrieve_a_list_of_device_track_positions_by_trips(self, device_id, dateFrom, dateTo, **kwargs):
        """Метод для отримання списку позицій треку пристрою за поїздками."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        response = self.api_context.get(f"api/device/{device_id}/track/trips", params=params, headers=self.headers)
        return response


    def calculate_track_distance_by_interval_of_positions_in_kilometers(self, device_id, dateFrom, dateTo, **kwargs):
        """Метод для розрахунку відстані треку за інтервалом позицій в кілометрах."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        response = self.api_context.get(f"api/device/{device_id}/track/distance", params=params, headers=self.headers)
        return response


    def get_device_position_by_interval_with_pagination(self, device_id, dateFrom, dateTo):
        """Метод для отримання позицій пристрою за інтервалом з пагінацією."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        response = self.api_context.get(f"api/device/{device_id}/positions/interval", params=params, headers=self.headers)
        return response


    def get_the_last_position_of_device(self, device_id):
        """Метод для отримання останньої позиції пристрою."""
        response = self.api_context.get(f"api/device/{device_id}/position/latest", headers=self.headers)
        return response


    def export_device_positions_by_interval_to_file(self, ext_file, device_id, dateFrom, dateTo, **kwargs):
        """Метод для експорту позицій пристрою за інтервалом в файл."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        response = self.api_context.get(f"api/device/{device_id}/position/interval/{ext_file}", params=params, headers=self.headers)
        return response


    def get_device_geojson_track(self, device_id, dateFrom, dateTo, **kwargs):
        """Метод для отримання геоjson треку пристрою."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        response = self.api_context.get(f"api/device/{device_id}/geojson/positions", params=params, headers=self.headers)
        return response