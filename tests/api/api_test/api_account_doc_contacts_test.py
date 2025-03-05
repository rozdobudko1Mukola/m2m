import pytest
from pytest import mark
from pages.api.account_doc_contacts_api import AccDocContactAPI
from playwright.sync_api import expect


# Test for the Account Documents API -------------------------------------------
@mark.api
@mark.smoke
@mark.testomatio('@Tttttt871')
def test_retrieve_child_account_documents(api_context, admin_token, test_data, create_and_del_account):
    acc_doc_contact = AccDocContactAPI(api_context, admin_token)
    response = acc_doc_contact.retrieve_child_account_documents(
        test_data['account_id']
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt872')
def test_update_child_account_documents(api_context, admin_token, test_data, create_and_del_account):
    acc_doc_contact = AccDocContactAPI(api_context, admin_token)
    response = acc_doc_contact.update_child_account_documents(
        test_data['account_id'],
        companyName="test_company"
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data['companyName'] == "test_company"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1727')
def test_retrieve_account_documents(api_context, admin_token, test_data, create_and_del_account):
    acc_doc_contact = AccDocContactAPI(api_context, admin_token)
    response = acc_doc_contact.retrieve_account_documents()
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1728')
def test_update_account_documents(api_context, admin_token, test_data, create_and_del_account):
    acc_doc_contact = AccDocContactAPI(api_context, admin_token)
    response = acc_doc_contact.update_account_documents(
        iban="1234567890",
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data['iban'] == "1234567890"


# Test for the Account contacts API -------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1739')
def test_retrieve_account_contacts_for_child_account(api_context, admin_token, test_data, create_and_del_account):
    acc_doc_contact = AccDocContactAPI(api_context, admin_token)
    response = acc_doc_contact.retrieve_account_contacts_for_child_account(
        test_data['account_id']
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1740')
def test_edit_contacts_for_child_account(api_context, admin_token, test_data, create_and_del_account):
    acc_doc_contact = AccDocContactAPI(api_context, admin_token)
    response = acc_doc_contact.edit_contacts_for_child_account(
        test_data['account_id'],
        companyAddress="test_address"
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data['companyAddress'] == "test_address"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1000')
def test_retrieve_account_contacts(api_context, token, test_data):
    acc_doc_contact = AccDocContactAPI(api_context, token)
    response = acc_doc_contact.retrieve_account_contacts()
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1001')
def test_update_account_contacts(api_context, token, test_data):
    acc_doc_contact = AccDocContactAPI(api_context, token)
    response = acc_doc_contact.update_account_contacts(
        companyAddress="test_company"
    )
    expect(response).to_be_ok()
    json_data = response.json()
    assert json_data['companyAddress'] == "test_company"



