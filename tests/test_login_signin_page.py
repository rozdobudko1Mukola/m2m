import pytest

from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.googl_login import get_token_from_email


valid_user_email = "dkononenko1994@ukr.net"
valid_password = "123456"

invalid_email = "dkononenko1994ukr.net"
invalid_password = "123"

unregisteret_user_email = "userdosenotexist@gmail.com"

email_for_restore = "m2m.test.auto@gmail.com"

assertion_urn = "https://staging.m2m.eu/monitoring"
restore_password_url = "https://staging.m2m.eu/password-reset"


# M2M-1 Authorization of a registered user
def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(valid_user_email, valid_password)
    login_page.acsept_btn.click()

    expect(page).to_have_url(assertion_urn)
    

# M2M-2 Authorization of a registered user with an invalid email
def test_invalid_email_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(invalid_email, valid_password)
    login_page.acsept_btn.click()

    expect(login_page.mandatory_fields_msg.first).to_have_text("Введіть корекно Email")


# M2M-3 Authorization of a registered user with an invalid password
def test_invalid_password_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(valid_user_email, invalid_password)
    login_page.acsept_btn.click()

    expect(login_page.mandatory_fields_msg.last).to_have_text("Мінімум 6 сиволів")


# M2M-4 Authorization of an unregistered user
def test_unregistered_user_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(unregisteret_user_email, valid_password)
    login_page.acsept_btn.click() 

    expect(login_page.error_block).to_be_visible()


# M2M-1311 View user password
def test_view_password(page: Page):
    login_page = LoginPage(page)
    login_page.login(valid_user_email, valid_password)
    login_page.show_password_btn.click()

    expect(login_page.password_input).to_have_attribute("type", "text")


# M2M-5 View the "Terms and Conditions of Use."
def test_terms_of_use(page: Page):
    login_page = LoginPage(page)
    login_page.terms_of_use_btn.click()

    expect(login_page.term_popup).to_be_visible()
    expect(login_page.term_popup).to_contain_text("Умови користування")


# M2M-1435 View the "User agreement."
def test_user_agreement(page: Page):
    login_page = LoginPage(page)
    login_page.user_agriment_btn.click()

    expect(login_page.term_popup).to_be_visible()
    expect(login_page.term_popup).to_contain_text("ДОГОВІР ПУБЛІЧНОЇ ОФЕРТИ ПРО НАДАННЯ ПОСЛУГ МОНІТОРИНГУ")


# M2M-6 Remind user password
def test_restore_password(page: Page):
    login_page = LoginPage(page)

    login_page.restore_password_link.click()

    expect(page).to_have_url(restore_password_url)

    login_page.email_input.fill(email_for_restore)
    login_page.acsept_btn.click()







