from playwright.sync_api import APIRequestContext, expect


class deviceCommandsAPI:
    """Клас для роботи з API deviceCommandsAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def get_device_command_by_id(self, device_id: int, command_id: int):
        """Метод для отримання команди по id."""
        response = self.api_context.get(f"/api/device/{device_id}/command/{command_id}", headers=self.headers)
        return response


    def update_device_command(self, device_id: int, command_id: int, **kwargs):
        """Метод для оновлення команди."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/device/{device_id}/command/{command_id}", data=data, headers=self.headers)
        return response


    def remove_device_command_by_id(self, device_id: int, command_id: int):
        """Метод для видалення команди по id."""
        response = self.api_context.delete(f"/api/device/{device_id}/command/{command_id}", headers=self.headers)
        return response


    def retrieve_a_list_of_device_commands(self, device_id: int):
        """Метод для отримання списку команд."""
        response = self.api_context.get(f"/api/device/{device_id}/commands", headers=self.headers)
        return response


    def create_command_for_device(self, device_id: int, **kwargs):
        """Метод для створення команди."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/device/{device_id}/commands", data=data, headers=self.headers)
        return response


    def dispatch_a_command_to_device(self, device_id: int, command_id: int):
        """Метод для відправлення команди на пристрій."""
        response = self.api_context.post(f"/api/device/{device_id}/command/{command_id}/dispatch", headers=self.headers)
        return response


    def retrieve_list_of_available_commands(self, device_id: int):
        """Метод для отримання списку доступних команд."""
        response = self.api_context.get(f"/api/device/{device_id}/commands/available", headers=self.headers)
        return response