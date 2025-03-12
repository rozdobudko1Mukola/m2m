from playwright.sync_api import APIRequestContext


class DeviceTransferAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def transfer_devices_to_account(self, **kwargs):
        """Передає пристрої на інший акаунт."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post("/api/devices/transfer", data=data, headers=self.headers)
        return response


    def retrieve_a_paginated_devices_not_in_account(self, account_id, **kwargs):
        """Отримує список пристроїв, які не належать аккаунту."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/devices/notin/account/{account_id}", params=params, headers=self.headers)
        return response


    def retrieve_a_paginated_devices_in_account(self, account_id, **kwargs):
        """Отримує список пристроїв, які належать аккаунту."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/devices/in/account/{account_id}", params=params, headers=self.headers)
        return response