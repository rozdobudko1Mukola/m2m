from playwright.sync_api import APIRequestContext, expect


class SensorsAPI:
    """Клас для роботи з API CompaniesAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def get_sensor_by_id(self, device_id: int, sensor_id: int):
        """Отримання даних про датчик по його ID."""
        response = self.api_context.get(f"/api/device/{device_id}/sensors/{sensor_id}", headers=self.headers)
        return response


    def update_sensor_properties(self, device_id: int, sensor_id: int, **kwargs):
        """Оновлення властивостей датчика."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/device/{device_id}/sensors/{sensor_id}", data=data, headers=self.headers)
        return response


    def remove_the_sensor(self, device_id: int, sensor_id: int):
        """Видалення датчика."""
        response = self.api_context.delete(f"/api/device/{device_id}/sensors/{sensor_id}", headers=self.headers)
        return response


    def update_computation_table_data_X_Y_pairs(self, device_id: int, sensor_id: int, pairs: list):
        """Оновлення або зміна даних таблиці обчислень X-Y пар."""
        response = self.api_context.put(f"/api/device/{device_id}/sensors/{sensor_id}/table/pairs", data=pairs, headers=self.headers)
        return response


    def update_computation_table_approximation_coefficients_and_min_max_value(self, device_id: int, sensor_id: int, **kwargs):
        """Оновлення або зміна коефіцієнтів апроксимації та minValue або maxValue."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/device/{device_id}/sensors/{sensor_id}/table/coeffs", data=data, headers=self.headers)
        return response


    def get_sensor_additional_properties(self, device_id: int, sensor_id: int):
        """Отримання додаткових властивостей датчика."""
        response = self.api_context.get(f"/api/device/{device_id}/sensors/{sensor_id}/additional", headers=self.headers)
        return response


    def update_sensor_additional_properties(self, device_id: int, sensor_id: int, **kwargs):
        """Оновлення додаткових властивостей датчика."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/device/{device_id}/sensors/{sensor_id}/additional", data=data, headers=self.headers)
        return response


    def retrieve_a_list_of_sensors(self, device_id: int):
        """Отримання списку датчиків."""
        response = self.api_context.get(f"/api/device/{device_id}/sensors", headers=self.headers)
        return response


    def create_new_sensor(self, device_id: int, **kwargs):
        """Створення нового датчика."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"/api/device/{device_id}/sensors", data=data, headers=self.headers)
        return response


    def import_computation_table_data_X_Y_pairs_from_CSV(self, device_id: int, sensor_id: int, file):
        """Імпорт даних таблиці обчислень X-Y пар з CSV файлу."""
        response = self.api_context.post(f"/api/device/{device_id}/sensors/{sensor_id}/table/pairs/import", data=file, headers=self.headers)
        return response


    def calculate_computation_table_coefficients(self, device_id: int, sensor_id: int):
        """Розрахунок коефіцієнтів апроксимації."""
        response = self.api_context.post(f"/api/device/{device_id}/sensors/{sensor_id}/table/calc", headers=self.headers)
        return response


    def delete_multiple_sensors_by_ids(self, device_id: int, sensor_ids: list):
        """Видалення декількох датчиків по їх ID."""
        response = self.api_context.post(f"/api/device/{device_id}/sensors/delete", data=sensor_ids, headers=self.headers)
        return response


    def get_sensor_computation_table(self, device_id: int, sensor_id: int):
        """Отримання таблиці обчислень датчика."""
        response = self.api_context.get(f"/api/device/{device_id}/sensors/{sensor_id}/table", headers=self.headers)
        return response


    def export_computation_table_data_X_Y_pairs_to_CSV(self, device_id: int, sensor_id: int):
        """Експорт даних таблиці обчислень X-Y пар в CSV файл."""
        response = self.api_context.get(f"/api/device/{device_id}/sensors/{sensor_id}/table/pairs/export", headers=self.headers)
        return response

    
    def list_available_attributes_keys(self, device_id: int):
        """Отримання списку доступних ключів атрибутів."""
        response = self.api_context.get(f"/api/device/{device_id}/attributes", headers=self.headers)
        return response