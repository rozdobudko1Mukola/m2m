import pytest
from pytest import mark
from pages.api.reports_api import ReportsAPI
from pages.api.geofences_api import GeofencesAPI
from playwright.sync_api import expect


# Fixtures for the test ReportsAPI
@pytest.fixture(scope="function")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}


# Tests for the test ReportsAPI
@mark.api
@mark.smoke
@mark.testomatio('@Tttttt821')
def test_export_report_template_to_excel(api_context, token, test_data, create_and_del_report_template, pre_and_post_conditions_device):
    """Тест експорту шаблону звіту в Excel."""
    reports_api = ReportsAPI(api_context, token)
    response = reports_api.export_report_template_to_excel(
        report_template_id=test_data["template_id"],
        elementId=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="template_report.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt822')
def test_get_report_for_geofence_devices(api_context, token, test_data, create_and_remove_geofence):
    """Тест отримання звіту по пристроях в геозоні."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_report_for_geofence_devices(
        geofence_id=test_data["geofence_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt823')
def test_export_report_for_geofence_devices_to_file_excel(api_context, token, test_data, create_and_remove_geofence):
    """Тестуємо експорт списку пристроїв з пагінацією в Excel"""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_for_geofence_devices_to_file(
        geofence_id=test_data["geofence_id"],
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="geofence_devices.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt824')
def test_export_report_for_geofence_devices_to_file_csv(api_context, token, test_data, create_and_remove_geofence):
    """Тестуємо експорт списку пристроїв з пагінацією в csv"""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_for_geofence_devices_to_file(
        geofence_id=test_data["geofence_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="geofence_devices.csv"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('')
def test_get_a_report_trips_for_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання звіту про поїздки пристрою."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_a_report_trips_for_device(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    print(response.json())