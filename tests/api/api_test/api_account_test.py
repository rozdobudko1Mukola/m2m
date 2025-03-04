import pytest
from pytest import mark
from pages.api.account_api import AccountAPI
from pages.api.users_api import UsersAPI
from playwright.sync_api import expect


# Fixtures for the test ReportsAPI

@pytest.fixture(scope="function")
def del_user_postcondition(api_context, admin_token, test_data):
    """Фікстура видалення користувача(user) після тесту."""

    yield
    user_api = UsersAPI(api_context, admin_token)

    response = user_api.remove_child_user(test_data["user_id"])
    expect(response).to_be_ok()


# Tests for the test AccountAPI
@mark.api
@mark.smoke
@mark.testomatio('@Tttttt934')
def test_create_an_account_for_a_new_user(api_context, admin_token, test_data, del_user_postcondition):
    """Тест на створення облікового запису для нового користувача."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.create_an_account_for_a_new_user(
        email="m2m.test.auto+APIAuto@gmail.com",
        password="123456",
        language="UKRAINIAN",
        accountType="REGISTERED", 
        billingPlanTemplateId="12"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["user_id"] = json_data.get("userId")


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt935')
def test_create_an_account_from_existing_user(api_context, admin_token, test_data, create_and_del_user_by_accaunt):
    """Тест на створення облікового запису для існуючого користувача."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.create_an_account_from_existing_user(
        userId=test_data["user_id"],
        accountType="REGISTERED",
        billingPlanTemplateId="12"
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt925')
def test_get_account_by_id(api_context, admin_token, test_data, create_and_del_account):
    """Тест на отримання облікового запису по ID."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.get_account_by_id(test_data["account_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt926')
def test_update_account_properties(api_context, admin_token, test_data, create_and_del_account):
    """Тест на оновлення властивостей облікового запису."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.update_account_properties(
        account_id=test_data["account_id"],
        dealer="false",
        blockByBalance="false",
        blockByInvoice="false",
        accountType="CLIENT"
    )
    expect(response).to_be_ok()
    assert response.json()["accountType"] == "CLIENT"


@mark.api
@mark.smoke
@mark.testomatio("@Tttttt927")
@mark.skip(reason="Тест на видалення аккаунта.")
def test_remove_account(api_context, admin_token, test_data, create_and_del_account):
    """Тест на видалення аккаунта."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.remove_account(test_data["account_id"])
    expect(response).to_be_ok()
    print(response.json())


@mark.api
@mark.smoke
@mark.testomatio("@Tttttt928")
def test_update_account_state(api_context, admin_token, test_data, create_and_del_account):
    """Тест на оновлення стану облікового запису."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.update_account_state(test_data["account_id"], enabled=False)
    expect(response).to_be_ok()
    assert response.json()["enabled"] == False


@mark.api
@mark.smoke
@mark.testomatio("@Tttttt929")
def test_get_a_billing_plan_for_a_child_account(api_context, admin_token, test_data, create_and_del_account):
    """Тест на отримання плану для дочірнього облікового запису."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.get_a_billing_plan_for_a_child_account(test_data["account_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio("@Tttttt930")
def test_update_billing_plan_for_child_account(api_context, admin_token, test_data, create_and_del_account):
    """Тест на оновлення плану для дочірнього облікового запису."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.update_billing_plan_for_child_account(
        test_data["account_id"],
        name="Безкоштовний тариф",
        smsCost=1
    )
    expect(response).to_be_ok()
    assert response.json()["smsCost"] == 1.0


# @mark.api
# @mark.smoke
# @mark.testomatio()
# @mark.skip(reason="Тест на отримання знижки на план для дочірнього облікового запису.")
# def test_get_a_billing_plan_discount_for_a_child_account(api_context, admin_token, test_data, create_and_del_account):
#     """Тест на отримання знижки на план для дочірнього облікового запису."""
#     account_api = AccountAPI(api_context, admin_token)
#     response = account_api.get_a_billing_plan_discount_for_a_child_account(test_data["account_id"])
#     expect(response).to_be_ok()
#     print(response.json())


