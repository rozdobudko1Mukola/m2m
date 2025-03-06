from playwright.sync_api import APIRequestContext, expect


class SimCardGroupAPI:
    """Клас для роботи з API SimCardGroupAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def create_new_simcard_group(self, **kwargs):
        """Метод для створення нової групи SIM-карти."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/simcard/groups", data=data, headers=self.headers)
        return response


    def remove_simcard_group(self, simcard_group_id: str):
        """Метод для видалення групи SIM-карт."""
        response = self.api_context.delete(f"/api/simcard/group/{simcard_group_id}", headers=self.headers)
        return response


    def get_simcard_group_by_id(self, simcard_group_id: str):
        """Метод для отримання групи SIM-карт по ID."""
        response = self.api_context.get(f"/api/simcard/group/{simcard_group_id}", headers=self.headers)
        return response


    def update_simcard_group_properties(self, simcard_group_id: str, **kwargs):
        """Метод для оновлення властивостей групи SIM-карт."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/simcard/group/{simcard_group_id}", data=data, headers=self.headers)
        return response


    def retrieve_a_list_of_simcard_groups_with_pagination(self, **kwargs):
        """Метод для отримання списку груп SIM-карт з пагінацією."""
        response = self.api_context.get("/api/simcard/groups", params=kwargs, headers=self.headers)
        return response


    def add_simcard_to_group(self, simcard_group_id: str, simcard_id: str):
        """Метод для додавання SIM-карти до групи."""
        response = self.api_context.post(f"/api/simcard/group/{simcard_group_id}/card/{simcard_id}", headers=self.headers)
        return response


    def remove_simcard_from_group(self, simcard_group_id: str, simcard_id: str):
        """Метод для видалення SIM-карти з групи."""
        response = self.api_context.delete(f"/api/simcard/group/{simcard_group_id}/card/{simcard_id}", headers=self.headers)
        return response


    def retrieve_a_list_of_simcards_from_group(self, simcard_group_id: str):
        """Метод для отримання списку SIM-карт з групи."""
        response = self.api_context.get(f"/api/simcard/group/{simcard_group_id}/cards", headers=self.headers)
        return response