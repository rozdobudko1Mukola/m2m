from playwright.sync_api import APIRequestContext, expect


class ExportPdfAPI:
    """Клас для роботи з API ExportPdf."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def export_report_template_to_pdf(self, templateId, **kwargs):
        """Експорт шаблону звіту в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/template/{templateId}/pdf", params=params, headers=self.headers)
        return response


    def export_report_for_geofence_devices_to_pdf(self, geofenceId, **kwargs):
        """Експорт звіту для пристроїв геозони в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/geofence/{geofenceId}/report/devices/pdf", params=params, headers=self.headers)
        return response


    def export_report_trips_for_device_to_pdf(self, deviceId, **kwargs):
        """Експорт звіту по поїздкам для пристрою в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/device/{deviceId}/trips/pdf", params=params, headers=self.headers)
        return response


    def export_summary_report_for_single_device_to_pdf(self, deviceId, **kwargs):
        """Експорт зведеного звіту для одного пристрою в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/device/{deviceId}/summary/pdf", params=params, headers=self.headers)
        return response


    def export_report_a_stops_for_device_to_pdf(self, deviceId, **kwargs):
        """Експорт звіту по зупинкам для пристрою в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/device/{deviceId}/stops/pdf", params=params, headers=self.headers)
        return response


    def export_report_on_the_device_entry_into_the_geofence_to_pdf(self, deviceId, **kwargs):
        """Експорт звіту по входу пристрою в геозону в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/device/{deviceId}/report/geofences/pdf", params=params, headers=self.headers)
        return response

    
    def export_report_trips_for_devices_group_to_pdf(self, groupId, **kwargs):
        """Експорт звіту по поїздкам для групи пристроїв в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/device/group/{groupId}/trips/pdf", params=params, headers=self.headers)
        return response


    def export_summary_report_for_devices_group_to_pdf(self, groupId, **kwargs):
        """Експорт зведеного звіту для групи пристроїв в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/device/group/{groupId}/summary/pdf", params=params, headers=self.headers)
        return response


    def export_report_a_stops_for_devices_group_to_pdf(self, groupId, **kwargs):
        """Експорт звіту по зупинкам для групи пристроїв в PDF."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/report/device/group/{groupId}/stops/pdf", params=params, headers=self.headers)
        return response


    def retrieve_latest_10_seconds_ago_devices_events(self):
        """Метод для отримання останніх подій пристроїв 10 секунд тому."""
        response = self.api_context.get("/api/events", headers=self.headers)
        return response