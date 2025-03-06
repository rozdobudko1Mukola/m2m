import pytest
from pytest import mark
from pages.api.managers import ManagersAPI 
from pages.api.auth_api import AuthAPI
from playwright.sync_api import expect


# Fixtures ---------------------------------------------------------------------

@pytest.fixture(scope="function")
def create_new_account_manager(api_context, admin_token, test_data):
    """Тест на створення нового акаунт менеджера."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.create_new_account_manager(
        firstName="autoTest",
        lastName="api",
        phone="380000000000",
        email="m2m.test.auto+APIAuto_manager@gmail.com"
    )

    expect(response).to_be_ok()

    json_data = response.json()
    test_data["manager_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def delete_account_manager(api_context, admin_token, test_data):
    """Тест на видалення акаунт менеджера."""
    yield

    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.delete_account_manager(test_data["manager_id"])
    expect(response).to_be_ok()
    test_data.pop("manager_id", None)


@pytest.fixture(scope="function")
def set_remove_account_to_manager(api_context, admin_token, test_data):
    """Тест на призначення акаунту менеджера."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.set_account_to_manager(
        test_data["manager_id"],
        test_data["account_id"]
    )
    expect(response).to_be_ok()

    yield

    response = managers_api.set_account_to_manager(
        test_data["manager_id"],
        test_data["account_id"]
    )
    expect(response).to_be_ok()


@pytest.fixture(scope="function")
def set_account_to_manager(api_context, admin_token, test_data, create_and_del_manager, create_and_del_account):
    """Тест на призначення акаунту менеджера."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.set_account_to_manager(
        test_data["manager_id"],
        test_data["account_id"]
    )
    expect(response).to_be_ok()
    
    assert response.json().get("managerId") == test_data["manager_id"]

    yield


# Test for the Managers API ---------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1757')
def test_get_account_manager_by_id(api_context, admin_token, test_data, create_and_del_manager):
    """Тест на отримання акаунт менеджера по ID."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.get_account_manager_by_id(test_data["manager_id"])
    expect(response).to_be_ok()
    assert response.json().get("id") == test_data["manager_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1758')
def test_update_account_manager_by_id(api_context, admin_token, test_data, create_and_del_manager):
    """Тест на оновлення акаунт менеджера по ID."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.update_account_manager_by_id(
        test_data["manager_id"],
        firstName="update autoTest"
    )
    expect(response).to_be_ok()
    assert response.json().get("firstName") == "update autoTest"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1759')
def test_delete_account_manager(api_context, admin_token, test_data, create_new_account_manager):
    """Тест на видалення акаунт менеджера."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.delete_account_manager(test_data["manager_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1760')
def test_retrieve_account_managers(api_context, admin_token, test_data, create_and_del_manager):
    """Тест на отримання списку акаунт менеджерів з пагінацією."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.retrieve_account_managers(
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1761')
def test_create_new_account_manager(api_context, admin_token, test_data, delete_account_manager):
    """Тест на створення нового акаунт менеджера."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.create_new_account_manager(
        firstName="autoTest",
        lastName="api",
        phone="380000000000",
        email="m2m.test.auto+APIAuto_manager@gmail.com"
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data.get("firstName") == "autoTest"

    test_data["manager_id"] = json_data.get("id")


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1762')
def test_set_account_to_manager(api_context, admin_token, test_data, create_and_del_manager, create_and_del_account):
    """Тест на призначення акаунту менеджера."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.set_account_to_manager(
        test_data["manager_id"],
        test_data["account_id"]
    )
    expect(response).to_be_ok()
    
    assert response.json().get("managerId") == test_data["manager_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1763')
@mark.skip("Test is not ready") # Skip test, figure out how to fix it later
def test_send_request_to_manager(api_context, admin_token, test_data, create_and_del_manager, create_and_del_account, set_remove_account_to_manager, get_new_account_token):
    """Тест на відправлення запиту менеджеру."""
    auth_api = AuthAPI(api_context)
    
    managers_api = ManagersAPI(api_context, admin_token)

    response = managers_api.send_request_to_manager("Test message")
    expect(response).to_be_ok()
    print(response.json())
    assert response.json().get("message") == "Test message"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1764')
def test_remove_link_from_account_to_manager(api_context, admin_token, test_data, create_and_del_manager, create_and_del_account, set_account_to_manager):
    """Тест на видалення посилання акаунту менеджера."""
    managers_api = ManagersAPI(api_context, admin_token)
    response = managers_api.remove_link_from_account_to_manager(test_data["account_id"])
    expect(response).to_be_ok()
