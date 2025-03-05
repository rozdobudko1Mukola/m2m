from playwright.sync_api import APIRequestContext, expect


class SimCardAPI:
    """Клас для роботи з API SimCardAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def create_new_simcard(self, **kwargs):
        """Метод для створення нової SIM-карти."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/simcards", data=data, headers=self.headers)
        return response


    def remove_the_simcard(self, simcard_id: str):
        """Метод для видалення SIM-карти."""
        response = self.api_context.delete(f"/api/simcard/{simcard_id}", headers=self.headers)
        return response


    def get_simcard_by_id(self, simcard_id: str):
        """Метод для отримання SIM-карти по ID."""
        response = self.api_context.get(f"/api/simcard/{simcard_id}", headers=self.headers)
        return response


    def update_simcard_properties(self, simcard_id: str, **kwargs):
        """Метод для оновлення властивостей SIM-карти."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/simcard/{simcard_id}", data=data, headers=self.headers)
        return response


    def retrieve_a_list_of_simcards_with_pagination(self, **kwargs):
        """Метод для отримання списку SIM-карт з пагінацією."""
        response = self.api_context.get(f"/api/simcards", params=kwargs, headers=self.headers)
        return response

    
    def assign_device_to_simcard(self, simcard_id: str, device_id: str):
        """Метод для призначення пристрою до SIM-карти."""
        data = {
            "deviceId": device_id
        }
        response = self.api_context.post(f"/api/simcard/{simcard_id}/device/assign", data=data, headers=self.headers)
        return response


    def assign_account_to_simcard(self, simcard_id: str, account_id: str):
        """Метод для призначення акаунта до SIM-карти."""
        data = {
            "accountId": account_id
        }
        response = self.api_context.post(f"/api/simcard/{simcard_id}/account/assign", data=data, headers=self.headers)
        return response


    def export_a_list_of_simcards_with_pagination_to_file(self, file_ext, **kwargs):
        """Метод для експорту списку SIM-карт з пагінацією в xls."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/simcards/{file_ext}", params=params, headers=self.headers)
        return response


    def get_child_account_simcard_statistics(self, account_id: str, **kwargs):
        """Метод для отримання статистики SIM-карти по дитячому акаунту."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/account/{account_id}/simcard/statistics", params=params, headers=self.headers)
        return response


    def export_simcard_statistics_for_child_account_to_file(self, account_id: str, file_ext, **kwargs):
        """Метод для експорту статистики SIM-карти по дитячому акаунту в файл."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/account/{account_id}/simcard/statistics/{file_ext}", params=params, headers=self.headers)
        return response


    def get_auth_account_simcard_statistics(self, **kwargs):
        """Метод для отримання статистики SIM-карти по авторизованому акаунту."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/account/simcard/statistics", params=params, headers=self.headers)
        return response


    def export_simcard_statistics_to_file(self, file_ext, **kwargs):
        """Метод для експорту статистики SIM-карти по авторизованому акаунту в файл."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/account/simcard/statistics/{file_ext}", params=params, headers=self.headers)
        return response