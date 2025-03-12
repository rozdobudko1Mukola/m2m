import pytest
from pytest import mark
from pages.api.timezone_api import TimezoneAPI 
from playwright.sync_api import expect

@mark.api
@mark.smoke
@mark.testomatio('@Tttttt898')
def test_retrieve_a_list_of_available_timezones(api_context, token):
    """Тест на отримання списку доступних часових зон."""
    timezone_api = TimezoneAPI(api_context, token)
    response = timezone_api.retrieve_a_list_of_available_timezones()
    expect(response).to_be_ok()
    assert len(response.json()) > 0