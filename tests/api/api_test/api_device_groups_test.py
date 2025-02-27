import pytest
from pytest import mark
from pages.api.device_groups_api import DeviceGroupsAPI
from playwright.sync_api import expect


# Fixtures for the test DeviceGroupsAPI
@pytest.fixture(scope="function")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}


@pytest.fixture(scope="function")
def create_new_device_group(api_context, token, test_data):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.create_new_device_group(
        name="Test Device Group"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["device_group_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def remove_device_group(api_context, token, test_data):
    yield

    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.remove_device_group(test_data["device_group_id"])
    expect(response).to_be_ok()


# Test for the DeviceGroupsAPI
@mark.api
@mark.smoke
@mark.testomatio('@Tttttt964')
def test_create_new_device_group(api_context, token, test_data, remove_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.create_new_device_group(
        name="Test Device Group"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["device_group_id"] = json_data.get("id")


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt968')
def test_remove_device_group(api_context, token, test_data, create_new_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.remove_device_group(test_data["device_group_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('')
def test_retrieve_devices_group_related_permissions(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.retrieve_devices_group_related_permissions(test_data["device_group_id"])
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("VIEW_ELEMENT") is True


@mark.api
@mark.smoke
@mark.testomatio('')
def test_update_devices_group_related_permissions(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.update_devices_group_related_permissions(
        test_data["device_group_id"], 
        permission="ADMIN_FIELDS_VIEW",
        state="false"
        )
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("ADMIN_FIELDS_VIEW") is False


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt955')
def test_rename_devices_group(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.rename_devices_group(test_data["device_group_id"], name="New Test Device Group")
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("name") == "New Test Device Group"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt956')
def test_retrieve_custom_fields_for_devices_group(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.retrieve_custom_fields_for_devices_group(test_data["device_group_id"])
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("customFields") is None


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt958')
def test_retrieve_admin_fields_for_devices_group(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.retrieve_admin_fields_for_devices_group(test_data["device_group_id"])
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("adminFields") is None


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt957')
def test_update_devices_group_custom_fields(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.update_devices_group_custom_fields(
        test_data["device_group_id"], 
        customFields="{\"custom name\":\"custom value\"}"
        )
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("customFields") == "{\"custom name\":\"custom value\"}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt959')
def test_update_devices_group_admin_fields(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.update_devices_group_admin_fields(
        test_data["device_group_id"], 
        adminFields="{\"admin name\":\"admin value\"}"
        )
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("adminFields") == "{\"admin name\":\"admin value\"}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt962')
def test_add_device_to_group(api_context, token, test_data, create_and_del_device_group, pre_and_post_conditions_device):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.add_device_to_group(
        test_data["device_group_id"], 
        device_id=test_data["device_id"]
        )
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data[0]['id'] == test_data["device_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt963')
def test_retrieve_a_list_of_devices_groups_with_pagination(api_context, token, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.retrieve_a_list_of_devices_groups_with_pagination(page=1, per_page=10)
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data['items'][0]["name"] == "Test Device Group"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt965')
def test_retrieve_a_list_of_device_from_group(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.retrieve_a_list_of_device_from_group(test_data["device_group_id"])
    expect(response).to_be_ok()
    
    json_data = response.json()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt967')
def test_get_devices_group_by_id(api_context, token, test_data, create_and_del_device_group):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.get_devices_group_by_id(test_data["device_group_id"])
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("id") == test_data["device_group_id"]  


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt969')
def test_remove_device_from_group(api_context, token, test_data, create_and_del_device_group, pre_and_post_conditions_device):
    device_groups = DeviceGroupsAPI(api_context, token)

    response = device_groups.add_device_to_group(
        test_data["device_group_id"], 
        device_id=test_data["device_id"]
        )
    expect(response).to_be_ok()
    
    response = device_groups.remove_device_from_group(
        test_data["device_group_id"], 
        device_id=test_data["device_id"]
        )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt961')
def test_set_devices_group_permission_for_child_user(api_context, token, test_data, create_and_del_device_group, create_and_del_user_by_accaunt):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.set_devices_group_permission_for_child_user(
        test_data["device_group_id"], 
        user_id=test_data["user_id"], 
        permission="VIEW_ELEMENT",
        state="true"
        )
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("VIEW_ELEMENT") is True


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt960')
def test_retrieve_devices_group_permissions_for_child_user(api_context, token, test_data, create_and_del_device_group, create_and_del_user_by_accaunt):
    device_groups = DeviceGroupsAPI(api_context, token)
    response = device_groups.retrieve_devices_group_permissions_for_child_user(
        test_data["device_group_id"], 
        user_id=test_data["user_id"]
        )
    expect(response).to_be_ok()
    
    json_data = response.json()
    assert json_data.get("VIEW_ELEMENT") is False