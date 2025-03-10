import pytest
from pytest import mark
from pages.api.invoices_api import InvoiceAPI
from playwright.sync_api import expect


# Fixtures ---------------------------------------------------------------------

@pytest.fixture(scope="function")
def precondition_get_test_invoice_id(api_context, test_data, client_token):
    invoice_api = InvoiceAPI(api_context, client_token)
    response = invoice_api.get_list_of_invoices_paginated(
        dateFrom="2023-01-01T00:00:00Z",
        dateTo="2025-01-31T23:59:59Z",
        page=1,
        per_page=100
    )
    expect(response).to_be_ok()

    response_data = response.json()

    # Знаходимо item, у якого 'comments' містить 'test'
    invoice_item = next((item for item in response_data["items"] if item["comments"] and 'test' in item["comments"]), None)

    # Зберігаємо id у test_data, якщо знайдено
    if invoice_item:
        test_data["invoice_id"] = invoice_item["id"]

    yield

# Tests ------------------------------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1729')
def test_get_account_invoice_by_id(api_context, client_token, test_data, precondition_get_test_invoice_id):
    invoice_api = InvoiceAPI(api_context, client_token)
    response = invoice_api.get_account_invoice_by_id(test_data["invoice_id"])
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1730')
def test_update_invoice_properties(api_context, admin_token, test_data, precondition_get_test_invoice_id):
    invoice_api = InvoiceAPI(api_context, admin_token)
    response = invoice_api.update_invoice_properties(test_data["invoice_id"], comments="test")
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1731')
def test_get_list_of_invoices_paginated(api_context, client_token):
    invoice_api = InvoiceAPI(api_context, client_token)
    response = invoice_api.get_list_of_invoices_paginated(
        dateFrom="2025-01-01T00:00:00Z",
        dateTo="2025-01-31T23:59:59Z",
        page=1,
        per_page=10 
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@T93426757')
def test_export_a_list_of_invoices_paginated_to_xls(api_context, client_token):
    invoice_api = InvoiceAPI(api_context, client_token)
    response = invoice_api.export_a_list_of_invoices_paginated_to_file(
        "xls", 
        dateFrom="2025-01-01T00:00:00Z", 
        dateTo="2025-01-31T23:59:59Z")
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="invoices.xls"', f"Expected Content-Disposition: attachment; filename=invoices.xls, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@T3fee62b7')
def test_export_a_list_of_invoices_paginated_to_csv(api_context, client_token):
    invoice_api = InvoiceAPI(api_context, client_token)
    response = invoice_api.export_a_list_of_invoices_paginated_to_file(
        "csv", 
        dateFrom="2025-01-01T00:00:00Z", 
        dateTo="2025-01-31T23:59:59Z")
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="invoices.csv"', f"Expected Content-Disposition: attachment; filename=invoices.csv, but got: {response.headers.get('Content-Disposition')}"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1732')
def test_get_invoice_pdf(api_context, client_token, test_data, precondition_get_test_invoice_id):
    invoice_api = InvoiceAPI(api_context, client_token)
    response = invoice_api.get_invoice_pdf(test_data["invoice_id"])
    expect(response).to_be_ok()
    assert response.headers.get("content-disposition") == 'attachment; filename="invoice.pdf"', f"Expected Content-Disposition: attachment; filename=invoice.pdf, but got: {response.headers.get('Content-Disposition')}"