import pytest
from pytest import mark
from pages.api.companies_api import CompaniesAPI
from playwright.sync_api import expect

# Fixture -----------------------------------------------------------------------

@pytest.fixture(scope='function')
def create_a_new_company(api_context, admin_token, test_data):
    """Тест на створення нової компанії."""
    companies_api = CompaniesAPI(api_context, admin_token)
    data = {
        "companyName": "Test API Company Name",
        "vatAmount": 0,
        "iban": "123123123123",
        "email": "",
        "address": "адреса",
        "integrationType": "PRIVATBANK",
        "apiKey": "123123123123",
        "relatedPerson": "",
        "companyType": "LEGAL_ENTITY",
        "vatCertificate": ""
    }
    response = companies_api.create_a_new_company(**data)

    expect(response).to_be_ok()
    test_data['company_id'] = response.json()['id']

    yield


@pytest.fixture(scope='function')
def delete_company(api_context, admin_token, test_data):
    """Тест на видалення компанії."""

    yield

    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.delete_company(test_data['company_id'])

    expect(response).to_be_ok()


@pytest.fixture(scope='function')
def create_and_delete_new_company(api_context, admin_token, test_data):
    """Тест на створення нової компанії."""
    companies_api = CompaniesAPI(api_context, admin_token)
    data = {
        "companyName": "Test API Company Name",
        "vatAmount": 0,
        "iban": "123123123123",
        "email": "",
        "address": "адреса",
        "integrationType": "PRIVATBANK",
        "apiKey": "123123123123",
        "relatedPerson": "",
        "companyType": "LEGAL_ENTITY",
        "vatCertificate": ""
    }
    response = companies_api.create_a_new_company(**data)

    expect(response).to_be_ok()
    test_data['company_id'] = response.json()['id']

    yield

    response = companies_api.delete_company(test_data['company_id'])
    expect(response).to_be_ok()


# Tests -------------------------------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1039')
def test_create_a_new_company(api_context, admin_token, test_data, delete_company):
    """Тест на створення нової компанії."""
    companies_api = CompaniesAPI(api_context, admin_token)
    data = {
        "companyName": "Test API Company Name",
        "vatAmount": 0,
        "iban": "123123123123",
        "email": "",
        "address": "адреса",
        "integrationType": "PRIVATBANK",
        "apiKey": "123123123123",
        "relatedPerson": "",
        "companyType": "LEGAL_ENTITY",
        "vatCertificate": ""
    }
    response = companies_api.create_a_new_company(**data)

    expect(response).to_be_ok()
    test_data['company_id'] = response.json()['id']


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1037')
def test_delete_company(api_context, admin_token, test_data, create_a_new_company):
    """Тест на видалення компанії."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.delete_company(test_data['company_id'])

    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1035')
def test_get_company_by_id(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на отримання компанії по ID."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.get_company_by_id(test_data['company_id'])

    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1036')
def test_update_company_properties(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на оновлення властивостей компанії."""
    companies_api = CompaniesAPI(api_context, admin_token)

    response = companies_api.update_company_properties(
        test_data['company_id'],
        companyName="Updated Test API Company Name")

    expect(response).to_be_ok()
    assert response.json()['companyName'] == "Updated Test API Company Name"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1745')
def test_get_invoice_properties(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на отримання властивостей рахунків."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.get_invoice_properties(test_data['company_id'])

    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1746')
def test_update_invoice_properties(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на оновлення властивостей рахунків."""
    companies_api = CompaniesAPI(api_context, admin_token)

    response = companies_api.update_invoice_properties(
        test_data['company_id'],
        invoiceMessage="Updated Test API Invoice Message"
        )

    expect(response).to_be_ok()
    assert response.json()['invoiceMessage'] == "Updated Test API Invoice Message"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1747')
def test_get_stamp_image(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на отримання зображення печатки."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.get_stamp_image(test_data['company_id'])

    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1748')
@mark.skip('Skip test. can not implemented upload')
def test_save_stamp_image(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на збереження зображення печатки."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.save_stamp_image(test_data['company_id'], image="downloads/img.png")
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1749')
def test_get_signature_image(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на отримання зображення підпису."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.get_signature_image(test_data['company_id'])

    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1750')
@mark.skip('Skip test. can not implemented upload')
def test_save_signature_image(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на збереження зображення підпису."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.save_signature_image(test_data['company_id'], image="test_image")

    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1038')
def test_retrieve_a_list_of_companies_with_pagination(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на отримання списку компаній з пагінацією."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.retrieve_a_list_of_companies_with_pagination()

    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1751')
def test_assign_company_to_account(api_context, admin_token, test_data, create_and_delete_new_company, create_and_del_account):
    """Тест на призначення компанії до облікового запису."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.assign_company_to_account(test_data['company_id'], test_data['account_id'])

    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1752')
def test_get_preview_of_invoice(api_context, admin_token, test_data, create_and_delete_new_company):
    """Тест на отримання попереднього перегляду рахунку."""
    companies_api = CompaniesAPI(api_context, admin_token)
    response = companies_api.get_preview_of_invoice(test_data['company_id'])

    expect(response).to_be_ok()