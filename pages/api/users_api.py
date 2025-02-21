from playwright.sync_api import APIRequestContext

class UsersAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def create_new_user(self, **kwargs):
        """Створює нового користувача через API."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post("/api/users", data=data, headers=self.headers)
        return response


    def remove_child_user(self, user_id: str):
        """Видаляє дитячого користувача."""
        response = self.api_context.delete(f"/api/user/{user_id}", headers=self.headers)
        return response