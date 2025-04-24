import pytest
from typing import List
from pages.api.wastebin_api import WastebinAPI
from playwright.sync_api import APIRequestContext 
from playwright.sync_api import expect
from pages.api.devices_api import DeviceAPI
from pages.api.device_groups_api import DeviceGroupsAPI


#### -----Fixtures with use in APi ------------------------------------------------
# # Units Fixtures --------------------------------------------------------------


@pytest.fixture(scope="function")
def test_data():
    """Фікстура для збереження даних між тестами."""
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
    for i in range(1, num_devices + 1):
        response = device_api.create_new_device(
            name=f"Test device {i}",
            type="VEHICLE",
            uniqueId=device_api.unique_id()
        )
        expect(response).to_be_ok()
        test_data["device_ids"].append(response.json().get("id"))
        test_data["uniqueId"].append(response.json().get("uniqueId"))
    
    # Передаємо список створених ID у тест
    yield test_data["device_ids"]
    
    # Після виконання тесту видаляємо пристрої
        # Отримуємо всі ID з усіх трьох джерел
    active_ids = {
        device["id"]
        for device in device_api.retrieve_list_of_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    paused_ids = {
        device["id"]
        for device in wastebin_api.retrieve_a_list_of_paused_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    deleted_ids = {
        device["id"]
        for device in wastebin_api.retrieve_list_of_deleted_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    # Переміщаємо все, що ще не в кошику
    for device_id in active_ids.union(paused_ids):
        move_response = wastebin_api.move_device_to_wastebin(device_id)
        expect(move_response).to_be_ok()

    # Видаляємо усе, що в кошику
    for device_id in deleted_ids.union(active_ids).union(paused_ids):
        delete_response = wastebin_api.device_permanent_delete(device_id)
        expect(delete_response).to_be_ok()
    
    # Очищення test_data
    test_data.pop("device_ids", None)


# Group Fixtures ----------------------------------------------------------------------------------------------------------------------------------------

@pytest.fixture(scope="function")
def create_and_del_device_groups(api_context, token, test_data, request):
    """
    Фікстура для створення заданої кількості груп пристроїв перед тестом та їх видалення після.
    Кількість визначається параметром request.param (наприклад: @pytest.mark.parametrize(create_and_del_device_groups, [3], indirect=True)).
    """
    device_groups_api = DeviceGroupsAPI(api_context, token)
    
    # Список ID створених груп
    test_data["device_group_ids"] = []
    
    # Кількість груп для створення
    num_groups = request.param if hasattr(request, "param") else 1

    # Створення груп
    for i in range(num_groups):
        response = device_groups_api.create_new_device_group(
            name=f"Test Device Group {i + 1}"
        )
        expect(response).to_be_ok()
        group_id = response.json().get("id")
        test_data["device_group_ids"].append(group_id)

    yield test_data["device_group_ids"]

    # Видалення створених груп
    for group_id in test_data["device_group_ids"]:
        try:
            response = device_groups_api.remove_device_group(group_id)
            expect(response).to_be_ok()
        except Exception:
            pass  # Якщо група не знайдена або вже видалена, просто пропустимо

    # Очищення test_data
    test_data.pop("device_group_ids", None)


@pytest.fixture(scope="function")
def delete_device_groups_after_test(api_context, token, test_data):
    """
    Фікстура для видалення груп пристроїв після виконання тесту.
    Очікує, що test_data["device_group_ids"] буде містити список ID груп для видалення.
    """
    yield  # Тест виконується тут

    device_groups_api = DeviceGroupsAPI(api_context, token)

    # Пошук усіх груп
    response = device_groups_api.retrieve_a_list_of_devices_groups_with_pagination(page=1, per_page=10)
    expect(response).to_be_ok()

    items = response.json().get("items", [])

    # Запишемо всі ID груп, які треба видалити, в список
    group_ids = test_data.get("device_group_ids", [])

    for group in items:
        # якщо хочеш фільтрувати тільки певні групи (наприклад, назва = "Test_group")
        if group["name"] == "Test_group":
            group_ids.append(group["id"])

    # Тепер видаляємо всі зібрані ID
    for group_id in group_ids:
        response = device_groups_api.remove_device_group(group_id)
        expect(response).to_be_ok()

    # Очистка test_data
    test_data.pop("device_group_ids", None)



### Searshcing fixtures -------------------------------------------------------------

@pytest.fixture(scope="class")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}


@pytest.fixture(scope="class")
def full_unit_create_and_remove_by_api(api_context: APIRequestContext, token: str, test_data, request):
    """Фікстура для створення та видалення пристроїв через API після кожного тесту.
    Кількість пристроїв визначається параметром request.param."""
    
    device_api = DeviceAPI(api_context, token)
    wastebin_api = WastebinAPI(api_context, token)

    # Визначаємо кількість пристроїв для створення (за замовчуванням 1)
    num_devices = request.param if hasattr(request, "param") else 1
    test_data["device_ids"] = []
    test_data["uniqueId"] = []
    test_data["customFields"] = []
    test_data["adminFields"] = []
    test_data["phone"] = []
    test_data["phone2"] = []
    test_data["device_name"] = []
    test_data["model"] = []

    # Створюємо пристрої та зберігаємо їхні ID
    for i in range(1, num_devices + 1):
        # Для перної кількості обʼєктів ми запвнюємо поле phone, для непарної - phone2.
        phone = "+380123456789" if i % 2 != 0 else ""
        phone2 = "" if i % 2 != 0 else "+380980000000"

        customFields = "{\"custom Field Name\":\"custom Field value\"}" if i % 2 != 0 else "{\"name 123\":\" value 123\"}"
        adminFields = "{\"name 123\":\"value 123\"}" if i % 2 != 0 else "{\"admin Field name\":\"admin Field value\"}"

        response = device_api.create_new_device(
            name=f"Test device {i}",
            type="VEHICLE",
            uniqueId=device_api.unique_id(),
            customFields=customFields,
            adminFields=adminFields,
            phone=phone,
            phone2=phone2
        )
        expect(response).to_be_ok()
        
        test_data["unit_id"] = response.json().get("id")

        test_data["device_ids"].append(response.json().get("id"))
        test_data["customFields"].append(response.json().get("customFields"))
        test_data["adminFields"].append(response.json().get("adminFields"))
        test_data["device_name"].append(response.json().get("name"))

        model = "M2M Mobile Tracker" if i % 2 != 0 else "TK104" # Для парної кількості обʼєктів ми запвнюємо поле model як TK104, для непарної - M2M Mobile Tracker.

        response = device_api.update_connection_parameters(
            device_id=test_data["unit_id"],
            uniqueId=device_api.unique_id(),
            phone=phone,
            phone2=phone2,
            model=model
        )
    
        expect(response).to_be_ok()
        test_data["uniqueId"].append(response.json().get("uniqueId"))
        test_data["phone"].append(response.json().get("phone"))
        test_data["phone2"].append(response.json().get("phone2"))
        test_data["model"].append(response.json().get("model"))

    # Передаємо список створених ID у тест
    yield test_data
    
    # Отримуємо всі ID з усіх трьох джерел
    active_ids = {
        device["id"]
        for device in device_api.retrieve_list_of_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    paused_ids = {
        device["id"]
        for device in wastebin_api.retrieve_a_list_of_paused_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    deleted_ids = {
        device["id"]
        for device in wastebin_api.retrieve_list_of_deleted_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    # Переміщаємо все, що ще не в кошику
    for device_id in active_ids.union(paused_ids):
        move_response = wastebin_api.move_device_to_wastebin(device_id)
        expect(move_response).to_be_ok()

    # Видаляємо усе, що в кошику
    for device_id in deleted_ids.union(active_ids).union(paused_ids):
        delete_response = wastebin_api.device_permanent_delete(device_id)
        expect(delete_response).to_be_ok()  

    # Очищення test_data
    test_data.pop("device_ids", None)


@pytest.fixture(scope="class")
def cleanup_devices():

    device_api = DeviceAPI(api_context, token)
    wastebin_api = WastebinAPI(api_context, token)

    # Отримуємо всі ID з усіх трьох джерел
    active_ids = {
        device["id"]
        for device in device_api.retrieve_list_of_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    paused_ids = {
        device["id"]
        for device in wastebin_api.retrieve_a_list_of_paused_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    deleted_ids = {
        device["id"]
        for device in wastebin_api.retrieve_list_of_deleted_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    # Переміщаємо все, що ще не в кошику
    for device_id in active_ids.union(paused_ids):
        move_response = wastebin_api.move_device_to_wastebin(device_id)
        expect(move_response).to_be_ok()

    # Видаляємо усе, що в кошику
    for device_id in deleted_ids.union(active_ids).union(paused_ids):
        delete_response = wastebin_api.device_permanent_delete(device_id)
        expect(delete_response).to_be_ok()

    # Повертаємо очищене середовище, якщо це потрібно для тестів
    yield