import pytest
from pytest import mark
from pages.api.position_api import PositionAPI
from playwright.sync_api import expect


# Test for the Position API ---------------------------------------------------
@mark.api
@mark.smoke
@mark.testomatio('@Tttttt917')
def test_retrieve_a_list_of_devices_positions(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на отримання списку позицій пристроїв."""
    position_api = PositionAPI(api_context, token)
    response = position_api.retrieve_a_list_of_devices_positions(
        devicesIds=[test_data["device_id"]]
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt918')
def test_get_details_the_track_by_speed_and_optional_trips_or_stops(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на отримання деталей треку за швидкістю та опціональними поїздками або зупинками."""
    position_api = PositionAPI(api_context, token)
    response = position_api.get_details_the_track_by_speed_and_optional_trips_or_stops(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z",
        useStops="true",
        useTrips="true"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt919')
def test_retrieve_a_list_of_device_track_positions_by_interval(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на отримання списку позицій треку пристрою за інтервалом."""
    position_api = PositionAPI(api_context, token)
    response = position_api.retrieve_a_list_of_device_track_positions_by_interval(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1734')
def test_retrieve_a_list_of_device_track_positions_by_trips(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на отримання списку позицій треку пристрою за поїздками."""
    position_api = PositionAPI(api_context, token)
    response = position_api.retrieve_a_list_of_device_track_positions_by_trips(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1735')
def test_calculate_track_distance_by_interval_of_positions_in_kilometers(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на розрахунок відстані треку за інтервалом позицій в кілометрах."""
    position_api = PositionAPI(api_context, token)
    response = position_api.calculate_track_distance_by_interval_of_positions_in_kilometers(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt920')
def test_get_device_position_by_interval_with_pagination(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на отримання позицій пристрою за інтервалом з пагінацією."""
    position_api = PositionAPI(api_context, token)
    response = position_api.get_device_position_by_interval_with_pagination(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt921')
@mark.skip("Not implemented yet") # Skip this test because it is not implemented yet
def test_get_device_position_details():
    """Тест на отримання деталей позиції пристрою."""
    pass


@mark.api
@mark.smoke
@mark.testomatio('@T4e10d607')
@mark.skip("Not implemented yet") # Skip this test because it is not implemented yet
def test_delete_device_position_from_database():
    """Тест на видалення позиції пристрою."""
    pass


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt922')
@mark.skip("Актуальна інформація про позицію недоступна так як пристрій не відправляє дані.") # Skip this test because the device does not send data
def test_get_the_last_position_of_device(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на отримання останньої позиції пристрою."""
    position_api = PositionAPI(api_context, token)
    response = position_api.get_the_last_position_of_device(
        device_id=test_data["device_id"]
    )
    expect(response).to_be_ok()
    print(response.json())


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt923')
def test_export_device_positions_by_interval_to_xls(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на експорт позицій пристрою за інтервалом в файл."""
    position_api = PositionAPI(api_context, token)
    response = position_api.export_device_positions_by_interval_to_file(
        ext_file="xls",
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="positions.xls"', f"Expected Content-Disposition: attachment; filename=positions.xlsx, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt924')
def test_export_device_positions_by_interval_to_csv(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на експорт позицій пристрою за інтервалом в файл."""
    position_api = PositionAPI(api_context, token)
    response = position_api.export_device_positions_by_interval_to_file(
        ext_file="csv",
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="positions.csv"', f"Expected Content-Disposition: attachment; filename=positions.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1733')
def test_get_device_geojson_track(api_context, token, test_data, pre_and_post_conditions_device):
    """Тест на отримання геоjson треку пристрою."""
    position_api = PositionAPI(api_context, token)
    response = position_api.get_device_geojson_track(
        device_id=test_data["device_id"],
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
