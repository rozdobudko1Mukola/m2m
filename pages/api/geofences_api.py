from playwright.sync_api import APIRequestContext, expect


class GeofencesAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def create_new_geofence(self, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post("/api/geofences", data=data, headers=self.headers)
        return response


    def remove_the_geofence(self, geofence_id: int):
        response = self.api_context.delete(f"/api/geofence/{geofence_id}", headers=self.headers)
        return response


    def get_geofence_by_id(self, geofence_id: int):
        response = self.api_context.get(f"/api/geofence/{geofence_id}", headers=self.headers)
        return response


    def update_geofence_properties(self, geofence_id: int, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/geofence/{geofence_id}", data=data, headers=self.headers)
        return response


    def rename_geofence(self, geofence_id: int, name: str):
        data = {
            "name": name
        }
        response = self.api_context.put(f"/api/geofence/{geofence_id}/rename", data=data, headers=self.headers)
        return response


    def retrieve_list_of_geofences_with_pagination(self, **kwargs):
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get("/api/geofences", params=params, headers=self.headers)
        return response


    def list_geofences_by_selected_ids(self, geofenceIds: list):
        data = {
            "geofenceIds": geofenceIds
        }
        response = self.api_context.post("/api/geofences/batch", data=data, headers=self.headers)
        return response


    def assign_device_to_geofence(self, geofence_id: int, device_id: int):
        response = self.api_context.post(f"/api/geofence/{geofence_id}/device/{device_id}", headers=self.headers)
        return response


    def remove_device_from_geofence(self, geofence_id: int, device_id: int):
        response = self.api_context.delete(f"/api/geofence/{geofence_id}/device/{device_id}", headers=self.headers)
        return response


    def list_assigned_geofence_device(self, geofence_id: int):
        response = self.api_context.get(f"/api/geofence/{geofence_id}/devices", headers=self.headers)
        return response


    def create_copy_of_geofence(self, geofence_id: int):
        response = self.api_context.post(f"/api/geofence/{geofence_id}/copy", headers=self.headers)
        return response


    def retrieve_geofence_permissions_for_child_user(self, geofence_id: int, user_id: int):
        response = self.api_context.get(f"/api/permission/user/{user_id}/geofence/{geofence_id}", headers=self.headers)
        return response


    def set_geofence_permissions_for_child_user(self, geofence_id: int, user_id: int, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/permission/user/{user_id}/geofence/{geofence_id}", data=data, headers=self.headers)
        return response
