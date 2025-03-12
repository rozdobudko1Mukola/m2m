import pytest
from pytest import mark
from pages.api.google_server_keys_api import GoolgeServerKeys
from playwright.sync_api import expect

# Fixtures ---------------------------------------------------------------------

@pytest.fixture(scope='function')
def remove_google_server_api_key_by_id(api_context, admin_token, test_data):

    yield

    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.remove_google_server_api_key_by_id(test_data['google_server_key_id'])
    expect(response).to_be_ok()


@pytest.fixture(scope='function')
def add_new_google_server_api_key(api_context, admin_token, test_data):
    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.add_new_google_server_api_key("AIzaSyAznJXMIX5FS_no6OdPrvroH3BA-laWATU2")
    expect(response).to_be_ok()
    test_data['google_server_key_id'] = response.json()['id']

    yield


@pytest.fixture(scope='function')
def add_and_remove_google_server_api_key_by_id(api_context, admin_token, test_data):
    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.add_new_google_server_api_key("AIzaSyAznJXMIX5FS_no6OdPrvroH3BA-laWATU51")
    expect(response).to_be_ok()
    test_data['google_server_key_id'] = response.json()['id']

    yield

    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.remove_google_server_api_key_by_id(test_data['google_server_key_id'])
    expect(response).to_be_ok()

# Tests ------------------------------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1770')
def test_get_actual_server_google_key_for_maps(api_context, admin_token):
    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.get_actual_server_google_key_for_maps()
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1766')
def test_add_new_google_server_api_key(api_context, admin_token, test_data, remove_google_server_api_key_by_id):
    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.add_new_google_server_api_key("AIzaSyAznJXMIX5FS_no6OdPrvroH3BA-laWATU1")
    expect(response).to_be_ok()
    test_data['google_server_key_id'] = response.json()['id']


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1765')
def test_retrieve_list_of_all_google_server_api_keys(api_context, admin_token):
    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.retrieve_list_of_all_google_server_api_keys()
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1768')
def test_remove_google_server_api_key_by_id(api_context, admin_token, test_data, add_new_google_server_api_key):
    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.remove_google_server_api_key_by_id(test_data['google_server_key_id'])
    expect(response).to_be_ok()

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1767')
def test_update_google_server_api_key_by_id(api_context, admin_token, test_data, add_and_remove_google_server_api_key_by_id):
    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.update_google_server_api_key_by_id(test_data['google_server_key_id'], "AIzaSyAznJXMIX5FS_no6OdPrvroH3BA-laWATU5")
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1769')
def test_get_google_server_api_key_by_id(api_context, admin_token, test_data, add_and_remove_google_server_api_key_by_id):
    google_server_keys = GoolgeServerKeys(api_context, admin_token)
    response = google_server_keys.get_google_server_api_key_by_id(test_data['google_server_key_id'])
    expect(response).to_be_ok()
