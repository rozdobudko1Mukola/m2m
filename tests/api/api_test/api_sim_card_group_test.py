import pytest
from pytest import mark
from pages.api.sim_card_group_api import SimCardGroupAPI 
from playwright.sync_api import expect


# Fixtures ---------------------------------------------------------------------

@pytest.fixture(scope="function")
def create_new_simcard_group(api_context, admin_token, test_data):
    """Тест на створення нової групи SIM-карт."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.create_new_simcard_group(
        name="Test Group",
        groupType="OPERATOR",
        icon="KYIVSTAR"
    )
    expect(response).to_be_ok()
    
    json_data = response.json()
    test_data["simcard_group_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def remove_simcard_group(api_context, admin_token, test_data):
    """Тест на видалення групи SIM-карт."""
    yield

    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.remove_simcard_group(test_data["simcard_group_id"])
    expect(response).to_be_ok()
    test_data.pop("simcard_group_id", None)


@pytest.fixture(scope="function")
def add_simcard_to_group(api_context, admin_token, test_data):
    """Тест на додавання SIM-карти до групи."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.add_simcard_to_group(
        test_data["simcard_group_id"],
        test_data["simcard_id"]
    )
    expect(response).to_be_ok()

    yield


# Test for the SimCard API ---------------------------------------------------
@mark.api
@mark.smoke
@mark.testomatio('@Tttttt910')
def test_create_new_simcard_group(api_context, admin_token, test_data, remove_simcard_group):
    """Тест на створення нової групи SIM-карт."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.create_new_simcard_group(
        name="Test Group",
        groupType="OPERATOR",
        icon="KYIVSTAR"
    )
    expect(response).to_be_ok()
    
    json_data = response.json()
    test_data["simcard_group_id"] = json_data.get("id")


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt903')
def test_remove_simcard_group(api_context, admin_token, test_data, create_new_simcard_group):
    """Тест на видалення групи SIM-карт."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.remove_simcard_group(test_data["simcard_group_id"])
    expect(response).to_be_ok()
    test_data.pop("simcard_group_id", None)


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt901')
def test_get_simcard_group_by_id(api_context, admin_token, test_data, create_add_remove_simcard_group):
    """Тест на отримання групи SIM-карт по ID."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.get_simcard_group_by_id(test_data["simcard_group_id"])
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data.get("id") == test_data["simcard_group_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt902')
def test_update_simcard_group_properties(api_context, admin_token, test_data, create_add_remove_simcard_group):
    """Тест на оновлення властивостей групи SIM-карт."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.update_simcard_group_properties(
        test_data["simcard_group_id"],
        name="Updated Group"
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data.get("name") == "Updated Group"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt909')
def test_retrieve_a_list_of_simcard_groups_with_pagination(api_context, admin_token):
    """Тест на отримання списку груп SIM-карт з пагінацією."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.retrieve_a_list_of_simcard_groups_with_pagination(
        page=1,
        size=10
    )
    expect(response).to_be_ok()
    json_data = response.json()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt911')
def test_add_simcard_to_group(api_context, admin_token, test_data, create_add_remove_simcard_group, create_and_remove_simcard):
    """Тест на додавання SIM-карти до групи."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.add_simcard_to_group(
        test_data["simcard_group_id"],
        test_data["simcard_id"]
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data[0].get("id") == test_data["simcard_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt912')
def test_remove_simcard_from_group(api_context, admin_token, test_data, create_add_remove_simcard_group, create_and_remove_simcard, add_simcard_to_group):
    """Тест на видалення SIM-карти з групи."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)

    response = sim_card_group_api.remove_simcard_from_group( # remove simcard from group
        test_data["simcard_group_id"],
        test_data["simcard_id"]
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt916')
def test_retrieve_a_list_of_simcards_from_group(api_context, admin_token, test_data, create_add_remove_simcard_group, create_and_remove_simcard, add_simcard_to_group):
    """Тест на отримання списку SIM-карт з групи."""
    sim_card_group_api = SimCardGroupAPI(api_context, admin_token)
    response = sim_card_group_api.retrieve_a_list_of_simcards_from_group(test_data["simcard_group_id"])
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data[0].get("id") == test_data["simcard_id"]
