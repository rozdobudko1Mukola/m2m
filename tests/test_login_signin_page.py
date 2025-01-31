import pytest
import random
import os
from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.base_page import BasePage


valid_user_email = "dkononenko1994@ukr.net"
valid_password = "123456"

invalid_email = "dkononenko1994ukr.net"
invalid_password = "123"

unregisteret_user_email = "userdosenotexist@gmail.com"

email_for_restore = "m2m.test.auto@gmail.com"

monitoring_url = "/monitoring"
restore_password_url = "/password-reset"
sign_up_url = "/sign-up"

login_url = os.getenv("BASE_URL", "/" "")

main_url = "https://m2m.ua/"

color_of_red = "rgb(211, 47, 47)"

user_email_list = "cateyo5874@rowplant.com"
prod_users = "baker44793@bulatox.com"

# M2M-1 Authorization of a registered user
def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(valid_user_email, valid_password)
    login_page.accept_btn.click()

    expect(page).to_have_url(monitoring_url)
    

# M2M-2 Authorization of a registered user with an invalid email
def test_invalid_email_login(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(invalid_email, valid_password)
    login_page.accept_btn.click()

    expect(base_page.mandatory_fields_msg.first).to_have_text("Введіть корекно Email")


# M2M-3 Authorization of a registered user with an invalid password
def test_invalid_password_login(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(valid_user_email, invalid_password)
    login_page.accept_btn.click()

    expect(base_page.mandatory_fields_msg.last).to_have_text("Мінімум 6 сиволів")


# M2M-4 Authorization of an unregistered user
def test_unregistered_user_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(unregisteret_user_email, valid_password)
    login_page.accept_btn.click() 

    expect(login_page.error_block).to_be_visible(timeout=10000)


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


# M2M-772 Remind user's password with an invalid email
def test_restore_password_invalid_email(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.restore_password_link.click()

    expect(page).to_have_url(restore_password_url)

    login_page.email_input.fill(invalid_email)
    login_page.accept_btn.click()

    expect(base_page.red_fild_color, "color should be red").to_have_css("border-color", color_of_red)
    expect(base_page.mandatory_fields_msg.first).to_have_text("Введіть корекно Email")  


# M2M-7 Switch to another account using the "Sign in as" button
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
def test_sign_in_as_search_invalid_email(page: Page):
    login_page = LoginPage(page)

    login_page.login(valid_user_email, valid_password)
    login_page.login_as_btn.click()

    login_page.login_as_input.fill(invalid_email)

    expect(login_page.login_as_list).not_to_be_visible

# M2M-1824 Reopen "Sign in as" window, after use a search using an invalid email
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
def test_go_to_login_page(page: Page):
    login_page = LoginPage(page)

    login_page.sign_up_btn.click()

    expect(page).to_have_url(sign_up_url)


# M2M-1457 Go from the user creation page to the login page using the arrows in the upper left corner
def test_go_back_to_login_page_use_arrow(page: Page):
    login_page = LoginPage(page)

    login_page.sign_up_btn.click()

    expect(page).to_have_url(sign_up_url)

    login_page.go_back_btn.click()

    expect(page).to_have_url(login_url)


# M2M-1456 Go from the login page to the login site
def test_go_back_to_home_page(page: Page):
    login_page = LoginPage(page)

    login_page.go_back_btn.click()

    expect(page).to_have_url(main_url)


# M2M-10 Create a new user with invalid data
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
    expect(base_page.mandatory_fields_msg.last).to_have_text("Цей пароль не відповідає паролю, який ви ввели раніше")


# M2M-13 Create a new user without confirming the terms and conditions of use
def test_create_new_user_without_confirm(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.sign_up_btn.click()
    login_page.sign_up(valid_user_email, valid_password, valid_password, "ua")

    login_page.accept_btn.is_disabled()


# M2M-1310 Create a new user using the data of a user who is already registered
def test_create_new_user_with_registered_data(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.sign_up_btn.click()
    login_page.sign_up(valid_user_email, valid_password, valid_password, "ua")

    login_page.i_agree_checkbox.check()
    login_page.accept_btn.click()

    expect(login_page.user_is_exist_msg).to_have_text("Такий користувач вже існує")


# M2M-1312 View user password on the account creation page
def test_view_password_on_sign_up_page(page: Page):
    login_page = LoginPage(page)

    login_page.sign_up_btn.click()
    login_page.sign_up(valid_user_email, valid_password, valid_password, "ua")

    login_page.show_password_btn.first.click()
    expect(login_page.password_input).to_have_attribute("type", "text")

    login_page.show_password_btn.last.click()
    expect(login_page.repeat_password_input).to_have_attribute("type", "text")

# M2M-6 Remind user password ------------------------------------------------
def test_restore_password(page: Page):
    login_page = LoginPage(page)

    login_page.restore_password_link.click()

    expect(page).to_have_url(restore_password_url)

    login_page.email_input.fill(email_for_restore)
    login_page.accept_btn.click()

@pytest.mark.skip("generate a lot of users/ Need to add post condition")
# M2M-9 Create a new user ------------------------------------------------
def test_create_new_user(page: Page):
    login_page = LoginPage(page)
    random_number = random.sample(range(10000), 10000).pop()

    login_page.sign_up_btn.click()
    login_page.sign_up(f"test_email+{random_number}@gmail.com", "123456", "123456", "ua")

    login_page.i_agree_checkbox.check()
    login_page.accept_btn.click()

    expect(page.locator("body h1")).to_have_text("Реєстрацію завершено")

@pytest.mark.skip("Not implemented")
# M2M-1603 Authorisation with new user data
def test_login_new_user(page: Page):
    pass

    

