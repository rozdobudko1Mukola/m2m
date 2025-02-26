import pytest
from pytest import mark
from pages.api.devices_api import DeviceAPI
from playwright.sync_api import expect


@mark.smoke 
@mark.api
@mark.testomatio('@Tttttt888')
def test_create_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо створення пристрою"""
    pass

@mark.smoke
@mark.api
@mark.testomatio('@Tttttt875')
def test_move_devise_to_pause(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо переміщення пристрою на паузу"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.move_device_to_pause(device_id=test_data["device_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt874')
def test_update_devise_characteristic(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо оновлення характеристик пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.update_devise_characteristic(
        device_id=test_data["device_id"],
        vinCode="vin 123",
        licencePlate="number",
        vendorName="opel",
        vendorModel="cadet",
        releaseYear="1999",
        engineVolume=1500,
        engineFuelType="disel",
        consumptionByNormLPH=1.3,
        consumptionByNormLpKM=13
    )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt873')
def test_get_device_by_id(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання пристрою по ID"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.get_device_by_id(device_id=test_data["device_id"])
    expect(response).to_be_ok()

    json_data = response.json()

    assert json_data.get("id") == test_data["device_id"], f"Expected device ID: {test_data['device_id']}, but got: {json_data.get('id')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt876')
def test_rename_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо перейменування пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.rename_device(device_id=test_data["device_id"], name="New Name")
    expect(response).to_be_ok()

    assert response.json().get("name") == "New Name", f"Expected device name: New Name, but got: {response.json().get('name')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt877')
def test_get_motion_detector_settings_for_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання налаштувань детектора руху для пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.get_motion_detector_settings_for_device(device_id=test_data["device_id"])
    expect(response).to_be_ok()

    assert response.json().get("minimalStopDuration") == 300, f"Expected minimalStopDuration: 300, but got: {response.json().get('minimalStopDuration')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt878')
def test_change_motion_detector_settings_for_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо зміну налаштувань детектора руху для пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.change_motion_detector_settings_for_device(
        device_id=test_data["device_id"],
        minimalStopDuration=100,
        minSpeed=100,
        minStayTime=100
    )
    expect(response).to_be_ok()
    assert response.json().get("minimalStopDuration") == 100, f"Expected minimalStopDuration: 100, but got: {response.json().get('minimalStopDuration')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt879')
def test_retrieve_custom_fields_for_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання додаткових полів для пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.retrieve_custom_fields_for_device(device_id=test_data["device_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt880')
def test_update_custom_fields_for_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо оновлення додаткових полів для пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.update_custom_fields_for_device(device_id=test_data["device_id"], customFields='{\"name test\":\"value test\"}')
    expect(response).to_be_ok()
    assert response.json().get("customFields") == '{\"name test\":\"value test\"}', f"Expected customFields: custom fields, but got: {response.json().get('customFields')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt881')
def test_get_connection_parameters(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання параметрів підключення"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.get_connection_parameters(device_id=test_data["device_id"])
    expect(response).to_be_ok()



@mark.smoke
@mark.api
@mark.testomatio('@Tttttt882')
def test_update_connection_parameters(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо оновлення параметрів підключення"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.update_connection_parameters(
        device_id=test_data["device_id"], 
        deviceType="FUEL_VEHICLE", 
        uniqueId=device_api.unique_id()
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt883')
def test_retrieve_admin_fields_for_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання адміністративних полів для пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.retrieve_admin_fields_for_device(device_id=test_data["device_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt884')
def test_update_admin_fields_for_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо оновлення адміністративних полів для пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.update_admin_fields_for_device(device_id=test_data["device_id"], adminFields='{\"name test_ad\":\"value test_ad\"}')
    expect(response).to_be_ok()
    assert response.json().get("adminFields") == '{\"name test_ad\":\"value test_ad\"}', f"Expected adminFields: admin fields, but got: {response.json().get('adminFields')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt887')
def test_retrieve_list_of_devices_with_pagination(api_context, token, pre_and_post_conditions_device):
    """Тестуємо отримання списку пристроїв з пагінацією"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.retrieve_list_of_devices_with_pagination(page=1, per_page=10)
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@T827baa0a')
def test_device_permissions_ids(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання ID дозволів для пристрою"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.device_permissions_ids(device_id=test_data["device_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Ttttt1844')
def test_export_list_of_devices_with_pagination_excel(api_context, token, pre_and_post_conditions_device):
    """Тестуємо експорт списку пристроїв з пагінацією в Excel"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.export_list_of_devices_with_pagination_excel(file_ext="xls", page=1, per_page=10)
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="devices.xls"', f"Expected Content-Disposition: attachment; filename=devices.xlsx, but got: {response.headers.get('Content-Disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('@Ttttt1845')
def test_export_list_of_devices_with_pagination_csv(api_context, token, pre_and_post_conditions_device):
    """Тестуємо експорт списку пристроїв з пагінацією в csv"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.export_list_of_devices_with_pagination_excel(file_ext="csv", page=1, per_page=10)
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="devices.csv"', f"Expected Content-Disposition: attachment; filename=devices.xlsx, but got: {response.headers.get('Content-Disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt885')
def test_retrieve_device_permissions_for_child_user(api_context, token, test_data, pre_and_post_conditions_device, create_and_del_user_by_accaunt):
    """Тестуємо отримання прав користувача на пристрої"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.retrieve_device_permissions_for_child_user(user_id=test_data["user_id"], device_id=test_data["device_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt886')
def test_set_device_permissions_for_child_user(api_context, token, test_data, pre_and_post_conditions_device, create_and_del_user_by_accaunt):
    """Тестуємо встановлення прав користувача на пристрої"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.set_device_permissions_for_child_user(
        user_id=test_data["user_id"], 
        device_id=test_data["device_id"], 
        permission="RENAME_ELEMENT",
        state="true"
        )
    expect(response).to_be_ok()
    assert response.json().get("RENAME_ELEMENT") is True, f"Expected permissions: READ, but got: {response.json().get('permissions')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tc9d27714')
def test_switch_all_device_permissions_for_child_user(api_context, token, test_data, pre_and_post_conditions_device, create_and_del_user_by_accaunt):
    """Тестуємо встановлення прав користувача на пристрої"""
    device_api = DeviceAPI(api_context, token)
    response = device_api.switch_all_device_permissions_for_child_user(
        user_id=test_data["user_id"], 
        device_id=test_data["device_id"],
        state="true"
        )
    expect(response).to_be_ok()
    