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
@mark.testomatio('@Tttttt825')
def test_get_a_report_trips_for_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання звіту про поїздки пристрою."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_a_report_trips_for_device(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt826')
def test_export_report_trips_for_device_to_xls(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо експорт звіту про поїздки пристрою в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_trips_for_device_to_file(
        device_id=test_data["device_id"],
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_trips.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt827')
def test_export_report_trips_for_device_to_csv(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо експорт звіту про поїздки пристрою в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_trips_for_device_to_file(
        device_id=test_data["device_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_trips.csv"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt828')
def test_get_a_summary_report_for_single_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання зведеного звіту по пристрою."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_a_summary_report_for_single_device(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt829')
def test_export_summary_report_for_single_device_to_xls(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо експорт зведеного звіту по пристрою в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_summary_report_for_single_device_to_file(
        device_id=test_data["device_id"],
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_summary.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt830')
def test_export_summary_report_for_single_device_to_csv(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо експорт зведеного звіту по пристрою в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_summary_report_for_single_device_to_file(
        device_id=test_data["device_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_summary.csv"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt831')
def test_get_a_report_on_device_stops(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання звіту про зупинки пристрою."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_a_report_on_device_stops(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt832')
def test_export_report_on_device_stops_to_xls(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо експорт звіту про зупинки пристрою в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_on_device_stops_to_file(
        device_id=test_data["device_id"],
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_stops.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt833')
def test_export_report_on_device_stops_to_csv(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо експорт звіту про зупинки пристрою в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_on_device_stops_to_file(
        device_id=test_data["device_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_stops.csv"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt834')
def test_get_a_report_on_the_device_entry_into_the_geofence(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо отримання звіту про в'їзд пристрою в геозону."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_a_report_on_the_device_entry_into_the_geofence(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt835')
def test_export_report_on_the_device_entry_into_the_geofence_to_xls(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо експорт звіту про в'їзд пристрою в геозону в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_on_the_device_entry_into_the_geofence_to_file(
        device_id=test_data["device_id"],
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_geofences.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt836')
def test_export_report_on_the_device_entry_into_the_geofence_to_csv(api_context, token, test_data, pre_and_post_conditions_device):
    """Тестуємо експорт звіту про в'їзд пристрою в геозону в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_on_the_device_entry_into_the_geofence_to_file(
        device_id=test_data["device_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_geofences.csv"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt837')
def test_get_a_report_trips_for_devices_group(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо отримання звіту про поїздки групи пристроїв."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_a_report_trips_for_devices_group(
        devices_group_id=test_data["device_group_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt838')
def test_export_report_trips_for_devices_group_to_xls(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо експорт звіту про поїздки групи пристроїв в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_trips_for_devices_group_to_file(
        devices_group_id=test_data["device_group_id"],
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_trips.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt839')
def test_export_report_trips_for_devices_group_to_csv(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо експорт звіту про поїздки групи пристроїв в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_trips_for_devices_group_to_file(
        devices_group_id=test_data["device_group_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_trips.csv"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt840')
def test_get_a_summary_report_for_devices_group(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо отримання зведеного звіту по групі пристроїв."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_a_summary_report_for_devices_group(
        devices_group_id=test_data["device_group_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt841')
def test_export_summary_report_for_devices_group_to_xls(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо експорт зведеного звіту по групі пристроїв в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_summary_report_for_devices_group_to_file(
        devices_group_id=test_data["device_group_id"],
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_summary.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt842')
def test_export_summary_report_for_devices_group_to_csv(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо експорт зведеного звіту по групі пристроїв в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_summary_report_for_devices_group_to_file(
        devices_group_id=test_data["device_group_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_summary.csv"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt843')
def test_get_report_of_stops_for_devices_group(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо отримання звіту про зупинки групи пристроїв."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.get_report_of_stops_for_devices_group(
        devices_group_id=test_data["device_group_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt844')
def test_export_report_of_stops_for_devices_group_to_xls(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо експорт звіту про зупинки групи пристроїв в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_of_stops_for_devices_group_to_file(
        devices_group_id=test_data["device_group_id"],
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_stops.xls"', f"Wrong file name: {response.headers.get('content-disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt845')
def test_export_report_of_stops_for_devices_group_to_csv(api_context, token, test_data, create_and_del_device_group):
    """Тестуємо експорт звіту про зупинки групи пристроїв в файл."""
    reports_api = ReportsAPI(api_context, token)

    response = reports_api.export_report_of_stops_for_devices_group_to_file(
        devices_group_id=test_data["device_group_id"],
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_stops.csv"', f"Wrong file name: {response.headers.get('content-disposition')}"