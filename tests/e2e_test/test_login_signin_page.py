from pytest import mark
import os
from playwright.sync_api import Page, expect
from pages.e2e.login import LoginPage
from pages.e2e.base_page import BasePage


valid_user_email = "dkononenko1994@ukr.net"
valid_password = "123456"

invalid_email = "dkononenko1994ukr.net"
invalid_password = "123"

unregisteret_user_email = "userdosenotexist@gmail.com"

email_for_restore = "m2m.test.auto@gmail.com"

sign_up_url = "/sign-up"

login_url = os.getenv("BASE_URL", "/" "")

main_url = "https://m2m.ua/"

color_of_red = "rgb(211, 47, 47)"

user_email_list = "cateyo5874@rowplant.com"
prod_users = "baker44793@bulatox.com"


# M2M-1 Authorization of a registered user
@mark.testomatio('@Tttttttt1')
def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(valid_user_email, valid_password)
    login_page.accept_btn.click()

    expect(page).to_have_url("/monitoring")


# M2M-2 Authorization of a registered user with an invalid email
@mark.testomatio('@Tttttttt2')
def test_invalid_email_login(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(invalid_email, valid_password)
    login_page.accept_btn.click()

    expect(base_page.mandatory_fields_msg.first).to_have_text("Введіть корекно Email")


# M2M-3 Authorization of a registered user with an invalid password
@mark.testomatio('@Tttttttt3')
def test_invalid_password_login(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(valid_user_email, invalid_password)
    login_page.accept_btn.click()

    expect(base_page.mandatory_fields_msg.last).to_have_text("Мінімум 6 сиволів")


# M2M-4 Authorization of an unregistered user
@mark.testomatio('@Tttttttt4')
def test_unregistered_user_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(unregisteret_user_email, valid_password)
    login_page.accept_btn.click()

    expect(login_page.error_block).to_be_visible(timeout=10000)


# M2M-1311 View user password
@mark.testomatio('@Ttttt1311')
def test_view_password(page: Page):
    login_page = LoginPage(page)
    login_page.login(valid_user_email, valid_password)
    login_page.show_password_btn.click()

    expect(login_page.password_input).to_have_attribute("type", "text")


# M2M-5 View the "Terms and Conditions of Use."
@mark.testomatio('@Tttttttt5')
def test_terms_of_use(page: Page):
    login_page = LoginPage(page)
    login_page.terms_of_use_btn.click()

    expect(login_page.term_popup).to_be_visible()
    expect(login_page.term_popup).to_contain_text("Умови користування")


# M2M-1435 View the "User agreement."
@mark.testomatio('@Ttttt1435')
def test_user_agreement(page: Page):
    login_page = LoginPage(page)
    login_page.user_agriment_btn.click()

    expect(login_page.term_popup).to_be_visible()
    expect(login_page.term_popup).to_contain_text("ДОГОВІР ПУБЛІЧНОЇ ОФЕРТИ ПРО НАДАННЯ ПОСЛУГ МОНІТОРИНГУ")


# M2M-772 Remind user's password with an invalid email
@mark.testomatio('@Tttttt772')
def test_restore_password_invalid_email(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.restore_password_link.click()

    expect(page).to_have_url("/password-reset")

    login_page.email_input.fill(invalid_email)
    login_page.accept_btn.click()

    expect(base_page.red_fild_color, "color should be red").to_have_css("border-color", color_of_red)
    expect(base_page.mandatory_fields_msg.first).to_have_text("Введіть корекно Email")


# M2M-7 Switch to another account using the "Sign in as" button
@mark.testomatio('@Tttttttt7')
def test_sign_in_as(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    base_url = page.url.split("/")[2]
    if base_url == "staging.m2m.eu":
        ch_user_email = user_email_list
    elif base_url == "my.m2m.eu":
        ch_user_email = prod_users

    login_page.login_as(valid_user_email, valid_password, ch_user_email)

    base_page.profile_menu_btn.click()

    expect(login_page.user_email_profile_input).to_have_value(ch_user_email)


# M2M-8 In the "Sign in as" window, use the search
@mark.testomatio('@Tttttttt8')
def test_sign_in_as_search(page: Page):
    login_page = LoginPage(page)

    login_page.login(valid_user_email, valid_password)
    login_page.login_as_btn.click()

    base_url = page.url.split("/")[2]
    if base_url == "staging.m2m.eu":
        ch_user_email = user_email_list
    elif base_url == "my.m2m.eu":
        ch_user_email = prod_users

    login_page.login_as_input.fill(ch_user_email)
    expect(login_page.login_as_list).to_contain_text(ch_user_email)


# M2M-780 In the "Sign in as" window, use a search using an invalid email
@mark.testomatio('@Tttttt780')
def test_sign_in_as_search_invalid_email(page: Page):
    login_page = LoginPage(page)

    login_page.login(valid_user_email, valid_password)
    login_page.login_as_btn.click()

    login_page.login_as_input.fill(invalid_email)

    expect(login_page.login_as_list).not_to_be_visible


# M2M-1824 Reopen "Sign in as" window, after use a search using an invalid email
@mark.testomatio('@Ttttt1824')
def test_reopen_sign_in_as_window(page: Page):
    login_page = LoginPage(page)

    login_page.login(valid_user_email, valid_password)
    login_page.login_as_btn.click()

    login_page.login_as_input.fill(invalid_email)

    expect(login_page.login_as_list).not_to_be_visible

    login_page.close_login_as_popap.click()
    login_page.login_as_btn.click()

    expect(login_page.login_as_list).to_be_visible


# M2M-1313 Go from the new account creation page to the authorization page
@mark.testomatio('@Ttttt1313')
def test_go_to_login_page(page: Page):
    login_page = LoginPage(page)

    login_page.sign_up_btn.click()

    expect(page).to_have_url(sign_up_url)


# M2M-1457 Go from the user creation page to the login page using the arrows in the upper left corner
@mark.testomatio('@Ttttt1457')
def test_go_back_to_login_page_use_arrow(page: Page):
    login_page = LoginPage(page)

    login_page.sign_up_btn.click()

    expect(page).to_have_url(sign_up_url)

    login_page.go_back_btn.click()

    expect(page).to_have_url(login_url)


# M2M-1456 Go from the login page to the login site
@mark.testomatio('@Ttttt1456')
def test_go_back_to_home_page(page: Page):
    login_page = LoginPage(page)

    login_page.go_back_btn.click()

    expect(page).to_have_url(main_url)


# M2M-10 Create a new user with invalid data
@mark.testomatio('@Ttttttt10')
def test_create_new_user_invalid_data(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.sign_up_btn.click()
    login_page.sign_up(invalid_email, "123", "321", "ua")

    login_page.i_agree_checkbox.check()
    login_page.accept_btn.click()

    expect(base_page.red_fild_color.first, "color should be red").to_have_css("border-color", color_of_red)
    expect(base_page.red_fild_color.nth(1), "color should be red").to_have_css("border-color", color_of_red)
    expect(base_page.red_fild_color.nth(2), "color should be red").to_have_css("border-color", color_of_red)

    expect(base_page.mandatory_fields_msg.first).to_have_text("Введіть корекно Email")
    expect(base_page.mandatory_fields_msg.nth(1)).to_have_text("Мінімум 6 сиволів")
    expect(base_page.mandatory_fields_msg.last).to_have_text("Паролі не співпадають")


# M2M-13 Create a new user without confirming the terms and conditions of use
@mark.testomatio('@Ttttttt13')
def test_create_new_user_without_confirm(page: Page):
    login_page = LoginPage(page)

    login_page.sign_up_btn.click()
    login_page.sign_up(valid_user_email, valid_password, valid_password, "ua")

    login_page.accept_btn.is_disabled()


# M2M-1310 Create a new user using the data of a user who is already registered
@mark.testomatio('@Ttttt1310')
def test_create_new_user_with_registered_data(page: Page):
    login_page = LoginPage(page)

    login_page.sign_up_btn.click()
    login_page.sign_up(valid_user_email, valid_password, valid_password, "ua")

    login_page.i_agree_checkbox.check()
    login_page.accept_btn.click()

    expect(login_page.user_is_exist_msg).to_have_text("Такий користувач вже існує")


# M2M-1312 View user password on the account creation page
@mark.testomatio('@Ttttt1312')
def test_view_password_on_sign_up_page(page: Page):
    login_page = LoginPage(page)

    login_page.sign_up_btn.click()
    login_page.sign_up(valid_user_email, valid_password, valid_password, "ua")

    login_page.show_password_btn.first.click()
    expect(login_page.password_input).to_have_attribute("type", "text")

    login_page.show_password_btn.last.click()
    expect(login_page.repeat_password_input).to_have_attribute("type", "text")


# M2M-6 Remind user password ------------------------------------------------
@mark.testomatio('@Tttttttt6')
def test_restore_password(page: Page):
    login_page = LoginPage(page)

    login_page.restore_password_link.click()

    expect(page).to_have_url("/password-reset")

    login_page.email_input.fill(email_for_restore)
    login_page.accept_btn.click()
