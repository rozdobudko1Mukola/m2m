import pytest
from datetime import datetime
from pages.support_page import SupportPage
from pages.base_page import BasePage
from pages.profil_page import ProfilePage  
from playwright.sync_api import Page, expect


stage_user_email = "dkononenko1994@ukr.net"

invalid_email = "dkononenko1994ukr.net"

hide_sidebar_nav = "МоніторингЗвітиБаза данихБілінгБаланс: ПідтримкаДокументаціяПрофіль користувачаВихід"
show_sidebar_nav = "АналітикаМоніторингГеозониЗвітиТрекиПовідомленняБаза данихБілінгБаланс: ПідтримкаДокументаціяПрофіль користувачаВихід"

user_window_data_check = f"{stage_user_email}Дані облікового запису:Ім'я: {stage_user_email}НалаштуванняВихід"



# M2M-15 Change the background color of the site
pytest.mark.skip(reason="Not implemented")
def test_bg_color_switcher_m2m_15(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)    
    profile_page.switch_bg_color()

    expect(profile_page.bg_color_locator).to_have_css("background-color", profile_page.black_bg_color) # Перевіряємо зміну кольору фону



# M2M-781 Open the notification window
def test_open_close_notifications_m2m_781(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)

    profile_page.open_notifications()
    expect(authenticated_page.locator("ul div span").nth(0)).to_contain_text("Сповіщення") # Перевіряємо відкриття вікна сповіщень

    profile_page.close_notifications()
    expect(authenticated_page.locator("ul div span").nth(0)).not_to_be_visible() # Перевіряємо закриття вікна сповіщень


# M2M-782 Clear notifications in the Notifications window
pytest.mark.skip(reason="Not implemented")
def test_clear_notifications_m2m_782(authenticated_page: Page):
    pass


# M2M-16 The time displayed in the system is up to date
def test_current_time_m2m_16(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)
    current_time_on_site = profile_page.get_time_on_site()

    now = datetime.now().strftime("%H:%M") 

    assert current_time_on_site == now, f"час на сайті {current_time_on_site}" # Перевіряємо час на сайті з часом на ПК


# M2M-17 Customize the menu
def test_customize_menu_m2m_17(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)

    profile_page.customize_menu_deactivate_checkbox()
    assert profile_page.get_sidebar_list() == hide_sidebar_nav
    
    profile_page.customize_menu_activate_checkbox()
    assert profile_page.get_sidebar_list() == show_sidebar_nav


# M2M-783 Open the "User window"
def test_open_user_window_m2m_783(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)

    profile_page.base_page.avatar_btn.click()
    expect(authenticated_page.get_by_role("menu")).to_have_text(user_window_data_check) # Перевіряємо відкриття вікна користувача


# M2M-786 Use the user window to go to the "User Profile" page
def test_go_to_the_user_profile_page_m2m_786(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)

    profile_page.go_to_the_user_profile_page()
    expect(authenticated_page.locator("header h1")).to_have_text("Профіль користувача") # Перевіряємо перехід на сторінку профілю користувача


# M2M-787 Use the user window to log out of your account
def test_logout_from_account_m2m_787(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)

    profile_page.logout_use_user_window()
    expect(authenticated_page).to_have_url(f"{profile_page.BASE_URL}/login") # Перевіряємо вихід з облікового запису


# M2M-19 Replace user's email
pytest.mark.skip(reason="Not implemented")
def test_change_user_email_m2m_19(authenticated_page: Page):
    pass


# M2M-21 Replace user's email with invalid data
def test_replace_email_invalid_data_m2m_21(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    expect(profile_page.replace_email_invalid_data(invalid_email)).to_have_text("Введіть корекно Email") # Перевіряємо зміну email на невірний формат
    expect(profile_page.base_page.red_fild_color.last).to_have_css("border-color", profile_page.base_page.color_of_red) # Перевіряємо червоний колір поля


# M2M-22 Replace the username
def test_change_user_name_m2m_22(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    expect(profile_page.repalce_username(invalid_email)).to_have_value(invalid_email) # Перевіряємо зміну імені користувача