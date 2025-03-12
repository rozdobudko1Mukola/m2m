from playwright.sync_api import APIRequestContext


class GoolgeServerKeys:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def get_google_server_api_key_by_id(self, key_id):
        """Отримує ключ API Google Server за ID."""
        response = self.api_context.get(f"/api/google/key/{key_id}", headers=self.headers)
        return response


    def update_google_server_api_key_by_id(self, key_id, key):
        """Оновлює ключ API Google Server за ID."""
        data = {
            "key": key
        }
        response = self.api_context.put(f"/api/google/key/{key_id}", data=data, headers=self.headers)
        return response


    def remove_google_server_api_key_by_id(self, key_id):
        """Видаляє ключ API Google Server за ID."""
        response = self.api_context.delete(f"/api/google/key/{key_id}", headers=self.headers)
        return response


    def retrieve_list_of_all_google_server_api_keys(self):
        """Отримує список всіх ключів API Google Server."""
        response = self.api_context.get("/api/google/key", headers=self.headers)
        return response


    def add_new_google_server_api_key(self, key):
        """Додає новий ключ API Google Server."""
        data = {
            "key": key
        }
        response = self.api_context.post("/api/google/keys", data=data, headers=self.headers)
        return response


    def get_actual_server_google_key_for_maps(self):
        """Отримує актуальний ключ Google Server для карти."""
        response = self.api_context.get("/api/google/key", headers=self.headers)
        return response