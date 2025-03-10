from playwright.sync_api import APIRequestContext, expect


class GeofenceGroupsAPI:
    """Клас для роботи з API CompaniesAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def rename_geofences_group(self, group_id: int, new_name: str):
        """Перейменування групи геозон."""
        data = {
            "name": new_name
        }
        response = self.api_context.put(f"/api/geofence/group/{group_id}/rename", data=data, headers=self.headers)
        return response


    def retrieve_custom_fields_for_geofences_group(self, group_id: int):
        """Отримання додаткових полів для геозон."""
        response = self.api_context.get(f"/api/geofence/group/{group_id}/custom/fields", headers=self.headers)
        return response


    def update_geofences_group_custom_fields(self, group_id: int, custom_fields: dict):
        """Оновлення додаткових полів для геозон."""
        data = {
            "customFields": custom_fields
        }
        response = self.api_context.put(f"/api/geofence/group/{group_id}/custom/fields", data=data, headers=self.headers)
        return response

    
    def retrieve_admin_fields_for_geofences_group(self, group_id: int):
        """Отримання адміністративних полів для геозон."""
        response = self.api_context.get(f"/api/geofence/group/{group_id}/admin/fields", headers=self.headers)
        return response


    def update_geofences_group_admin_fields(self, group_id: int, admin_fields: dict):
        """Оновлення адміністративних полів для геозон."""
        data = {
            "adminFields": admin_fields
        }
        response = self.api_context.put(f"/api/geofence/group/{group_id}/admin/fields", data=data, headers=self.headers)
        return response


    def retrieve_geofences_group_permissions_for_child_user(self, group_id: int, child_user_id: int):
        """Отримання прав доступу до геозон для дочірнього користувача."""
        response = self.api_context.get(f"/api/permission/user/{child_user_id}/geofence/group/{group_id}", headers=self.headers)
        return response


    def set_geofences_group_permission_for_child_user(self, group_id: int, child_user_id: int, **kwargs):
        """Встановлення прав доступу до геозон для дочірнього користувача."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/permission/user/{child_user_id}/geofence/group/{group_id}", data=data, headers=self.headers)
        return response


    def add_geofence_to_group(self, group_id: int, geofence_id: int):
        """Додавання геозони до групи."""
        response = self.api_context.post(f"/api/group/{group_id}/geofence/{geofence_id}/add", headers=self.headers)
        return response


    def retrieve_a_list_of_geofences_groups_with_pagination(self, **kwargs):
        """Отримання списку груп геозон з пагінацією."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get("/api/geofence/groups", params=params, headers=self.headers)
        return response


    def create_new_geofences_group(self, **kwargs):
        """Створення нової групи геозон."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post("/api/geofence/groups", data=data, headers=self.headers)
        return response


    def retrieve_a_list_of_geofences_from_group(self, group_id: int):
        """Отримання списку геозон з групи."""
        response = self.api_context.get(f"/api/group/{group_id}/geofences", headers=self.headers)
        return response


    def get_geofences_group_by_id(self, group_id: int):
        """Отримання групи геозон по ID."""
        response = self.api_context.get(f"/api/geofence/group/{group_id}", headers=self.headers)
        return response


    def remove_the_geofences_group(self, group_id: int):
        """Видалення групи геозон."""
        response = self.api_context.delete(f"/api/geofence/group/{group_id}", headers=self.headers)
        return response


    def remove_geofence_from_group(self, group_id: int, geofence_id: int):
        """Видалення геозони з групи."""
        response = self.api_context.delete(f"/api/group/{group_id}/geofence/{geofence_id}/remove", headers=self.headers)
        return response