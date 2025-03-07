from pytest import mark
from pages.api.dashboard_api import DashboardAPI
from playwright.sync_api import expect


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1031')
def test_dashboard_devices_stops_duration_rating(api_context, token, test_data, pre_and_post_conditions_device):
    dashboard = DashboardAPI(api_context, token)
    response = dashboard.dashboard_devices_stops_duration_rating(
    device_id=[test_data['device_id']],
    dateFrom="2025-01-01T00:00:00Z",
    dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1032')
def test_dashboard_devices_mileage_rating(api_context, token, test_data, pre_and_post_conditions_device):
    dashboard = DashboardAPI(api_context, token)
    response = dashboard.dashboard_devices_mileage_rating(
    device_id=[test_data['device_id']],
    dateFrom="2025-01-01T00:00:00Z",
    dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1033')
def test_dashboard_devices_max_speed_rating(api_context, token, test_data, pre_and_post_conditions_device):
    dashboard = DashboardAPI(api_context, token)
    response = dashboard.dashboard_devices_max_speed_rating(
    device_id=[test_data['device_id']],
    dateFrom="2025-01-01T00:00:00Z",
    dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1034')
def test_get_devices_actual_motion_state_based_on_speed(api_context, token):
    dashboard = DashboardAPI(api_context, token)
    response = dashboard.get_devices_actual_motion_state_based_on_speed()
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1744')
def test_get_devices_connection_state(api_context, token):
    dashboard = DashboardAPI(api_context, token)
    response = dashboard.get_devices_connection_state()
    expect(response).to_be_ok()
