from playwright.sync_api import APIRequestContext
from pages.e2e.base_page import BasePage
import random

class DeviceAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def unique_id(self):
        unique_id = ''.join(random.choices('0123456789', k=random.randint(5, 20)))
        return unique_id

    def create_new_device(self, **kwargs):
        """Створює новий пристрій через API."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
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


    def retrieve_admin_fields_for_device(self, device_id: str):
        """Отримує список пристроїв."""
        response = self.api_context.get(f"api/device/{device_id}/admin/fields", headers=self.headers)
        return response

    
    def update_admin_fields_for_device(self, device_id: str, adminFields: str):
        """Оновлює додаткові поля для пристрою."""
        data = {
            "adminFields": adminFields
        }
        response = self.api_context.put(f"api/device/{device_id}/admin/fields", data=data, headers=self.headers)
        return response


    def retrieve_list_of_devices_with_pagination(self, **kwargs):
        """Отримує список пристроїв з пагінацією."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/devices", params=data, headers=self.headers)
        return response


    def device_permissions_ids(self, device_id: str):
        """Отримує список ID дозволів для пристрою."""
        response = self.api_context.get(f"/api/permission/device/{device_id}/user/ids", headers=self.headers)
        return response

    
    def export_list_of_devices_with_pagination_excel(self, file_ext, **kwargs):
        """Експортує список пристроїв з пагінацією в Excel."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"api/devices/{file_ext}", params=data, headers=self.headers)
        return response


    def retrieve_device_permissions_for_child_user(self, user_id: str, device_id: str):
        """Отримує права користувача на пристрої."""
        response = self.api_context.get(f"api/permission/user/{user_id}/device/{device_id}", headers=self.headers)
        return response


    def set_device_permissions_for_child_user(self, user_id: str, device_id: str, **kwargs):
        """Встановлює права користувача на пристрої."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"api/permission/user/{user_id}/device/{device_id}", data=data, headers=self.headers)
        return response   
        

    def switch_all_device_permissions_for_child_user(self, user_id: str, device_id: str, state: str):
        """Встановлює права користувача на пристрої."""
        data = {
            "state": state
        }
        response = self.api_context.post(f"api/permission/user/{user_id}/device/{device_id}/switch", data=data, headers=self.headers)
        return response