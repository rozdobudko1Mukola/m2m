import pytest
from datetime import datetime
from pages.support_page import SupportPage
from pages.base_page import BasePage
from pages.profil_page import ProfilePage  
from playwright.sync_api import Page, expect





# M2M-15 Change the background color of the site
def test_bg_color_switcher_m2m_15(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)
    profile_page.switch_bg_color()

    expect(authenticated_page.locator("body main")).to_have_css("background-color", "rgb(12, 31, 55)") # Перевіряємо зміну кольору фону


# M2M-781 Open the notification window
def test_open_close_notifications_m2m_781(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)

    profile_page.open_notifications()
    expect(authenticated_page.locator("ul div span").nth(0)).to_contain_text("Сповіщення") # Перевіряємо відкриття вікна сповіщень

    profile_page.close_notifications()
    expect(authenticated_page.locator("ul div span")).not_to_be_visible() # Перевіряємо закриття вікна сповіщень


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
    assert profile_page.get_sidebar_list() == "МоніторингЗвітиБаза данихБілінгБаланс: ПідтримкаДокументаціяПрофіль користувачаВихід"
    
    profile_page.customize_menu_activate_checkbox()
    assert profile_page.get_sidebar_list() == "АналітикаМоніторингГеозониЗвітиТрекиПовідомленняБаза данихБілінгБаланс: ПідтримкаДокументаціяПрофіль користувачаВихід"