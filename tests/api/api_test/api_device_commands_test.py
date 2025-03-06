import pytest
from pytest import mark
from pages.api.device_commands_api import deviceCommandsAPI
from playwright.sync_api import expect


# Fixtures for deviceCommandsAPI ------------------------------------------------

@pytest.fixture(scope="function")
def create_command_for_device(api_context, token, test_data):
    """Create command for device."""
    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.create_command_for_device(
        device_id=test_data["device_id"],
        description="test name if command",
        data="Api test massage in command",
        type="CUSTOM"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["command_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def remove_device_command(api_context, token, test_data):
    """Remove command for device."""

    yield

    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.remove_device_command_by_id(test_data["device_id"], test_data["command_id"])
    expect(response).to_be_ok()


# Test for the deviceCommandsAPI ------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Tttttt476')
def test_get_device_command_by_id(api_context, token, test_data, pre_and_post_conditions_device, create_and_remove_command_for_device):
    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.get_device_command_by_id(test_data["device_id"], test_data["command_id"])
    expect(response).to_be_ok()
    assert response.json().get("id") == test_data["command_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt479')
def test_update_device_command(api_context, token, test_data, pre_and_post_conditions_device, create_and_remove_command_for_device):
    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.update_device_command(
        test_data["device_id"],
        test_data["command_id"],
        description="new test name command",
        type="CUSTOM"
    )
    expect(response).to_be_ok()
    assert response.json().get("id") == test_data["command_id"]
    assert response.json().get("description") == "new test name command"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt480')
def test_remove_device_command_by_id(api_context, token, test_data, pre_and_post_conditions_device, create_command_for_device):
    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.remove_device_command_by_id(test_data["device_id"], test_data["command_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1736')
def test_retrieve_a_list_of_device_commands(api_context, token, test_data, pre_and_post_conditions_device, create_and_remove_command_for_device):
    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.retrieve_a_list_of_device_commands(test_data["device_id"])
    expect(response).to_be_ok()
    assert response.json()[0].get("id") == test_data["command_id"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt477')
def test_create_command_for_device(api_context, token, test_data, pre_and_post_conditions_device, remove_device_command):
    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.create_command_for_device(
        device_id=test_data["device_id"],
        description="test name command",
        data="Api test massage in command",
        type="CUSTOM"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["command_id"] = json_data.get("id")
    assert json_data.get("description") == "test name command"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt478')
def test_dispatch_a_command_to_device(api_context, token, test_data, pre_and_post_conditions_device, create_and_remove_command_for_device):
    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.dispatch_a_command_to_device(test_data["device_id"], test_data["command_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1737')
def test_retrieve_list_of_available_commands(api_context, token, test_data, pre_and_post_conditions_device, create_and_remove_command_for_device):
    device_commands = deviceCommandsAPI(api_context, token)
    response = device_commands.retrieve_list_of_available_commands(test_data["device_id"])
    expect(response).to_be_ok()
    assert response.json()[0] == "CUSTOM"