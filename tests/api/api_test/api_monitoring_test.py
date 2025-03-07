import pytest
from pytest import mark
from pages.api.monitoring_api import monitoringAPI
from playwright.sync_api import expect


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt990')
def test_search_monitoring_devices_by_address_or_name(api_context, token, pre_and_post_conditions_device):
    monitoring = monitoringAPI(api_context, token)
    response = monitoring.search_monitoring_devices_by_address_or_name(search="")
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt991')
def test_retrieve_a_list_of_monitoring_devices_with_pagination(api_context, token, test_data, pre_and_post_conditions_device):
    monitoring = monitoringAPI(api_context, token)
    response = monitoring.retrieve_a_list_of_monitoring_devices_with_pagination(
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.json()['items'][0]['device']['id'] == test_data['device_id']


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt992')
def test_retrieve_a_list_of_a_monitoring_device_group(api_context, token, test_data, create_and_del_device_group):
    monitoring = monitoringAPI(api_context, token)
    response = monitoring.retrieve_a_list_of_a_monitoring_device_group(test_data['device_group_id'])
    expect(response).to_be_ok()
    print(response.json())
