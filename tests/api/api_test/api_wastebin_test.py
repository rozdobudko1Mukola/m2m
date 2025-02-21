import pytest
from pytest import mark
from pages.api.devices_api import DeviceAPI
from pages.api.wastebin_api import WastebinAPI
from playwright.sync_api import expect


@mark.smoke
@mark.api
@mark.testomatio('')
def test_unpause_device(api_context, token, test_data, pre_and_post_conditions, fixt_move_device_to_pause):
    """Тестуємо відновлення пристрою з корзини"""
    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.unpause_device(device_id=test_data["device_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('')
def test_restore_the_device_from_wastebin(api_context, token, test_data, pre_and_post_conditions, move_device_to_wastebin):
    """Тестуємо відновлення пристрою з корзини"""
    wastebin_api = WastebinAPI(api_context, token)
    
    response = wastebin_api.restore_the_device_from_wastebin(device_id=test_data["device_id"])
    expect(response).to_be_ok()



@mark.smoke
@mark.api
@mark.testomatio('')
def test_retrieve_a_list_of_paused_devices_with_pagination(api_context, token, test_data, pre_and_post_conditions):
    """Тестуємо отримання списку пристроїв з корзини"""
    devise_api = DeviceAPI(api_context, token)
    response = devise_api.move_device_to_pause(device_id=test_data["device_id"])
    expect(response).to_be_ok()

    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.retrieve_a_list_of_paused_devices_with_pagination(page=1, per_page=10)

    expect(response).to_be_ok()
    assert response.json()["items"][0]["id"] == test_data["device_id"]


@mark.smoke
@mark.api
@mark.testomatio('')
def test_export_list_of_devices_with_pagination_to_excel(api_context, token, pre_and_post_conditions, move_device_to_wastebin):
    """Тестуємо експорт списку пристроїв з пагінацією в Excel"""
    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.export_list_of_devices_with_pagination_to_file(file_ext="xls", page=1, per_page=10)
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="devices.xls"', f"Expected Content-Disposition: attachment; filename=devices.xlsx, but got: {response.headers.get('Content-Disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('')
def test_export_list_of_devices_with_pagination_to_csv(api_context, token, pre_and_post_conditions, move_device_to_wastebin):
    """Тестуємо експорт списку пристроїв з пагінацією в csv"""
    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.export_list_of_devices_with_pagination_to_file(file_ext="csv", page=1, per_page=10)
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="devices.csv"', f"Expected Content-Disposition: attachment; filename=devices.xlsx, but got: {response.headers.get('Content-Disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('')
def test_retrieve_list_of_deleted_devices_with_pagination(api_context, token, test_data, pre_and_post_conditions):
    """Тестуємо отримання списку видалених пристроїв з корзини"""
    wastebin_api = WastebinAPI(api_context, token)

    response = wastebin_api.move_device_to_wastebin(device_id=test_data["device_id"])
    expect(response).to_be_ok()

    response = wastebin_api.retrieve_list_of_deleted_devices_with_pagination(page=1, per_page=10)
    expect(response).to_be_ok()
    assert response.json()["items"][0]["id"] == test_data["device_id"]


@mark.smoke
@mark.api
@mark.testomatio('')
def test_move_devise_to_waisbin(api_context, token, test_data, create_device_precondition, ):
    """Тестуємо переміщення пристрою в корзину"""
    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.move_device_to_wastebin(device_id=test_data["device_id"])
    
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('')
def test_device_permanent_delete(api_context, token, test_data, create_device_precondition):
    """Тестуємо видалення пристрою назавжди"""
    wastebin_api = WastebinAPI(api_context, token)
    response = wastebin_api.move_device_to_wastebin(test_data["device_id"])
    expect(response).to_be_ok()

    response = wastebin_api.device_permanent_delete(test_data["device_id"])
    expect(response).to_be_ok()
