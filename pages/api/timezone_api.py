from playwright.sync_api import APIRequestContext, expect


class TimezoneAPI:
    """Клас для роботи з API TimezoneAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def retrieve_a_list_of_available_timezones(self):
        """Метод для отримання списку доступних часових зон."""
        response = self.api_context.get("/api/timezones", headers=self.headers)
        return response