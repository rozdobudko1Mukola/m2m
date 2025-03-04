from playwright.sync_api import APIRequestContext, expect


class AccountAPI:
    """Клас для роботи з API облікових записів."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def create_an_account_for_a_new_user(self, **kwargs):
        """Метод для створення облікового запису для нового користувача."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.post("/api/accounts/user/new", data=data, headers=self.headers)
        return response


    def create_an_account_from_existing_user(self, **kwargs):
        """Метод для створення облікового запису для існуючого користувача."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.post("/api/accounts/user/exist", data=data, headers=self.headers)
        return response


    def get_account_by_id(self, account_id: str):
        """Метод для отримання облікового запису по ID."""
        response = self.api_context.get(f"/api/account/{account_id}", headers=self.headers)
        return response

    
    def update_account_properties(self, account_id: str, **kwargs):
        """Метод для оновлення властивостей облікового запису."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.put(f"/api/account/{account_id}", data=data, headers=self.headers)
        return response

    
    def update_account_state(self, account_id: str, enabled: bool):
        """Метод для оновлення стану облікового запису."""
        data = {
            "enabled": enabled
        }
        response = self.api_context.put(f"/api/account/{account_id}/state", data=data, headers=self.headers)
        return response


    def get_a_billing_plan_for_a_child_account(self, account_id: str):
        """Метод для отримання плану для дочірнього облікового запису."""
        response = self.api_context.get(f"/api/account/{account_id}/plan", headers=self.headers)
        return response


    def update_billing_plan_for_child_account(self, account_id: str, **kwargs):
        """Метод для оновлення плану для дочірнього облікового запису."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.put(f"/api/account/{account_id}/plan", data=data, headers=self.headers)
        return response


    def get_a_billing_plan_discount_for_a_child_account(self, account_id: str):
        """Метод для отримання знижки на план для дочірнього облікового запису."""
        response = self.api_context.get(f"/api/account/{account_id}/plan/discount", headers=self.headers)
        return response


    def make_payment_on_account(self, account_id: str, **kwargs):
        """Метод для проведення платежу на обліковий запис."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.put(f"/api/account/{account_id}/payment", data=data, headers=self.headers)
        return response


    # export to file metods

    def export_a_list_of_accounts_with_pagination_to_file(self, file_ext, **kwargs):
        """Метод для експорту списку облікових записів з пагінацією в файл."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.get(f"/api/accounts/{file_ext}", params=data, headers=self.headers, timeout=90000)
        return response


    def export_payment_statistics_for_child_account_to_file(self, file_ext, account_id, **kwargs):
        """Метод для експорту статистики платежів для дочірнього облікового запису в файл."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.get(f"/api/account/{account_id}/statistics/payment/{file_ext}", params=data, headers=self.headers)
        return response


    def export_device_statistics_for_child_account_to_file(self, file_ext, account_id, **kwargs):
        """Метод для експорту статистики пристроїв для дочірнього облікового запису в файл."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.get(f"/api/account/{account_id}/statistics/devices/{file_ext}", params=data, headers=self.headers)
        return response


    def export_payment_statistics_to_file(self, file_ext, **kwargs):
        """Метод для експорту статистики платежів в файл."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.get(f"/api/account/statistics/payment/{file_ext}", params=data, headers=self.headers)
        return response


    def export_device_statistics_to_file(self, file_ext, **kwargs):
        """Метод для експорту статистики пристроїв в файл."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.get(f"/api/account/statistics/devices/{file_ext}", params=data, headers=self.headers)
        return response