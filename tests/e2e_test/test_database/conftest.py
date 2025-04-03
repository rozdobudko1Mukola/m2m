import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from pages.e2e.database.objects import ObjectsPage
from pages.e2e.database.on_pause import onPausePage



# Group Fixtures ------------------------------------------------------------

@pytest.fixture
def create_and_remove_one_group(freebill_user: Page):
    objects_page = ObjectsPage(freebill_user)

    # Create group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 3)
    objects_page.popap_btn["ok"].click()
    freebill_user.wait_for_selector("#display-tabpanel-1 table")

    yield

    # Remove group
    freebill_user.wait_for_timeout(1000)
    while objects_page.group_table["body_row"].count() > 0:
        objects_page.remove_group()
        freebill_user.wait_for_timeout(500)


@pytest.fixture()
def create_and_remove_12_group(freebill_user: Page, index=13):
    objects_page = ObjectsPage(freebill_user)

    # Create group
    objects_page.page_tab_buttons["groups"].click()
    for i in range(index):
        objects_page.add_new_group(f"Test group {i}", 3)
        objects_page.popap_btn["ok"].click()

    yield

    # Remove group
    freebill_user.wait_for_timeout(1000)
    while objects_page.group_table["body_row"].count() > 0:
        objects_page.remove_group()
        freebill_user.wait_for_timeout(500)


@pytest.fixture()
def create_and_remove_3_groups(freebill_user: Page, index=3):
    objects_page = ObjectsPage(freebill_user)

    # Create group
    objects_page.page_tab_buttons["groups"].click()
    for i in range(index):
        objects_page.add_new_group(f"Test group {i}", 3)
        objects_page.popap_btn["ok"].click()

    yield

    # Remove group
    if objects_page.head_menu_group_locators["group_search_input"].input_value() != "":
        objects_page.head_menu_group_locators["group_search_input"].fill("")
        freebill_user.wait_for_timeout(1000)

        while objects_page.group_table["body_row"].count() > 0:
            objects_page.remove_group()
            freebill_user.wait_for_timeout(500)


@pytest.fixture
def create_and_remove_25_group(freebill_user: Page, index=26):
    objects_page = ObjectsPage(freebill_user)

    # Create group
    objects_page.page_tab_buttons["groups"].click()
    for i in range(index):
        objects_page.add_new_group(f"Test group {i}", 3)
        objects_page.popap_btn["ok"].click()

    yield

    # Remove group
    freebill_user.wait_for_timeout(1000)
    while objects_page.group_table["body_row"].count() > 0:
        objects_page.remove_group()
        freebill_user.wait_for_timeout(500)


@pytest.fixture
def just_remove_groups(freebill_user: Page):
    objects_page = ObjectsPage(freebill_user)

    yield 
    # Remove group
    freebill_user.wait_for_timeout(1000)
    while objects_page.group_table["body_row"].count() > 0:
        objects_page.remove_group()
        freebill_user.wait_for_timeout(500)


# Units Fixtures --------------------------------------------------------------

@pytest.fixture
def create_and_remove_one_units(selfreg_user: Page):
    objects_page = ObjectsPage(selfreg_user)

    # Preconditions add object
    objects_page.precondition_add_multiple_objects(1, "Auto_Test", "180455679224", "180455679224", "Teltonika FMB965", "VEHICLE")
    objects_page.object_main_popap_inputs["name"].wait_for(state="detached")
    selfreg_user.wait_for_timeout(500)

    yield  # Provide the data to the test

    # Delete all objects from pause to trash after test
    selfreg_user.wait_for_timeout(1000)
    while objects_page.unit_table["body_row"].count() > 0:
        objects_page.move_to_trash_all_object()
        selfreg_user.wait_for_timeout(500)


@pytest.fixture
def just_remove_units(selfreg_user: Page):
    objects_page = ObjectsPage(selfreg_user)

    yield  # Provide the data to the test

    # Delete all objects from pause to trash after test
    selfreg_user.wait_for_timeout(1000)
    while objects_page.unit_table["body_row"].count() > 0:
        objects_page.move_to_trash_all_object()
        selfreg_user.wait_for_timeout(500)

@pytest.fixture
def move_unnit_to_trash(selfreg_user: Page):
    objects_page = ObjectsPage(selfreg_user)

    yield  # Provide the data to the test

    on_pause_page = onPausePage(selfreg_user)
    on_pause_page.all_unit_move_to_trash()

