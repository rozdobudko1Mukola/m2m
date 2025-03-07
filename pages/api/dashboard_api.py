from playwright.sync_api import APIRequestContext, expect


class DashboardAPI:
    """Клас для роботи з API DashboardAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def dashboard_devices_stops_duration_rating(self, device_id, dateFrom, dateTo):
        """Метод для отримання рейтингу тривалості зупинок."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        data = {
            "deviceIds": device_id
        }
        response = self.api_context.post("/api/dashboard/stops", params=params, data=data, headers=self.headers)
        return response


    def dashboard_devices_mileage_rating(self, device_id, dateFrom, dateTo):
        """Метод для отримання рейтингу пробігу."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        data = {
            "deviceIds": device_id
        }
        response = self.api_context.post("/api/dashboard/mileage", params=params, data=data, headers=self.headers)
        return response


    def dashboard_devices_max_speed_rating(self, device_id, dateFrom, dateTo):
        """Метод для отримання рейтингу максимальної швидкості."""
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo
        }
        data = {
            "deviceIds": device_id
        }
        response = self.api_context.post("/api/dashboard/max-speed", params=params, data=data, headers=self.headers)
        return response


    def get_devices_actual_motion_state_based_on_speed(self):
        """Метод для отримання актуального стану руху на основі швидкості."""
        response = self.api_context.get("/api/dashboard/motions", headers=self.headers)
        return response


    def get_devices_connection_state(self):
        """Метод для отримання стану підключення пристроїв."""
        response = self.api_context.get("/api/dashboard/connection", headers=self.headers)
        return response