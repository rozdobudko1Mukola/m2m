from playwright.sync_api import APIRequestContext, expect

class WastebinAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def move_device_to_wastebin(self, device_id: str):
        response = self.api_context.delete(f"/api/wastebin/device/{device_id}", headers=self.headers)
        return response

    def device_permanent_delete(self, device_id: str):
        response = self.api_context.delete(f"/api/wastebin/deleted/device/{device_id}/remove", headers=self.headers)
        return response


    def unpause_device(self, device_id: str):
        response = self.api_context.post(f"/api/wastebin/restore/device/{device_id}", headers=self.headers)
        return response


    def restore_the_device_from_wastebin(self, device_id: str):
        response = self.api_context.post(f"/api/wastebin/deleted/device/{device_id}/restore", headers=self.headers)
        return response

    
    def retrieve_a_list_of_paused_devices_with_pagination(self, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"api/wastebin/devices",params=data, headers=self.headers)
        return response


    def export_list_of_devices_with_pagination_to_file(self, file_ext, **kwargs):
        """Експортує список пристроїв з пагінацією в Excel."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"api/wastebin/devices/{file_ext}", params=data, headers=self.headers)
        return response


    def retrieve_list_of_deleted_devices_with_pagination(self, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"api/wastebin/deleted/devices", params=data, headers=self.headers)
        return response