import pytest
from pytest import mark
from pages.api.payment_api import PaymentAPI
from playwright.sync_api import expect


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt899')
def test_prepare_liqpay_payment_request(api_context, token):
    """Тест на підготовку запиту на отримання платежу в LiqPay."""
    payment_api = PaymentAPI(api_context, token)
    response = payment_api.prepare_liqpay_payment_request(100)
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt900')
def test_list_current_account_transactions(api_context, token):
    """Тест на отримання списку транзакцій поточного рахунку."""
    payment_api = PaymentAPI(api_context, token)
    response = payment_api.list_current_account_transactions(
        dateFrom="2024-01-01T00:00:00Z",
        dateTo="2025-03-11T00:00:00Z",
        page=1,
        per_page=10
    )
    expect(response).to_be_ok()
    print(response.json())