# @pytest.fixture
# def just_remove_units(selfreg_user: Page):
#     print("\nTearing down resources...")
#     objects_page = ObjectsPage(selfreg_user)

#     yield  # Provide the data to the test
#     # Teardown: Clean up resources (if any) after the test
#     print("\nTearing down resources...")
#     objects_page.pause_all_object()
#     # Delete all objects from pause to trash after test
#     on_pause_page = onPausePage(selfreg_user)
#     on_pause_page.all_unit_move_to_trash()


#### -----Fixtures with use in APi ------------------------------------------------

import pytest
from typing import List
from pages.api.wastebin_api import WastebinAPI
from playwright.sync_api import APIRequestContext 
from playwright.sync_api import expect
from pages.api.devices_api import DeviceAPI


@pytest.fixture(scope="function")
def test_data():
    """Фікстура для збереження даних між тестами для всих апі тестів."""
    return {}


@pytest.fixture
def remove_units_by_api(api_context: APIRequestContext, token: str, test_data):
    """Фікстура для видалення пристроїв через API після кожного тесту."""
    
    yield

    wastebin_api = WastebinAPI(api_context, token)
    device_api = DeviceAPI(api_context, token)

    # Пошук усіх пристроїв
    response = device_api.retrieve_list_of_devices_with_pagination(page=1, per_page=10)
    expect(response).to_be_ok()

    items = response.json().get("items", [])
    if items:
        for device in items:
            # Перевіряємо, чи співпадає creatorName
            if device.get("creatorName") == "m2m.test.auto@gmail.com [m2m.test.auto@gmail.com]":
                test_data["device_id"] = device["id"]
                
                # Переміщаємо пристрій в кошик та видаляємо його
                response = wastebin_api.move_device_to_wastebin(test_data["device_id"])
                if response.status == 200:  # Якщо пристрій успішно переміщено в кошик
                    response = wastebin_api.device_permanent_delete(test_data["device_id"])
                    expect(response).to_be_ok()

                # Очистка test_data["device_id"] після кожного видалення
                test_data.pop("device_id", None)
                break  # Перериваємо цикл після успішного видалення пристрою




@pytest.fixture
def create_and_remove_units_by_api(api_context: APIRequestContext, token: str, test_data, request):
    """Фікстура для створення та видалення пристроїв через API після кожного тесту.
    Кількість пристроїв визначається параметром request.param."""
    
    device_api = DeviceAPI(api_context, token)
    wastebin_api = WastebinAPI(api_context, token)

    # Визначаємо кількість пристроїв для створення (за замовчуванням 1)
    num_devices = request.param if hasattr(request, "param") else 1
    test_data["device_ids"] = []
    test_data["uniqueId"] = []

    # Створюємо пристрої та зберігаємо їхні ID
    for _ in range(num_devices):
        response = device_api.create_new_device(
            name="Test device",
            type="VEHICLE",
            uniqueId=device_api.unique_id()
        )
        expect(response).to_be_ok()
        test_data["device_ids"].append(response.json().get("id"))
        test_data["uniqueId"].append(response.json().get("uniqueId"))
    
    # Передаємо список створених ID у тест
    yield test_data["device_ids"]
    
    # Після виконання тесту видаляємо пристрої
    for device_id in test_data["device_ids"]:
        for retrieval_method in [
            device_api.retrieve_list_of_devices_with_pagination,  # Отримуємо активні пристрої
            wastebin_api.retrieve_a_list_of_paused_devices_with_pagination,  # Отримуємо призупинені пристрої
            wastebin_api.retrieve_list_of_deleted_devices_with_pagination  # Отримуємо пристрої в кошику
        ]:
            response = retrieval_method(page=1, per_page=50)
            expect(response).to_be_ok()
            
            items = response.json().get("items", [])
            for device in items:
                if device["id"] == device_id:
                    # Переміщаємо пристрій в кошик перед видаленням
                    response = wastebin_api.move_device_to_wastebin(device_id)
                    if response.status == 200:
                        response = wastebin_api.device_permanent_delete(device_id)  # Остаточне видалення
                        expect(response).to_be_ok()
                    break  # Пристрій знайдено і видалено, переходимо до наступного
    
    # Очистка test_data після видалення пристроїв
    test_data.pop("device_ids", None)