@mark.api
@mark.smoke
@mark.testomatio("@Tttttt931")
def test_make_payment_on_account(api_context, admin_token, test_data, create_and_del_account):
    """Тест на здійснення платежу на обліковий запис."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.make_payment_on_account(
        test_data["account_id"],
        operation="WITHDRAW",
        value=100,
        description="api Test payment"
    )
    expect(response).to_be_ok()


# Export to file tests for the test AccountAPI

@mark.api
@mark.smoke
@mark.testomatio('@Tb5c5a8ed')
def test_export_a_list_of_accounts_with_pagination_to_csv_file(api_context, admin_token):
    """Тест на експорт списку облікових записів з пагінацією в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_a_list_of_accounts_with_pagination_to_file(
        file_ext="csv",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="accounts.csv"', f"Expected Content-Disposition: attachment; filename=accounts.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tba9d9f04')
def test_export_a_list_of_accounts_with_pagination_to_xls_file(api_context, admin_token):
    """Тест на експорт списку облікових записів з пагінацією в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_a_list_of_accounts_with_pagination_to_file(
        file_ext="xls",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="accounts.xls"', f"Expected Content-Disposition: attachment; filename=accounts.xls, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt941')
def test_export_payment_statistics_for_child_account_to_csv_file(api_context, admin_token):
    """Тест на експорт статистики платежів для дочірнього облікового запису в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_payment_statistics_for_child_account_to_file(
        account_id="473", # id аккаунта для теста m2m.test.auto@gmail.com
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="payment_account_statistics.csv"', f"Expected Content-Disposition: attachment; filename=payment_account_statistics.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt940')
def test_export_payment_statistics_for_child_account_to_xls_file(api_context, admin_token):
    """Тест на експорт статистики платежів для дочірнього облікового запису в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_payment_statistics_for_child_account_to_file(
        account_id="473", # id аккаунта для теста m2m.test.auto@gmail.com
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="payment_account_statistics.xls"', f"Expected Content-Disposition: attachment; filename=payment_account_statistics.xls, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt944')
def test_export_device_statistics_for_child_account_to_csv_file(api_context, admin_token):
    """Тест на експорт статистики пристроїв для дочірнього облікового запису в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_device_statistics_for_child_account_to_file(
        account_id="473", # id аккаунта для теста m2m.test.auto@gmail.com
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_account_statistics.csv"', f"Expected Content-Disposition: attachment; filename=device_account_statistics.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt943')
def test_export_device_statistics_for_child_account_to_xls_file(api_context, admin_token):
    """Тест на експорт статистики пристроїв для дочірнього облікового запису в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_device_statistics_for_child_account_to_file(
        account_id="473", # id аккаунта для теста m2m.test.auto@gmail.com
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_account_statistics.xls"', f"Expected Content-Disposition: attachment; filename=device_account_statistics.xls, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt949')
def test_export_payment_statistics_to_csv_file(api_context, admin_token):
    """Тест на експорт статистики платежів в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_payment_statistics_to_file(
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="payment_statistics.csv"', f"Expected Content-Disposition: attachment; filename=payment_statistics.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt948')
def test_export_payment_statistics_to_xls_file(api_context, admin_token):
    """Тест на експорт статистики платежів в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_payment_statistics_to_file(
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="payment_statistics.xls"', f"Expected Content-Disposition: attachment; filename=payment_statistics.xls, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt952')
def test_export_device_statistics_to_csv_file(api_context, admin_token):
    """Тест на експорт статистики пристроїв в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_device_statistics_to_file(
        file_ext="csv",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_statistics.csv"', f"Expected Content-Disposition: attachment; filename=device_statistics.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@@Tttttt951')
def test_export_device_statistics_to_xls_file(api_context, admin_token):
    """Тест на експорт статистики пристроїв в файл."""
    account_api = AccountAPI(api_context, admin_token)
    response = account_api.export_device_statistics_to_file(
        file_ext="xls",
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-01T23:59:59Z"
    )
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="device_statistics.xls"', f"Expected Content-Disposition: attachment; filename=device_statistics.xls, but got: {response.headers.get('Content-Disposition')}"
