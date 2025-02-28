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


    def export_report_trips_for_device_to_file(self, device_id: int, file_ext: str, dateFrom: str, dateTo: str):
        """Метод для експорту звіту про поїздки пристрою в файл."""
        response = self.api_context.get(f"/api/report/device/{device_id}/trips/{file_ext}?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def get_a_summary_report_for_single_device(self, device_id: int, dateFrom: str, dateTo: str):
        """Метод для отримання зведеного звіту по пристрою."""
        response = self.api_context.get(f"/api/report/device/{device_id}/summary?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def export_summary_report_for_single_device_to_file(self, device_id: int, file_ext: str, dateFrom: str, dateTo: str):
        """Метод для експорту зведеного звіту по пристрою в файл."""
        response = self.api_context.get(f"/api/report/device/{device_id}/summary/{file_ext}?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def get_a_report_on_device_stops(self, device_id: int, dateFrom: str, dateTo: str):
        """Метод для отримання звіту про зупинки пристрою."""
        response = self.api_context.get(f"/api/report/device/{device_id}/stops?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def export_report_on_device_stops_to_file(self, device_id: int, file_ext: str, dateFrom: str, dateTo: str):
        """Метод для експорту звіту про зупинки пристрою в файл."""
        response = self.api_context.get(f"/api/report/device/{device_id}/stops/{file_ext}?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def get_a_report_on_the_device_entry_into_the_geofence(self, device_id: int, dateFrom: str, dateTo: str):
        """Метод для отримання звіту про в'їзд пристрою в геозону."""
        response = self.api_context.get(f"/api/report/device/{device_id}/report/geofences?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def export_report_on_the_device_entry_into_the_geofence_to_file(self, device_id: int, file_ext: str, dateFrom: str, dateTo: str):
        """Метод для експорту звіту про в'їзд пристрою в геозону в файл."""
        response = self.api_context.get(f"/api/report/device/{device_id}/report/geofences/{file_ext}?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def get_a_report_trips_for_devices_group(self, devices_group_id: int, dateFrom: str, dateTo: str):
        """Метод для отримання звіту про поїздки групи пристроїв."""
        response = self.api_context.get(f"/api/report/device/group/{devices_group_id}/trips?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def export_report_trips_for_devices_group_to_file(self, devices_group_id: int, file_ext: str, dateFrom: str, dateTo: str):
        """Метод для експорту звіту про поїздки групи пристроїв в файл."""
        response = self.api_context.get(f"/api/report/device/group/{devices_group_id}/trips/{file_ext}?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def get_a_summary_report_for_devices_group(self, devices_group_id: int, dateFrom: str, dateTo: str):
        """Метод для отримання зведеного звіту по групі пристроїв."""
        response = self.api_context.get(f"/api/report/device/group/{devices_group_id}/summary?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def export_summary_report_for_devices_group_to_file(self, devices_group_id: int, file_ext: str, dateFrom: str, dateTo: str):
        """Метод для експорту зведеного звіту по групі пристроїв в файл."""
        response = self.api_context.get(f"/api/report/device/group/{devices_group_id}/summary/{file_ext}?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def get_report_of_stops_for_devices_group(self, devices_group_id: int, dateFrom: str, dateTo: str):
        """Метод для отримання звіту про зупинки групи пристроїв."""
        response = self.api_context.get(f"/api/report/device/group/{devices_group_id}/stops?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def export_report_of_stops_for_devices_group_to_file(self, devices_group_id: int, file_ext: str, dateFrom: str, dateTo: str):
        """Метод для експорту звіту про зупинки групи пристроїв в файл."""
        response = self.api_context.get(f"/api/report/device/group/{devices_group_id}/stops/{file_ext}?dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response