from playwright.sync_api import APIRequestContext

class AuthAPI:
    def __init__(self, api_context: APIRequestContext):
        self.api_context = api_context

    def login(self, email: str, password: str):
        """Авторизація через API."""
        data = {
            "email": email,
            "password": password
        }
        response = self.api_context.post("/api/login", data=data)
        return response

    def logout(self):
        """Вихід з системи через API."""
        response = self.api_context.post("/api/auth/logout")
        return response