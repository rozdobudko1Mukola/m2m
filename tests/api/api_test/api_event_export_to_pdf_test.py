import pytest
from pytest import mark
from pages.api.event_export_to_pdf import ExportPdfAPI
from playwright.sync_api import expect


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1041')
def test_export_report_template_to_pdf(api_context, token, test_data, pre_and_post_conditions_device, create_and_del_report_template):
    """Тест на експорт шаблону звіту в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_report_template_to_pdf(
        templateId=test_data["template_id"],
        elementId=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="template_report.pdf"', f"Expected Content-Disposition: attachment; filename=template_report.pdf, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1042')
def test_export_report_for_geofence_devices_to_pdf(api_context, token, test_data, create_and_remove_geofence):
    """Тест на експорт звіту для пристроїв геозони в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_report_for_geofence_devices_to_pdf(
        geofenceId=test_data["geofence_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="geofence_devices.pdf"', f"Expected Content-Disposition: attachment; filename=geofence_devices.pdf, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1043')
def test_export_report_trips_for_device_to_pdf(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на експорт звіту по поїздкам для пристрою в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_report_trips_for_device_to_pdf(
        deviceId=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_trips.pdf"', f"Expected Content-Disposition: attachment; filename=device_trips.pdf, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1044')
def test_export_summary_report_for_single_device_to_pdf(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на експорт зведеного звіту для одного пристрою в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_summary_report_for_single_device_to_pdf(
        deviceId=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_summary.pdf"', f"Expected Content-Disposition: attachment; filename=device_summary.pdf, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1045')
def test_export_report_a_stops_for_device_to_pdf(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на експорт звіту по зупинкам для пристрою в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_report_a_stops_for_device_to_pdf(
        deviceId=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_stops.pdf"', f"Expected Content-Disposition: attachment; filename=device_stops.pdf, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1046')
def test_export_report_on_the_device_entry_into_the_geofence_to_pdf(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на експорт звіту по входу пристрою в геозону в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_report_on_the_device_entry_into_the_geofence_to_pdf(
        deviceId=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_geofences.pdf"', f"Expected Content-Disposition: attachment; filename=device_geofences.pdf, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1047')
def test_export_report_trips_for_devices_group_to_pdf(api_context, token, test_data, create_and_del_device_group):
    """Тест на експорт звіту по поїздкам для групи пристроїв в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_report_trips_for_devices_group_to_pdf(
        groupId=test_data["device_group_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_trips.pdf"', f"Expected Content-Disposition: attachment; filename=device_group_trips.pdf, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1048')
def test_export_summary_report_for_devices_group_to_pdf(api_context, token, test_data, create_and_del_device_group):
    """Тест на експорт зведеного звіту для групи пристроїв в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_summary_report_for_devices_group_to_pdf(
        groupId=test_data["device_group_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_summary.pdf"', f"Expected Content-Disposition: attachment; filename=device_group_summary.pdf, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1049')
def test_export_report_a_stops_for_devices_group_to_pdf(api_context, token, test_data, create_and_del_device_group):
    """Тест на експорт звіту по зупинкам для групи пристроїв в PDF."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.export_report_a_stops_for_devices_group_to_pdf(
        groupId=test_data["device_group_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_group_stops.pdf"', f"Expected Content-Disposition: attachment; filename=device_group_stops.pdf, but got: {response.headers.get('Content-Disposition')}"


#Event----------------------------------------------------------------------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1040')
def test_retrieve_latest_10_seconds_ago_devices_events(api_context, token):
    """Тест на отримання останніх подій пристроїв за останні 10 секунд."""
    export_pdf_api = ExportPdfAPI(api_context, token)
    response = export_pdf_api.retrieve_latest_10_seconds_ago_devices_events()
    expect(response).to_be_ok()
