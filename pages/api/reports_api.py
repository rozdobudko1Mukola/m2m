from playwright.sync_api import APIRequestContext, expect


class ReportsAPI:
    """Клас для роботи з API звітів."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def export_report_template_to_excel(self, report_template_id: int, elementId: int, dateFrom: str, dateTo: str):
        """Метод для експорту шаблону звіту в Excel."""
        response = self.api_context.get(f"/api/report/template/{report_template_id}/xls?elementId={elementId}&dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def get_report_for_geofence_devices(self, geofence_id: int, dateFrom: str, dateTo: str):
        """Метод для отримання звіту по пристроях в геозоні."""
        response = self.api_context.get(f"/api/report/geofence/{geofence_id}/report/devices?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def export_report_for_geofence_devices_to_file(self, geofence_id, file_ext, dateFrom, dateTo):
        """Експортує список пристроїв з пагінацією в Excel."""
        response = self.api_context.get(f"api/report/geofence/{geofence_id}/report/devices/{file_ext}?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response

    
    def get_a_report_trips_for_device(self, device_id: int, dateFrom: str, dateTo: str):
        """Метод для отримання звіту про поїздки пристрою."""
        response = self.api_context.get(f"/api/report/device/{device_id}/trips?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response