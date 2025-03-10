import pytest
from pytest import mark
from pages.api.sensors_api import SensorsAPI
from pages.api.devices_api import DeviceAPI
from pages.api.wastebin_api import WastebinAPI
from playwright.sync_api import expect

# Fixture -----------------------------------------------------------------------

@pytest.fixture(scope="session")
def test_data():
    """Фікстура для збереження даних між тестами для sensors апі тестів."""
    return {}
    

@pytest.fixture(scope="function")
def create_new_sensor(api_context, token, test_data):
    """Передумова створення нового датчика."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.create_new_sensor(
        device_id=test_data["device_id"],
        name="Test sensor",
        type="FUEL_LEVEL_SENSOR",
        property="can_fls"
    )
    expect(response).to_be_ok()
    test_data["sensor_id"] = response.json()["id"]

    yield   


@pytest.fixture(scope="function")
def remove_the_sensor(api_context, token, test_data):
    """Післяумова видалення датчика."""

    yield

    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.remove_the_sensor(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"]
    )
    expect(response).to_be_ok()
    test_data.pop("sensor_id", None)


@pytest.fixture(scope="session")
def create_and_remove_device(api_context, token, test_data):
    """Фікстура для створення пристрою перед тестом та видалення після тесту."""
    device_api = DeviceAPI(api_context, token)
    response = device_api.create_new_device(
        type="FUEL_VEHICLE",
        name="api Test Device",
        uniqueId=device_api.unique_id(),
        customFields="",
        adminFields="",
        phoneTracker=False
    )
    expect(response).to_be_ok()
    json_data = response.json()
    test_data["device_id"] = json_data.get("id")

    yield

    wastebin_api = WastebinAPI(api_context, token)

    if "device_id" in test_data:
        response = wastebin_api.move_device_to_wastebin(test_data["device_id"])
        if response.status == 200:  # Якщо пристрій успішно переміщено в кошик
            response = wastebin_api.device_permanent_delete(test_data["device_id"])
            expect(response).to_be_ok()
        
        # Очистка test_data["device_id"] після кожного видалення
        test_data.pop("device_id", None)


@pytest.fixture(scope="function")
def create_and_remove_sensor(api_context, token, test_data, create_and_remove_device):
    """Фікстура для створення датчика перед тестом та видалення після тесту."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.create_new_sensor(
        device_id=test_data["device_id"],
        name="Test sensor",
        type="FUEL_LEVEL_SENSOR",
        property="can_fls"
    )
    expect(response).to_be_ok()
    test_data["sensor_id"] = response.json()["id"]

    yield

    response = sensors_api.remove_the_sensor(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"]
    )
    expect(response).to_be_ok()
    test_data.pop("sensor_id", None)


# Tests -------------------------------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1010')
def test_create_new_sensor(api_context, token, test_data, create_and_remove_device, remove_the_sensor):
    """Тест на створення нового датчика."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.create_new_sensor(
        device_id=test_data["device_id"],
        name="Test sensor",
        type="FUEL_LEVEL_SENSOR",
        property="can_fls"
    )
    expect(response).to_be_ok()
    test_data["sensor_id"] = response.json()["id"]


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1006')
def test_remove_the_sensor(api_context, token, test_data, create_and_remove_device, create_new_sensor):
    """Тест на видалення датчика."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.remove_the_sensor(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"]
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1004')
def test_get_sensor_by_id(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на отримання даних про датчик по його ID."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.get_sensor_by_id(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"]
    )
    expect(response).to_be_ok()
    assert response.json()["name"] == "Test sensor"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1005')
def test_update_sensor_properties(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на оновлення властивостей датчика."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.update_sensor_properties(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"],
        name="Updated Test sensor",
        type="FUEL_LEVEL_SENSOR",
        property="can_fls"
    )
    expect(response).to_be_ok()
    assert response.json()["name"] == "Updated Test sensor"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1007')
def test_update_computation_table_data_X_Y_pairs(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на оновлення або зміна даних таблиці обчислень X-Y пар."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.update_computation_table_data_X_Y_pairs(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"],
        pairs=[
            {
                "x": 1,
                "y": 2
            }
        ]
    )
    expect(response).to_be_ok()
    assert response.json()['pairs'] == [{"x": 1, "y": 2}]


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1008')
def test_update_computation_table_approximation_coefficients_and_min_max_value(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на оновлення або зміна коефіцієнтів апроксимації та minValue або maxValue."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.update_computation_table_approximation_coefficients_and_min_max_value(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"],
        coeffs=[
            {
                "x": 1,
                "a": 2,
                "b": 3
            }
        ],
        minValue=1,
        maxValue=100,
        applyRange='true'
    )
    expect(response).to_be_ok()
    assert response.json()['coeffs'] == [{"x": 1, "a": 2, "b": 3}]


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1743')
def test_get_sensor_additional_properties(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на отримання додаткових властивостей датчика."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.get_sensor_additional_properties(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"]
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1741')
def test_update_sensor_additional_properties(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на оновлення додаткових властивостей датчика."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.update_sensor_additional_properties(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"],
        refillTimeout=100
    )
    expect(response).to_be_ok()
    assert response.json()['refillTimeout'] == 100


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1009')
def test_retrieve_a_list_of_sensors(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на отримання списку датчиків."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.retrieve_a_list_of_sensors(
        device_id=test_data["device_id"]
    )
    expect(response).to_be_ok()
    assert len(response.json()) > 0


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1742')
@mark.skip("Тест на імпорт даних таблиці обчислень X-Y пар з CSV файлу поки не імплементовано.")
def test_import_computation_table_data_X_Y_pairs_from_CSV(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на імпорт даних таблиці обчислень X-Y пар з CSV файлу."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.import_computation_table_data_X_Y_pairs_from_CSV(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"],
        file="test.csv"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1011')
def test_calculate_computation_table_coefficients(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на розрахунок коефіцієнтів таблиці обчислень."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.calculate_computation_table_coefficients(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"]
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1012')
def test_delete_multiple_sensors_by_ids(api_context, token, test_data, create_and_remove_device, create_new_sensor):
    """Тест на видалення декількох датчиків по їх ID."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.delete_multiple_sensors_by_ids(
        device_id=test_data["device_id"],
        sensor_ids=[test_data["sensor_id"]]
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1013')
def test_get_sensor_computation_table(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на отримання таблиці обчислень датчика."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.get_sensor_computation_table(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"]
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1014')
def test_export_computation_table_data_X_Y_pairs_to_CSV(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на експорт таблиці обчислень датчика."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.export_computation_table_data_X_Y_pairs_to_CSV(
        device_id=test_data["device_id"],
        sensor_id=test_data["sensor_id"]
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="table.csv"', f"Expected Content-Disposition: attachment; filename=table.csv, but got: {response.headers.get('Content-Disposition')}"



@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1015')
def test_list_available_attributes_keys(api_context, token, test_data, create_and_remove_device, create_and_remove_sensor):
    """Тест на отримання списку доступних ключів атрибутів."""
    sensors_api = SensorsAPI(api_context, token)
    response = sensors_api.list_available_attributes_keys(
        device_id=test_data["device_id"]
    )
    expect(response).to_be_ok()
