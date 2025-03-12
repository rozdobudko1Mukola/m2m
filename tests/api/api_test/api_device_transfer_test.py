import pytest
from pytest import mark
from pages.api.device_transder_api import DeviceTransferAPI
from pages.api.account_api import AccountAPI
from playwright.sync_api import expect

# Fixtures ---------------------------------------------------------------------

@pytest.fixture(scope="function")
def get_test_account_id(api_context, test_data, token):
    """Фікстура для отримання ID аккаунту."""
    account_api = AccountAPI(api_context, token)
    response = account_api.retrieve_account_data()
    test_data["account_id"] = response.json().get("id")
    yield

# Tests ------------------------------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('')
def test_transfer_devices_to_account(api_context, admin_token, test_data, pre_and_post_conditions_device, get_test_account_id):
    """Тест на передачу пристроїв на інший акаунт."""
    device_transfer_api = DeviceTransferAPI(api_context, admin_token)
    response = device_transfer_api.transfer_devices_to_account(
        accountId=test_data["account_id"],
        deviceIds=[test_data["device_id"]]
        )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1053')
def test_retrieve_a_paginated_devices_not_in_account(api_context, admin_token, test_data, get_test_account_id):
    """Тест на отримання списку пристроїв, які не належать аккаунту."""
    device_transfer_api = DeviceTransferAPI(api_context, admin_token)
    response = device_transfer_api.retrieve_a_paginated_devices_not_in_account(
        test_data["account_id"],
        page=1,
        per_page=10
        )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@@Ttttt1055')
def test_retrieve_a_paginated_devices_in_account(api_context, admin_token, test_data, get_test_account_id):
    """Тест на отримання списку пристроїв, які належать аккаунту."""
    device_transfer_api = DeviceTransferAPI(api_context, admin_token)
    response = device_transfer_api.retrieve_a_paginated_devices_in_account(
        test_data["account_id"],
        page=1,
        per_page=10
        )
    expect(response).to_be_ok()
