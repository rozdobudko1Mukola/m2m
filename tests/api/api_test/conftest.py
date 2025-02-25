import pytest
from playwright.sync_api import expect
from pages.api.devices_api import DeviceAPI
from pages.api.wastebin_api import WastebinAPI
from pages.api.users_api import UsersAPI
from faker import Faker


@pytest.fixture(scope="session")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}
    

@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
def postcondition_permanent_del_device(api_context, token, test_data):
    """Фікстура для видалення пристрою за його ID. Пристрій повинен бути в корзині."""

    yield

    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.device_permanent_delete(test_data["device_id"])
    expect(response).to_be_ok()
    test_data.pop("device_id", None)



# @pytest.fixture(scope="session")
# def pre_and_post_conditions(api_context, token, test_data):
#     """Фікстура для створення пристрою перед стестом та видалення після тесту."""
#     device_api = DeviceAPI(api_context, token)
#     response = device_api.create_new_device(
#         type="VEHICLE",
#         name="api Test Device",
#         uniqueId=device_api.unique_id(),
#         customFields="",
#         adminFields="",
#         phoneTracker=False
#     )
#     expect(response).to_be_ok()
#     json_data = response.json()
#     test_data["device_id"] = json_data.get("id")   

#     yield

#     wastebim_api = WastebinAPI(api_context, token)
#     response = wastebim_api.move_device_to_wastebin(test_data["device_id"])
#     expect(response).to_be_ok()
#     # response = wastebim_api.retrieve_list_of_deleted_devices_with_pagination(page=1, per_page=10)
#     # assert response.json()["items"][0]["id"] == test_data["device_id"]
#     response = wastebim_api.device_permanent_delete(test_data["device_id"])
#     expect(response).to_be_ok()


@pytest.fixture(scope="session")
def pre_and_post_conditions(api_context, token, test_data):
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


@pytest.fixture(scope="session")
def create_and_del_user_by_accaunt(api_context, token, test_data):
    """Фікстура для створення користувача перед тестом та видалення після тесту."""
    fake = Faker()
    user_api = UsersAPI(api_context, token)

    response = user_api.create_new_user(
        email=fake.email(),
        password="123456",
        language="UKRAINIAN"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["user_id"] = json_data.get("id")

    yield

    response = user_api.remove_child_user(test_data["user_id"])
    expect(response).to_be_ok()


@pytest.fixture(scope="session")
def fixt_move_device_to_pause(api_context, token, test_data):
    """Переміщає пристрій в корзину."""
    device_api = DeviceAPI(api_context, token)
    response = device_api.move_device_to_pause(device_id=test_data["device_id"])
    expect(response).to_be_ok()
    yield


@pytest.fixture(scope="session")
def move_device_to_wastebin(api_context, token, test_data):
    """Переміщає пристрій в корзину."""
    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.move_device_to_wastebin(device_id=test_data["device_id"])
    expect(response).to_be_ok()
    yield

