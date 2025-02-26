import pytest
from pytest import mark
from playwright.sync_api import expect
from pages.api.report_templates_api import ReportTemplatesAPI


# Fixtures for the test ReportTemplatesAPI
@pytest.fixture(scope="function")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}


@pytest.fixture(scope="function")
def create_new_report_template(api_context, token, test_data):
    """Передумова на створення нового шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template(
        name="Test Report Template",
        elementType="DEVICE"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["template_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def remove_report_template(api_context, token, test_data):
    """Фікстура на видалення шаблону звіту."""

    yield

    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.remove_report_template(test_data["template_id"])
    expect(response).to_be_ok()
    test_data.pop("template_id", None)


@pytest.fixture(scope="function")
def create_new_report_template_chart(api_context, token, test_data):
    """Передумова на створення нового графіка в шаблоні звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template_chart(
        template_id=test_data["template_id"],
        name="Test Chart",
        selectedSensors=["SPEED"]
        )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["chart_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def remove_report_template_chart(api_context, token, test_data):
    """Фікстура на видалення графіка з шаблону звіту."""

    yield

    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.remove_report_template_chart(
        template_id=test_data["template_id"],
        chart_id=test_data["chart_id"]
        )
    expect(response).to_be_ok()
    test_data.pop("chart_id", None)


@pytest.fixture(scope="function")
def create_new_report_template_table(api_context, token, test_data):
    """Передумова на створення нової таблиці в шаблоні звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template_table(
        template_id=test_data["template_id"],
        title="Test Table",
        tableType="DEVICE_REFILL",
        tableColumns=["REFILL_START_TIME"]
        )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["table_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def remove_report_template_table(api_context, token, test_data):
    """Фікстура на видалення таблиці з шаблону звіту."""

    yield

    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.remove_report_template_table(
        template_id=test_data["template_id"],
        table_id=test_data["table_id"]
        )
    expect(response).to_be_ok()
    test_data.pop("table_id", None)


# Tests for the ReportTemplatesAPI

@mark.smoke
@mark.api
@mark.testomatio('@Tttttt865')
def test_create_new_report_template(api_context, token, test_data, remove_report_template):
    """Тест на створення нового шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template(
        name="Test Report Template",
        elementType="DEVICE"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("name") == "Test Report Template"
    test_data["template_id"] = json_data.get("id")


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt862')
def test_remove_report_template(api_context, token, test_data, create_new_report_template):
    """Тест на видалення шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.remove_report_template(test_data["template_id"])
    expect(response).to_be_ok()
    test_data.pop("template_id", None)


@mark.smoke
@mark.api
@mark.testomatio('@Ttttt1726')
def test_create_new_report_template_chart(api_context, token, test_data, create_and_del_report_template, remove_report_template_chart):
    """Тест на створення нового графіка в шаблоні звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template_chart(
        template_id=test_data["template_id"],
        name="Test Chart",
        selectedSensors=["SPEED"]
        )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("name") == "Test Chart"
    test_data["chart_id"] = json_data.get("id")


@mark.smoke
@mark.api
@mark.testomatio('@Ttttt1724')
def test_remove_report_template_chart(api_context, token, test_data, create_and_del_report_template, create_new_report_template_chart):
    """Тест на видалення графіка з шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.remove_report_template_chart(
        template_id=test_data["template_id"],
        chart_id=test_data["chart_id"]
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt867')
def test_create_new_report_template_table(api_context, token, test_data, create_and_del_report_template, remove_report_template_table):
    """Тест на створення нової таблиці в шаблоні звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.create_new_report_template_table(
        template_id=test_data["template_id"],
        title="Test Table",
        tableType="DEVICE_REFILL",
        tableColumns=["REFILL_START_TIME"]
        )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("title") == "Test Table"
    test_data["table_id"] = json_data.get("id")


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt859')
def test_remove_report_template_table(api_context, token, test_data, create_and_del_report_template, create_new_report_template_table):
    """Тест на видалення таблиці з шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.remove_report_template_table(
        template_id=test_data["template_id"],
        table_id=test_data["table_id"]
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt857')
def test_get_report_template_table_by_id(api_context, token, test_data, create_and_del_report_template, create_and_del_report_template_table):
    """Тест на отримання таблиці з шаблону звіту по id."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.get_report_template_table_by_id(
        template_id=test_data["template_id"],
        table_id=test_data["table_id"]
        )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("id") == test_data["table_id"]


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt858')
def test_update_report_template_table_properties(api_context, token, test_data, create_and_del_report_template, create_and_del_report_template_table):
    """Тест на оновлення властивостей таблиці в шаблоні звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.update_report_template_table_properties(
        template_id=test_data["template_id"],
        table_id=test_data["table_id"],
        title="Updated Test Table",
        tableType="DEVICE_REFILL",
        tableColumns=["REFILL_START_TIME", "REFILL_END_TIME"]
        )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("title") == "Updated Test Table"


@mark.smoke
@mark.api
@mark.testomatio('@Ttttt1722')
def test_get_report_template_chart_by_id(api_context, token, test_data, create_and_del_report_template, create_and_del_report_template_chart):
    """Тест на отримання графіка з шаблону звіту по id."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.get_report_template_chart_by_id(
        template_id=test_data["template_id"],
        chart_id=test_data["chart_id"]
        )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("id") == test_data["chart_id"]


