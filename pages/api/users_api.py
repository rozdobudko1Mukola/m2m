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


    def get_child_user_by_id(self, user_id: str):
        """Отримує дитячого користувача по id."""
        response = self.api_context.get(f"/api/user/{user_id}", headers=self.headers)
        return response


    def update_child_user(self, user_id: str, **kwargs):
        """Оновлює дитячого користувача."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/user/{user_id}", data=data, headers=self.headers)
        return response


    def retrieve_list_of_child_users_without_pagination(self):
        """Отримує список дитячих користувачів без пагінації."""
        response = self.api_context.get(f"/api/users", headers=self.headers)
        return response


    def change_the_child_user_password(self, user_id: str, password: str):
        """Змінює пароль дитячого користувача."""
        response = self.api_context.post(f"/api/user/{user_id}/password/change", data={"newPassword": password}, headers=self.headers)
        return response


    def send_invite(self, user_id: str):
        """Відправляє запрошення користувачу."""
        response = self.api_context.post(f"api/user/{user_id}/invite", headers=self.headers)
        return response


    def change_email(self, user_id: str, email: str):
        """Змінює email користувача."""
        data={
            "newEmail": email
            }
        response = self.api_context.post(f"/api/user/{user_id}/email/change", data=data, headers=self.headers)
        return response


    def get_child_user_permissions_for_another_child(self, user_id: str, managed_id: str):
        """Отримує права дитячого користувача для іншого дитячого користувача."""
        response = self.api_context.get(f"/api/permission/user/{user_id}/managed/{managed_id}", headers=self.headers)
        return response


    def grant_permissions_to_child_user_for_another_child(self, user_id: str, managed_id: str, **kwargs):
        """Надає права дитячому користувачу для іншого дитячого користувача."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/permission/user/{user_id}/managed/{managed_id}", data=data, headers=self.headers)
        return response


    def retrieve_list_of_child_users_with_pagination(self, page: int, per_page: int, query: str = None):
        """Отримує список дитячих користувачів з пагінацією."""
        params={
            "page": page, 
            "perPage": per_page, 
            "query": query
            }
        response = self.api_context.get(f"/api/users/paginated", params=params, headers=self.headers)
        return response
