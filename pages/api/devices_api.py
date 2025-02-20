from playwright.sync_api import APIRequestContext
from pages.api.auth_api import AuthAPI
from pages.base_page import BasePage
import random

class DeviceAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def unique_id(self):
        unique_id = ''.join(random.choices('0123456789', k=random.randint(5, 20)))
        return unique_id

    def create_new_device(self, dev_type: str, name: str, unique_id: str, phone: str):
        """Створює новий пристрій через API."""
        data = {
            "type": dev_type,
            "customFields": "",
            "adminFields": "",
            "name": name,
            "uniqueId": unique_id,
            "phone": phone,
            "phone2": "123456",
            "phoneTracker": True
        }
        response = self.api_context.post("/api/devices", data=data, headers=self.headers)
        return response


    def move_device_to_pause(self, device_id: str):
        """Переміщає пристрій в корзину."""
        response = self.api_context.delete(f"/api/device/{device_id}", headers=self.headers)
        return response


    def update_devise_characteristic(self, device_id: str, **kwargs):
        """Оновлює характеристики пристрою."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/device/{device_id}", data=data, headers=self.headers)
        return response


    def get_device_by_id(self, device_id: str):
        """Отримує пристрій по ID."""
        response = self.api_context.get(f"/api/device/{device_id}", headers=self.headers)
        return response


    def rename_device(self, device_id: str, name: str):
        """Перейменовує пристрій."""
        data = {
            "name": name
        }
        response = self.api_context.put(f"/api/device/{device_id}/rename", data=data, headers=self.headers)
        return response

    
    def get_motion_detector_settings_for_device(self, device_id: str):
        """Отримує список пристроїв."""
        response = self.api_context.get(f"api/device/{device_id}/motion/detector", headers=self.headers)
        return response


    def change_motion_detector_settings_for_device(self, device_id: str, **kwargs):
        """Змінює налаштування детектора руху."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"api/device/{device_id}/motion/detector", data=data, headers=self.headers)
        return response

    
    def retrieve_custom_fields_for_device(self, device_id: str):
        """Отримує список пристроїв."""
        response = self.api_context.get(f"api/device/{device_id}/custom/fields", headers=self.headers)
        return response

    
    def update_custom_fields_for_device(self, device_id: str, customFields: str):
        """Оновлює додаткові поля для пристрою."""
        data = {
            "customFields": customFields
        }
        response = self.api_context.put(f"api/device/{device_id}/custom/fields", data=data, headers=self.headers)
        return response


    def get_connection_parameters(self, device_id: str):
        """Отримує параметри підключення."""
        response = self.api_context.get(f"api/device/{device_id}/connection", headers=self.headers)
        return response

    
    def update_connection_parameters(self, device_id: str, **kwargs):
        """Оновлює параметри підключення."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"api/device/{device_id}/connection", data=data, headers=self.headers)
        return response