@mark.smoke
@mark.api
@mark.testomatio('@Ttttt1723')
def test_update_report_template_chart_properties(api_context, token, test_data, create_and_del_report_template, create_and_del_report_template_chart):
    """Тест на оновлення властивостей графіка в шаблоні звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.update_report_template_chart_properties(
        template_id=test_data["template_id"],
        chart_id=test_data["chart_id"],
        name="Updated Test Chart",
        selectedSensors=["SPEED"]
        )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("name") == "Updated Test Chart"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt860')
def test_get_report_template_by_id(api_context, token, test_data, create_and_del_report_template):
    """Тест на отримання шаблону звіту по id."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.get_report_template_by_id(test_data["template_id"])
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("id") == test_data["template_id"]


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt861')
def test_update_report_template_properties(api_context, token, test_data, create_and_del_report_template):
    """Тест на оновлення властивостей шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.update_report_template_properties(
        template_id=test_data["template_id"],
        elementType="DEVICE_GROUP"
        )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("elementType") == "DEVICE_GROUP"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt863')
def test_rename_report_template(api_context, token, test_data, create_and_del_report_template):
    """Тест на зміну назви шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.rename_report_template(
        template_id=test_data["template_id"],
        name="Updated Test Report Template"
        )
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data.get("name") == "Updated Test Report Template"


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt864')
def test_retrieve_list_of_reports_templates(api_context, token, test_data, create_and_del_report_template):
    """Тест на отримання списку шаблонів звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.retrieve_list_of_reports_templates()
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data[0]["id"] == test_data["template_id"]


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt866')
def test_retrieve_list_of_report_tables(api_context, token, test_data, create_and_del_report_template, create_and_del_report_template_table):
    """Тест на отримання списку таблиць з шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.retrieve_list_of_report_tables(test_data["template_id"])
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data[0]["id"] == test_data["table_id"]


@mark.smoke
@mark.api
@mark.testomatio('@Ttttt1725')
def test_retrieve_list_of_report_charts(api_context, token, test_data, create_and_del_report_template, create_and_del_report_template_chart):
    """Тест на отримання списку графіків з шаблону звіту."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.retrieve_list_of_report_charts(test_data["template_id"])
    expect(response).to_be_ok()

    json_data = response.json()
    assert json_data[0]["id"] == test_data["chart_id"]


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt870')
def test_execute_the_report_by_template(api_context, token, test_data, create_and_del_report_template, create_and_del_report_template_table, pre_and_post_conditions_device):
    """Тест на виконання звіту за шаблоном."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.execute_the_report_by_template(
        template_id=test_data["template_id"],
        elementId=test_data["device_id"],
        dateFrom="2021-01-01T00:00:00Z",
        dateTo="2021-01-01T23:59:59Z"
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt868')
def test_get_report_template_permission_for_child(api_context, token, test_data, create_and_del_report_template, create_and_del_user_by_accaunt):
    """Тест на отримання прав доступу до шаблону звіту для дитячого користувача."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.get_report_template_permission_for_child(
        template_id=test_data["template_id"],
        user_id=test_data["user_id"]
        )
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('@Tttttt869')
def test_update_report_template_permission_for_child(api_context, token, test_data, create_and_del_report_template, create_and_del_user_by_accaunt):
    """Тест на оновлення прав доступу до шаблону звіту для дитячого користувача."""
    report_templates_api = ReportTemplatesAPI(api_context, token)
    response = report_templates_api.update_report_template_permission_for_child(
        template_id=test_data["template_id"],
        user_id=test_data["user_id"],
        permission="VIEW_ELEMENT",
        state="true"
        )
    expect(response).to_be_ok()
    assert response.json().get("hasViewElement") is True