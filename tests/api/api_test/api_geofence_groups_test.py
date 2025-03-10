import pytest
from pytest import mark
from pages.api.geofence_groups_api import GeofenceGroupsAPI
from playwright.sync_api import expect

# Fixture -----------------------------------------------------------------------

@pytest.fixture(scope="function")
def create_new_geofences_group(api_context, token, test_data):
    """Створення нової групи геозон."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.create_new_geofences_group(
        name="Test group",
        customFields="",
        adminFields=""
    )
    expect(response).to_be_ok()
    test_data["geofence_group_id"] = response.json()["id"]

    yield


@pytest.fixture(scope="function")
def remove_geofences_group(api_context, token, test_data):
    """Видалення групи геозон."""

    yield

    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.remove_the_geofences_group(group_id=test_data["geofence_group_id"])
    expect(response).to_be_ok()


@pytest.fixture(scope="function")
def add_geofence_to_group(api_context, token, test_data):
    """Додавання геозони до групи."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.add_geofence_to_group(
        group_id=test_data["geofence_group_id"],
        geofence_id=test_data["geofence_id"]
    )
    expect(response).to_be_ok()


# Tests -------------------------------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1025')
def test_create_new_geofences_group(api_context, token, test_data, remove_geofences_group):
    """Тест на створення нової групи геозон."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.create_new_geofences_group(
        name="Test group",
        customFields="",
        adminFields=""
    )
    expect(response).to_be_ok()
    test_data["geofence_group_id"] = response.json()["id"]

    assert response.json()["name"] == "Test group"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1029')
def test_remove_geofences_group(api_context, token, test_data, create_new_geofences_group):
    """Тест на видалення групи геозон."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.remove_the_geofences_group(group_id=test_data["geofence_group_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1016')
def test_rename_geofences_group(api_context, token, test_data, create_and_remove_new_geofences_group):
    """Тест на перейменування групи геозон."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.rename_geofences_group(group_id=test_data["geofence_group_id"], new_name="New name")
    expect(response).to_be_ok()

    assert response.json()["name"] == "New name"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1017')
def test_retrieve_custom_fields_for_geofences_group(api_context, token, test_data, create_and_remove_new_geofences_group):
    """Тест на отримання додаткових полів для геозон."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.retrieve_custom_fields_for_geofences_group(group_id=test_data["geofence_group_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1018')
def test_update_geofences_group_custom_fields(api_context, token, test_data, create_and_remove_new_geofences_group):
    """Тест на оновлення додаткових полів для геозон."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.update_geofences_group_custom_fields(
        group_id=test_data["geofence_group_id"],
        custom_fields="{\"custom name\":\"custom value\"}"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1019')
def test_retrieve_admin_fields_for_geofences_group(api_context, token, test_data, create_and_remove_new_geofences_group):
    """Тест на отримання адміністративних полів для геозон."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.retrieve_admin_fields_for_geofences_group(group_id=test_data["geofence_group_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1020')
def test_update_geofences_group_admin_fields(api_context, token, test_data, create_and_remove_new_geofences_group):
    """Тест на оновлення адміністративних полів для геозон."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.update_geofences_group_admin_fields(
        group_id=test_data["geofence_group_id"],
        admin_fields="{\"admin name\":\"admin value\"}"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1021')
def test_retrieve_geofences_group_permissions_for_child_user(api_context, token, test_data, create_and_remove_new_geofences_group, create_and_del_user_by_accaunt):
    """Тест на отримання прав доступу до геозон для дочірнього користувача."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.retrieve_geofences_group_permissions_for_child_user(
        group_id=test_data["geofence_group_id"],
        child_user_id=test_data["user_id"]
    )
    expect(response).to_be_ok()
    assert response.json()['VIEW_ELEMENT'] is False


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1022')
def test_set_geofences_group_permission_for_child_user(api_context, token, test_data, create_and_remove_new_geofences_group, create_and_del_user_by_accaunt):
    """Тест на встановлення прав доступу до геозон для дочірнього користувача."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.set_geofences_group_permission_for_child_user(
        group_id=test_data["geofence_group_id"],
        child_user_id=test_data["user_id"],
        permission="VIEW_ELEMENT",
        state="true"
    )
    expect(response).to_be_ok()
    assert response.json()["VIEW_ELEMENT"] is True


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1023')
def test_add_geofence_to_group(api_context, token, test_data, create_and_remove_new_geofences_group, create_and_remove_geofence):
    """Тест на додавання геозони до групи."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.add_geofence_to_group(
        group_id=test_data["geofence_group_id"],
        geofence_id=test_data["geofence_id"]
    )
    expect(response).to_be_ok()
    assert response.json()[0]["id"] == test_data["geofence_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1024')
def test_retrieve_a_list_of_geofences_groups_with_pagination(api_context, token, test_data, create_and_remove_new_geofences_group):
    """Тест на отримання списку груп геозон з пагінацією."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.retrieve_a_list_of_geofences_groups_with_pagination()
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1028')
def test_get_geofences_group_by_id(api_context, token, test_data, create_and_remove_new_geofences_group):
    """Тест на отримання групи геозон по ID."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.get_geofences_group_by_id(group_id=test_data["geofence_group_id"])
    expect(response).to_be_ok()
    assert response.json()["id"] == test_data["geofence_group_id"]
    assert response.json()["name"] == "Test group"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1030')
def test_remove_geofence_from_group(api_context, token, test_data, create_and_remove_new_geofences_group, create_and_remove_geofence, add_geofence_to_group):
    """Тест на видалення геозони з групи."""
    geofence_groups_api = GeofenceGroupsAPI(api_context, token)
    response = geofence_groups_api.remove_geofence_from_group(
        group_id=test_data["geofence_group_id"],
        geofence_id=test_data["geofence_id"]
    )
    expect(response).to_be_ok()
