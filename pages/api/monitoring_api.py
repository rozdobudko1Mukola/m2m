from playwright.sync_api import APIRequestContext, expect


class monitoringAPI:
    """Клас для роботи з API monitoringAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def search_monitoring_devices_by_address_or_name(self, search: str):
        """Метод для пошуку моніторингу по адресі або імені."""
        params = {
            "search": search
        }
        response = self.api_context.get("/api/monitoring/search", params=params, headers=self.headers)
        return response


    def retrieve_a_list_of_monitoring_devices_with_pagination(self, **kwargs):
        """Метод для отримання списку моніторингу з пагінацією."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get("/api/devices/monitoring", params=params, headers=self.headers)
        return response


    def retrieve_a_list_of_a_monitoring_device_group(self, group_id: int):
        """Метод для отримання списку групи моніторингу."""
        response = self.api_context.get(f"/api/device/group/{group_id}/monitoring", headers=self.headers)
        return response