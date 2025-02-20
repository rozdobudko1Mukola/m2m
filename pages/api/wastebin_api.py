from playwright.sync_api import APIRequestContext, expect

class WastebinAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def device_permanent_delete(self, wastebin_id: str):
        response = self.api_context.delete(f"/api/wastebin/device/{wastebin_id}", headers=self.headers)
        expect(response).to_be_ok()
        
        response = self.api_context.delete(f"/api/wastebin/deleted/device/{wastebin_id}/remove", headers=self.headers)
        return response