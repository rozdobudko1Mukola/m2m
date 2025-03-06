import pytest
from pytest import mark
from pages.api.sim_card_api import SimCardAPI 
from playwright.sync_api import expect


# Fixtures ---------------------------------------------------------------------

@pytest.fixture(scope="function")
def create_simcard_precondition(api_context, admin_token, test_data):
    """Фікстура для створення SIM-карти перед тестом."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.create_new_simcard(
        icon="KYIVSTAR",
        iccid="123000111",
        phone="+380000000000",
        operator="KYIVSTAR",
        roaming="true"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["simcard_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def remove_simcard_postcondition(api_context, admin_token, test_data):
    """Фікстура для видалення SIM-карти після тесту."""
    yield

    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.remove_the_simcard(test_data["simcard_id"])
    expect(response).to_be_ok()
    test_data.pop("simcard_id", None)


# Test for the SimCard API ---------------------------------------------------
@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1065')
def test_create_new_simcard(api_context, admin_token, test_data, remove_simcard_postcondition):
    """Тест на створення нової SIM-карти."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.create_new_simcard(
        icon="KYIVSTAR",
        iccid="123000111",
        phone="+380000000000",
        operator="KYIVSTAR",
        roaming="true"
    )
    expect(response).to_be_ok() 
    
    json_data = response.json()
    test_data["simcard_id"] = json_data.get("id")


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1058')
def test_remove_the_simcard(api_context, admin_token, test_data, create_simcard_precondition):
    """Тест на видалення SIM-карти."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.remove_the_simcard(test_data["simcard_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1056')
def test_get_simcard_by_id(api_context, admin_token, test_data, create_and_remove_simcard):
    """Тест на отримання SIM-карти по ID."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.get_simcard_by_id(test_data["simcard_id"])
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("id") == test_data["simcard_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1057')
def test_update_simcard_properties(api_context, admin_token, test_data, create_and_remove_simcard):
    """Тест на оновлення властивостей SIM-карти."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.update_simcard_properties(
        simcard_id=test_data["simcard_id"],
        icon="LIFECELL",
    )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("icon") == "LIFECELL"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1064')
def test_retrieve_a_list_of_simcards_with_pagination(api_context, admin_token, test_data, create_and_remove_simcard):
    """Тест на отримання списку SIM-карт з пагінацією."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.retrieve_a_list_of_simcards_with_pagination(
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1065')
def test_assign_device_to_simcard(api_context, admin_token, test_data, create_and_remove_simcard, pre_and_post_conditions_device):
    """Тест на призначення пристрою до SIM-карти."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.assign_device_to_simcard(
        simcard_id=test_data["simcard_id"],
        device_id=test_data["device_id"]
    )
    expect(response).to_be_ok()
    assert response.json().get("deviceId") == test_data["device_id"]


@mark.api
@mark.smoke
@mark.testomatio('@T3cbc4bdf')
def test_assign_account_to_simcard(api_context, admin_token, test_data, create_and_remove_simcard, create_and_del_account):
    """Тест на призначення акаунта до SIM-карти."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.assign_account_to_simcard(
        simcard_id=test_data["simcard_id"],
        account_id=test_data["account_id"]
    )
    expect(response).to_be_ok()
    assert response.json().get("accountId") == test_data["account_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1059')
def test_export_a_list_of_simcards_with_pagination_to_xls(api_context, admin_token, test_data):
    """Тест на експорт списку SIM-карт з пагінацією в файл."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.export_a_list_of_simcards_with_pagination_to_file(
        file_ext="xls",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="sim_cards.xls"', f"Expected Content-Disposition: attachment; filename=sim_cards.xls, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@T09efbcd8')
def test_export_a_list_of_simcards_with_pagination_to_csv(api_context, admin_token, test_data):
    """Тест на експорт списку SIM-карт з пагінацією в файл."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.export_a_list_of_simcards_with_pagination_to_file(
        file_ext="csv",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="sim_cards.csv"', f"Expected Content-Disposition: attachment; filename=sim_cards.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1068')
def test_get_child_account_simcard_statistics(api_context, admin_token, test_data, create_and_del_account):
    """Тест на отримання статистики SIM-карт за дитячим акаунтом."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.get_child_account_simcard_statistics(
        account_id=test_data["account_id"],
        page=1,
        per_page=10,
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@T9a53e8a9')
def test_export_simcard_statistics_for_child_account_to_xls(api_context, admin_token, test_data, create_and_del_account):
    """Тест на експорт статистики SIM-карт за дитячим акаунтом в файл."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.export_simcard_statistics_for_child_account_to_file(
        account_id=test_data["account_id"],
        file_ext="excel",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="sim_card_statistics.xls"', f"Expected Content-Disposition: attachment; filename=sim_card_statistics.xls, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tf53310b3')
def test_export_simcard_statistics_for_child_account_to_csv(api_context, admin_token, test_data, create_and_del_account):
    """Тест на експорт статистики SIM-карт за дитячим акаунтом в файл."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.export_simcard_statistics_for_child_account_to_file(
        account_id=test_data["account_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="sim_card_statistics.csv"', f"Expected Content-Disposition: attachment; filename=sim_card_statistics.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@T6d84ba20')
def test_get_auth_account_simcard_statistics(api_context, admin_token):
    """Тест на отримання статистики SIM-карт за авторизованим акаунтом."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.get_auth_account_simcard_statistics(
        page=1,
        per_page=10,
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tb2b4befe')
def test_export_simcard_statistics_to_xls(api_context, admin_token):
    """Тест на експорт статистики SIM-карт за авторизованим акаунтом в файл."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.export_simcard_statistics_to_file(
        file_ext="excel",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="sim_card_statistics.xls"', f"Expected Content-Disposition: attachment; filename=sim_card_statistics.xls, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ta7b4832c')
def test_export_simcard_statistics_to_csv(api_context, admin_token):
    """Тест на експорт статистики SIM-карт за авторизованим акаунтом в файл."""
    sim_card_api = SimCardAPI(api_context, admin_token)
    response = sim_card_api.export_simcard_statistics_to_file(
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="sim_card_statistics.csv"', f"Expected Content-Disposition: attachment; filename=sim_card_statistics.csv, but got: {response.headers.get('Content-Disposition')}"