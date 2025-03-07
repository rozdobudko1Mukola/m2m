from playwright.sync_api import APIRequestContext, expect


class ProtocolAPI:
    """Клас для роботи з API ProtocolAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def retrieve_a_list_of_device_protocols(self, search):
        """Метод для отримання списку протоколів."""
        params = {
            "search": search
        }
        response = self.api_context.get(f"/api/protocols", params=params, headers=self.headers)
        return response


    def get_device_protocol_by_model(self, model):
        """Метод для отримання протоколу по моделі."""
        response = self.api_context.get(f"/api/protocol/{model}", headers=self.headers)
        return response