from playwright.sync_api import APIRequestContext

class AuthAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def get_profile(self):
        """Метод для отримання профілю користувача."""
        response = self.api_context.get("/api/profile", headers=self.headers)
        return response

    
    def update_profile(self, **kwargs):
        """Метод для оновлення профілю користувача."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put("/api/profile", data=data, headers=self.headers)
        return response


    def login_as_child_user(self, user_id):
        """Метод для входу як дитина."""
        response = self.api_context.post(f"/api/user/{user_id}/login", headers=self.headers)
        return response


    def verify_access_token(self):
        """Метод для перевірки доступу."""
        response = self.api_context.post("/api/token/verify", headers=self.headers)
        return response


    def refresh_access_token(self, refreshToken):
        """Метод для оновлення доступу."""
        data = {
            "refreshToken": refreshToken
        }
        response = self.api_context.post("/api/token/refresh", data=data)
        return response


    def send_an_email_to_reset_password(self, resetEmail):
        """Метод для відправлення листа для скидання пароля."""
        data = {
            "resetEmail": resetEmail
        }
        response = self.api_context.post("/api/reset/password", data=data)
        return response


    def password_reset_confirmation(self, token, newPassword):
        """Метод для підтвердження скидання пароля."""
        data = {
            "token": token,
            "newPassword": newPassword
        }
        response = self.api_context.post("/api/reset/password/confirm", data=data)
        return response


    def sign_up(self, email: str, password: str, language: str):
        """Метод для реєстрації."""
        data = {
            "email": email,
            "password": password,
            "language": language
            
        }
        response = self.api_context.post("/api/register", data=data)
        return response


    def activate_user_after_registration(self, token):
        """Метод для активації користувача після реєстрації."""
        data = {
            "token": token
        }
        response = self.api_context.post(f"/api/register/activate", data=data)
        return response

    
    def refresh_confirmation_link(self, email):
        """Метод для оновлення посилання підтвердження."""
        data = {
            "email": email
        }
        response = self.api_context.post("/api/register/activate/refresh", data=data)
        return response


    def change_password(self, oldPassword, newPassword):
        """Метод для зміни пароля."""
        data = {
            "oldPassword": oldPassword,
            "newPassword": newPassword
        }
        response = self.api_context.post("/api/profile/password/change", data=data, headers=self.headers)
        return response


    def send_email_to_change_email_address(self, newEmail):
        """Метод для відправлення листа для зміни адреси електронної пошти."""
        data = {
            "newEmail": newEmail
        }
        response = self.api_context.post("/api/profile/email/change", data=data, headers=self.headers)
        return response


    def confirmation_of_change_email(self, token):
        """Метод для підтвердження зміни адреси електронної пошти."""
        data = {
            "token": token
        }
        response = self.api_context.post("/api/profile/email/change/confirm", data=data, headers=self.headers)
        return response


    def sign_in(self, email, password):
        """Метод для входу."""
        data = {
            "email": email,
            "password": password
        }
        response = self.api_context.post("/api/login", data=data)
        return response