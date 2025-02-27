from playwright.sync_api import APIRequestContext, expect


class DeviceGroupsAPI:
    """Клас для роботи з API груп пристроїв."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def create_new_device_group(self, **kwargs):
        """Метод для створення нової групи пристроїв."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post("/api/device/groups", data=data, headers=self.headers)
        return response


    def remove_device_group(self, device_group_id: int):
        """Метод для видалення групи пристроїв."""
        response = self.api_context.delete(f"/api/device/group/{device_group_id}", headers=self.headers)
        return response


    def retrieve_devices_group_related_permissions(self, device_group_id: int):
        """Метод для отримання прав доступу до групи пристроїв."""
        response = self.api_context.get(f"/api/permissions/device/group/{device_group_id}", headers=self.headers)
        return response


    def update_devices_group_related_permissions(self, device_group_id: int, **kwargs):
        """Метод для оновлення прав доступу до групи пристроїв."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/permissions/device/group/{device_group_id}", data=data, headers=self.headers)
        return response


    def rename_devices_group(self, device_group_id: int, name: str):
        """Метод для зміни назви групи пристроїв."""
        data = {
            "name": name
        }
        response = self.api_context.put(f"/api/device/group/{device_group_id}/rename", data=data, headers=self.headers)
        return response

    
    def retrieve_custom_fields_for_devices_group(self, device_group_id: int):
        """Метод для отримання додаткових полів для групи пристроїв."""
        response = self.api_context.get(f"/api/device/group/{device_group_id}/custom/fields", headers=self.headers)
        return response


    def retrieve_admin_fields_for_devices_group(self, device_group_id: int):
        """Метод для отримання адміністративних полів для групи пристроїв."""
        response = self.api_context.get(f"/api/device/group/{device_group_id}/admin/fields", headers=self.headers)
        return response


    def update_devices_group_custom_fields(self, device_group_id: int, customFields: str):
        """Метод для оновлення додаткових полів для групи пристроїв."""
        data = {
        "customFields": customFields
        }
        response = self.api_context.put(f"/api/device/group/{device_group_id}/custom/fields", data=data, headers=self.headers)
        return response


    def update_devices_group_admin_fields(self, device_group_id: int, adminFields: str):
        """Метод для оновлення адміністративних полів для групи пристроїв."""
        data = {
        "adminFields": adminFields
        }
        response = self.api_context.put(f"/api/device/group/{device_group_id}/admin/fields", data=data, headers=self.headers)
        return response


    def add_device_to_group(self, device_group_id: int, device_id: int):
        """Метод для додавання пристрою до групи."""
        response = self.api_context.post(f"/api/group/{device_group_id}/device/{device_id}/add", headers=self.headers)
        return response


    def retrieve_a_list_of_devices_groups_with_pagination(self, page: int, per_page: int):
        """Метод для отримання списку груп пристроїв з пагінацією."""
        param = {
            "page": page,
            "perPage": per_page
        }
        response = self.api_context.get("/api/device/groups", params=param, headers=self.headers)
        return response


    def retrieve_a_list_of_device_from_group(self, device_group_id: int):
        """Метод для отримання списку пристроїв з групи."""
        response = self.api_context.get(f"/api/group/{device_group_id}/devices", headers=self.headers)
        return response


    def get_devices_group_by_id(self, device_group_id: int):
        """Метод для отримання групи пристроїв по id."""
        response = self.api_context.get(f"/api/device/group/{device_group_id}", headers=self.headers)
        return response


    def remove_device_from_group(self, device_group_id: int, device_id: int):
        """Метод для видалення пристрою з групи."""
        response = self.api_context.delete(f"/api/group/{device_group_id}/device/{device_id}/remove", headers=self.headers)
        return response


    def retrieve_devices_group_permissions_for_child_user(self, device_group_id: int, user_id: int):
        """Метод для отримання прав доступу до групи пристроїв для дитячого користувача."""
        response = self.api_context.get(f"/api/permission/user/{user_id}/device/group/{device_group_id}", headers=self.headers)
        return response


    def set_devices_group_permission_for_child_user(self, device_group_id: int, user_id: int, **kwargs):
        """Метод для встановлення прав доступу до групи пристроїв для дитячого користувача."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/permission/user/{user_id}/device/group/{device_group_id}", data=data, headers=self.headers)
        return response