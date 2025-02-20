import pytest
from playwright.sync_api import expect
from pages.api.devices_api import DeviceAPI
from pages.api.wastebin_api import WastebinAPI

@pytest.fixture(scope="session")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}
    

@pytest.fixture(scope="session")
def create_device_precondition(api_context, token, test_data):
    """Фікстура для створення пристрою перед стестом."""
    device_api = DeviceAPI(api_context, token)
    response = device_api.create_new_device(
        dev_type="VEHICLE",
        name="api Test Device",
        unique_id=device_api.unique_id(),
        phone="+380501234567"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["device_id"] = json_data.get("id")        

    yield 


@pytest.fixture(scope="session")
def postcondition_permanent_del_device(api_context, token, test_data):
    """Фікстура для видалення пристрою за його ID. Спочатку в корзину, потім назавжди."""

    yield

    wastebim_api = WastebinAPI(api_context, token)
    response = wastebim_api.device_permanent_delete(test_data["device_id"])
    expect(response).to_be_ok()