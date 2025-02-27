import pytest
from pytest import mark
from pages.api.geofences_api import GeofencesAPI
from playwright.sync_api import expect


# Fixtures for the test GeofencesAPI
@pytest.fixture(scope="function")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}


@pytest.fixture(scope="function")
def remove_the_geofence(api_context, token, test_data):

    yield

    geofences = GeofencesAPI(api_context, token)
    response = geofences.remove_the_geofence(test_data["geofence_id"])
    expect(response).to_be_ok()


@pytest.fixture(scope="function")
def create_new_geofence(api_context, token, test_data):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.create_new_geofence(
        name="Test Geofence",
        description="Test Geofence Description",
        area="{\"type\":\"Circle\",\"coordinates\":[30.035527000, 51.835087000],\"radius\":187.237000000,\"radius_units\":\"km\"}",
        fillColor="#0091DC",
        strokeColor="#44D600"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["geofence_id"] = json_data.get("id")

    yield


# Test for the GeofencesAPI
@mark.api
@mark.smoke
@mark.testomatio('@Tttttt977')
def test_create_new_geofence(api_context, token, test_data, remove_the_geofence):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.create_new_geofence(
        name="Test Geofence",
        description="Test Geofence Description",
        area="{\"type\":\"Circle\",\"coordinates\":[30.035527000, 51.835087000],\"radius\":187.237000000,\"radius_units\":\"km\"}",
        fillColor="#0091DC",
        strokeColor="#44D600"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["geofence_id"] = json_data.get("id")


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt972')
def test_remove_the_geofence(api_context, token, test_data, create_new_geofence):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.remove_the_geofence(test_data["geofence_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt970')
def test_get_geofence_by_id(api_context, token, test_data, create_and_remove_geofence):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.get_geofence_by_id(test_data["geofence_id"])
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data.get("id") == test_data["geofence_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt971')
def test_update_geofence_properties(api_context, token, test_data, create_and_remove_geofence):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.update_geofence_properties(
        geofence_id=test_data["geofence_id"],
        description="Updated Geofence Description",
        area="{\"type\":\"Circle\",\"coordinates\":[30.035527000, 51.835087000],\"radius\":187.237000000,\"radius_units\":\"km\"}",
        fillColor="#0091DC",
        strokeColor="#44D600"
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data.get("description") == "Updated Geofence Description"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt973')
def test_rename_geofence(api_context, token, test_data, create_and_remove_geofence):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.rename_geofence(
        geofence_id=test_data["geofence_id"],
        name="Renamed Geofence"
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data.get("name") == "Renamed Geofence"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt976')
def test_retrieve_list_of_geofences_with_pagination(api_context, token, test_data, create_and_remove_geofence):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.retrieve_list_of_geofences_with_pagination(page=1, per_page=10)
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data.get("items")[0].get("id") == test_data["geofence_id"]


@mark.api
@mark.smoke
@mark.testomatio('@T21113635')
def test_list_geofences_by_selected_ids(api_context, token, test_data, create_and_remove_geofence):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.list_geofences_by_selected_ids(geofenceIds=[test_data["geofence_id"]])
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data[0].get("id") == test_data["geofence_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt978')
def test_assign_device_to_geofence(api_context, token, test_data, create_and_remove_geofence, pre_and_post_conditions_device):
    geofences = GeofencesAPI(api_context, token)
    response = geofences.assign_device_to_geofence(geofence_id=test_data["geofence_id"], device_id=test_data["device_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt986')
def test_remove_device_from_geofence(api_context, token, test_data, create_and_remove_geofence, pre_and_post_conditions_device):
    geofences = GeofencesAPI(api_context, token)

    response = geofences.assign_device_to_geofence(geofence_id=test_data["geofence_id"], device_id=test_data["device_id"])
    expect(response).to_be_ok()

    response = geofences.remove_device_from_geofence(geofence_id=test_data["geofence_id"], device_id=test_data["device_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt989')
def test_list_assigned_geofence_device(api_context, token, test_data, create_and_remove_geofence, pre_and_post_conditions_device):
    geofences = GeofencesAPI(api_context, token)

    response = geofences.assign_device_to_geofence(geofence_id=test_data["geofence_id"], device_id=test_data["device_id"])
    expect(response).to_be_ok()

    response = geofences.list_assigned_geofence_device(geofence_id=test_data["geofence_id"])
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data[0].get("id") == test_data["device_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt987')
def test_create_copy_of_geofence(api_context, token, test_data, create_and_remove_geofence):
    geofences = GeofencesAPI(api_context, token)

    response = geofences.create_copy_of_geofence(geofence_id=test_data["geofence_id"])
    expect(response).to_be_ok()
    test_data["copied_geofence_id"] = response.json().get("id")

    response = geofences.remove_the_geofence(test_data["copied_geofence_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt974')
def test_retrieve_geofence_permissions_for_child_user(api_context, token, test_data, create_and_remove_geofence, create_and_del_user_by_accaunt):
    geofences = GeofencesAPI(api_context, token)

    response = geofences.retrieve_geofence_permissions_for_child_user(geofence_id=test_data["geofence_id"], user_id=test_data["user_id"])
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data.get("VIEW_ELEMENT") is False


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt975')
def test_set_geofence_permissions_for_child_user(api_context, token, test_data, create_and_remove_geofence, create_and_del_user_by_accaunt):
    geofences = GeofencesAPI(api_context, token)

    response = geofences.set_geofence_permissions_for_child_user(
        geofence_id=test_data["geofence_id"], 
        user_id=test_data["user_id"], 
        permission="VIEW_ELEMENT",
        state="true"
    )
    expect(response).to_be_ok()
    assert response.json().get("VIEW_ELEMENT") is True