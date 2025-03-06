from playwright.sync_api import APIRequestContext, expect


class ManagersAPI:
    """Клас для роботи з API ManagersAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def create_new_account_manager(self, **kwargs):
        """Метод для створення нового акаунт менеджера."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/managers", data=data, headers=self.headers)
        return response


    def delete_account_manager(self, manager_id: str):
        """Метод для видалення акаунт менеджера."""
        response = self.api_context.delete(f"/api/manager/{manager_id}", headers=self.headers)
        return response


    def get_account_manager_by_id(self, manager_id: str):
        """Метод для отримання акаунт менеджера по ID."""
        response = self.api_context.get(f"/api/manager/{manager_id}", headers=self.headers)
        return response


    def update_account_manager_by_id(self, manager_id: str, **kwargs):
        """Метод для оновлення акаунт менеджера по ID."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/manager/{manager_id}", data=data, headers=self.headers)
        return response


    def retrieve_account_managers(self, **kwargs):
        """Метод для отримання списку акаунт менеджерів з пагінацією."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get("/api/managers", params=params, headers=self.headers)
        return response


    def set_account_to_manager(self, manager_id: str, account_id: str):
        """Метод для призначення акаунту менеджера."""
        response = self.api_context.post(f"/api/manager/{manager_id}/account/{account_id}/assign", headers=self.headers)
        return response


    def send_request_to_manager(self, massage: str):
        """Метод для відправлення запиту менеджеру."""
        data = {
            "message": massage
        }
        response = self.api_context.post(f"/api/manager/request", data=data, headers=self.headers)
        return response


    def remove_link_from_account_to_manager(self, account_id: str):
        """Метод для видалення зв'язку акаунту менеджера."""
        response = self.api_context.delete(f"/api/manager/account/{account_id}/reset", headers=self.headers)
        return response