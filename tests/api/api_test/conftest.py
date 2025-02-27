import pytest
from playwright.sync_api import expect

from pages.api.devices_api import DeviceAPI
from pages.api.wastebin_api import WastebinAPI
from pages.api.report_templates_api import ReportTemplatesAPI
from pages.api.geofences_api import GeofencesAPI
from pages.api.users_api import UsersAPI
from pages.api.device_groups_api import DeviceGroupsAPI


@pytest.fixture(scope="function")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}
    

# Fixtures for the test DevicesAPI

@pytest.fixture(scope="function")
def create_device_precondition(api_context, token, test_data):
    """Фікстура для створення пристрою перед тестом."""
    device_api = DeviceAPI(api_context, token)
    response = device_api.create_new_device(
        type="VEHICLE",
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


@pytest.fixture(scope="function")
def postcondition_permanent_del_device(api_context, token, test_data):
    """Фікстура для видалення пристрою за його ID. Пристрій повинен бути в корзині."""

    yield

    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.device_permanent_delete(test_data["device_id"])
    expect(response).to_be_ok()
    test_data.pop("device_id", None)


@pytest.fixture(scope="function")
def pre_and_post_conditions_device(api_context, token, test_data):
    """Фікстура для створення пристрою перед тестом та видалення після тесту."""
    device_api = DeviceAPI(api_context, token)
    response = device_api.create_new_device(
        type="VEHICLE",
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
def fixt_move_device_to_pause(api_context, token, test_data):
    """Переміщає пристрій в корзину."""
    device_api = DeviceAPI(api_context, token)
    response = device_api.move_device_to_pause(device_id=test_data["device_id"])
    expect(response).to_be_ok()
    yield


@pytest.fixture(scope="function")
def move_device_to_wastebin(api_context, token, test_data):
    """Переміщає пристрій в корзину."""
    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.move_device_to_wastebin(device_id=test_data["device_id"])
    expect(response).to_be_ok()
    yield


# Fixtures for the test device_groupsAPI------------------------------------------------------------
@pytest.fixture(scope="function")
def create_and_del_device_group(api_context, token, test_data):
    """Фікстура для створення групи пристроїв перед тестом та видалення після тесту."""
    device_groups_api = DeviceGroupsAPI(api_context, token)
    response = device_groups_api.create_new_device_group(
        name="Test Device Group"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["device_group_id"] = json_data.get("id")

    yield

    response = device_groups_api.remove_device_group(test_data["device_group_id"])
    expect(response).to_be_ok()
    test_data.pop("device_group_id", None)


# Fixtures for the test UsersAPI

@pytest.fixture(scope="function")
def create_and_del_user_by_accaunt(api_context, token, test_data):
    """Фікстура для створення користувача перед тестом та видалення після тесту."""
    user_api = UsersAPI(api_context, token)

    response = user_api.create_new_user(
        email="m2m.test.auto+APIAuto@gmail.com",
        password="123456",
        language="UKRAINIAN"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["user_id"] = json_data.get("id")

    yield

    response = user_api.remove_child_user(test_data["user_id"])
    expect(response).to_be_ok()
    test_data.pop("user_id", None)


# Fixtures for the test ReportTemplatesAPI

@pytest.fixture(scope="function")
def create_and_del_report_template(api_context, token, test_data):
    """Фікстура для створення шаблону звіту перед тестом та видалення після тесту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template(
        name="Test Report Template",
        elementType="DEVICE"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["template_id"] = json_data.get("id")

    yield

    response = report_templates_api.remove_report_template(test_data["template_id"])
    expect(response).to_be_ok()
    test_data.pop("template_id", None)


@pytest.fixture(scope="function")
def create_and_del_report_template_chart(api_context, token, test_data):
    """Фікстура для створення графіка в шаблоні звіту перед тестом та видалення після тесту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template_chart(
        template_id=test_data["template_id"],
        name="Test Chart",
        selectedSensors=["SPEED"]
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["chart_id"] = json_data.get("id")

    yield

    response = report_templates_api.remove_report_template_chart(
        template_id=test_data["template_id"],
        chart_id=test_data["chart_id"]
        )
    expect(response).to_be_ok()
    test_data.pop("chart_id", None)


@pytest.fixture(scope="function")
def create_and_del_report_template_table(api_context, token, test_data):
    """Фікстура для створення таблиці в шаблоні звіту перед тестом та видалення після тесту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template_table(
        template_id=test_data["template_id"],
        title="Test Table",
        tableType="DEVICE_REFILL",
        tableColumns=["REFILL_START_TIME"]
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["table_id"] = json_data.get("id")

    yield

    response = report_templates_api.remove_report_template_table(
        template_id=test_data["template_id"],
        table_id=test_data["table_id"]
        )
    expect(response).to_be_ok()
    test_data.pop("table_id", None)


# Fixtures for the test geofencesAPI
@pytest.fixture(scope="function")
def create_and_remove_geofence(api_context, token, test_data):
    """Фікстура для створення геозони перед тестом та видалення після тесту."""
    geofences = GeofencesAPI(api_context, token)
    response = geofences.create_new_geofence(
        name="Test Geofence",
        description="Test Geofence Description",
        area='{"type":"Circle","coordinates":[30.035527000, 51.835087000],"radius":187.237000000,"radius_units":"km"}',
        fillColor="#0091DC",
        strokeColor="#44D600"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["geofence_id"] = json_data.get("id")

    yield

    response = geofences.remove_the_geofence(test_data["geofence_id"])
    expect(response).to_be_ok()
    test_data.pop("geofence_id", None)