import pytest
from pytest import mark
from pages.api.protocol_api import ProtocolAPI
from playwright.sync_api import expect


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1002')
def test_retrieve_a_list_of_device_protocols(api_context, token):
    protocol = ProtocolAPI(api_context, token)
    response = protocol.retrieve_a_list_of_device_protocols(search='')
    expect(response).to_be_ok()
    assert len(response.json()) > 0


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1003')
def test_get_device_protocol_by_model(api_context, token):
    protocol = ProtocolAPI(api_context, token)
    response = protocol.get_device_protocol_by_model(model='M2M Mobile Tracker')
    expect(response).to_be_ok()
    assert response.json()['model'] == 'M2M Mobile Tracker'
