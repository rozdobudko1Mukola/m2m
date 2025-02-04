import pytest
from pytest import mark
from datetime import datetime
from pages.support_page import SupportPage
from pages.base_page import BasePage
from pages.login import LoginPage
from pages.profil_page import ProfilePage  
from playwright.sync_api import Page, expect


stage_user_email = "dkononenko1994@ukr.net"

hide_sidebar_nav = "МоніторингЗвітиБаза данихБілінгБаланс: ПідтримкаДокументаціяПрофіль користувачаВихід"
show_sidebar_nav = "АналітикаМоніторингГеозониЗвітиТрекиПовідомленняБаза данихБілінгБаланс: ПідтримкаДокументаціяПрофіль користувачаВихід"

user_window_data_check = f"{stage_user_email}Дані облікового запису:Ім'я: {stage_user_email}НалаштуванняВихід"

test_data = {
    "invalid_email": "dkononenko1994ukr.net",
    "first user name": "test auto user name",
    "last user name": "test auto user last name",
    "phone number": "+380123456789",
    "login_current_pass": "m2m.test.auto@gmail.com",
    "new pass": "qwerty123",
    "invalid_new_pass": "123",
    "invalid_current_pass": "invalid_o1d_pass"
    }


# M2M-15 Change the background color of the site
@mark.testomatio('@Ttttttt15')
def test_bg_color_switcher_m2m_15(client_user: Page):
    profile_page = ProfilePage(client_user)    
    profile_page.switch_bg_color()

    expect(profile_page.bg_color_locator).to_have_css("background-color", profile_page.black_bg_color) # Перевіряємо зміну кольору фону
    profile_page.base_page.bg_color_switcher.click()



# M2M-781 Open the notification window
@mark.testomatio('@Tttttt781')
def test_open_close_notifications_m2m_781(client_user: Page):
    profile_page = ProfilePage(client_user)

    profile_page.open_notifications()
    expect(client_user.locator("ul div span").nth(0)).to_contain_text("Сповіщення") # Перевіряємо відкриття вікна сповіщень

    profile_page.close_notifications()
    expect(client_user.locator("ul div span").nth(0)).not_to_be_visible() # Перевіряємо закриття вікна сповіщень


# M2M-782 Clear notifications in the Notifications window
@pytest.mark.skip(reason="Not implemented")
def test_clear_notifications_m2m_782(client_user: Page):
    pass


# M2M-16 The time displayed in the system is up to date
@mark.testomatio('@Ttttttt16')
def test_current_time_m2m_16(client_user: Page):
    profile_page = ProfilePage(client_user)
    current_time_on_site = profile_page.get_time_on_site()

    now = datetime.now().strftime("%H:%M") 

    assert current_time_on_site == now, f"час на сайті {current_time_on_site}" # Перевіряємо час на сайті з часом на ПК


# M2M-17 Customize the menu
@mark.testomatio('@Ttttttt17')
def test_customize_menu_m2m_17(client_user: Page):
    profile_page = ProfilePage(client_user)

    profile_page.customize_menu_deactivate_checkbox()
    assert profile_page.get_sidebar_list() == hide_sidebar_nav
    
    profile_page.customize_menu_activate_checkbox()
    assert profile_page.get_sidebar_list() == show_sidebar_nav


# M2M-783 Open the "User window"
@mark.testomatio('@Tttttt783')
def test_open_user_window_m2m_783(client_user: Page):
    profile_page = ProfilePage(client_user)

    profile_page.base_page.avatar_btn.click()
    expect(client_user.get_by_role("menu")).to_have_text(user_window_data_check) # Перевіряємо відкриття вікна користувача


# M2M-786 Use the user window to go to the "User Profile" page
@mark.testomatio('@Tttttt786')
def test_go_to_the_user_profile_page_m2m_786(client_user: Page):
    profile_page = ProfilePage(client_user)

    profile_page.go_to_the_user_profile_page()
    expect(client_user.locator("header h1")).to_have_text("Профіль користувача") # Перевіряємо перехід на сторінку профілю користувача


# M2M-787 Use the user window to log out of your account
@mark.testomatio('@Tttttt787')
def test_logout_from_account_m2m_787(client_user: Page):
    profile_page = ProfilePage(client_user)

    profile_page.logout_use_user_window()
    expect(client_user).to_have_url("/login") # Перевіряємо вихід з облікового запису


# M2M-19 Replace user's email
@pytest.mark.skip(reason="Not implemented")
def test_change_user_email_m2m_19(client_user: Page):
    pass


# M2M-21 Replace user's email with invalid data
@mark.testomatio('@Ttttttt21')
def test_replace_email_invalid_data_m2m_21(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)

    expect(profile_page.replace_email_invalid_data(test_data['invalid_email'])).to_have_text("Введіть корекно Email") # Перевіряємо зміну email на невірний формат
    expect(profile_page.base_page.red_fild_color.last).to_have_css("border-color", profile_page.base_page.color_of_red) # Перевіряємо червоний колір поля


# M2M-22 Replace the username
@mark.testomatio('@Ttttttt22')
def test_change_user_name_m2m_22(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)
    profile_page.repalce_username(f_name=test_data['first user name'])

    expect(profile_page.f_name_input).to_have_value(test_data["first user name"]) # Перевіряємо зміну імені користувача


# M2M-23 Replace the user's last name
@mark.testomatio('@Ttttttt23')
def test_change_user_last_name_m2m_23(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)
    profile_page.repalce_username(l_name=test_data['last user name'])

    expect(profile_page.l_name_input).to_have_value(test_data["last user name"]) # Перевіряємо зміну прізвища користувача


# M2M-24 Change the language of the site
@mark.testomatio('@Ttttttt24')
def test_change_site_language_m2m_24(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)

    expect(profile_page.change_language("English", 0)).to_have_text("User") # Перевіряємо зміну мови на "English"
    expect(profile_page.change_language("Русский", 0)).to_have_text("Профиль пользователя") # Перевіряємо зміну мови на "Русский"
    expect(profile_page.change_language("Українська", 0)).to_have_text("Профіль користувача") # Перевіряємо зміну мови на "Українська"


# M2M-25 Change the phone number
@mark.testomatio('@Ttttttt25')
def test_change_phone_number_m2m_25(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)
    profile_page.repalce_username(phone=test_data['phone number'])

    expect(profile_page.phone_input).to_have_value(test_data["phone number"]) # Перевіряємо зміну номера телефону


# M2M-26 Replace user time zone
@mark.testomatio('@Ttttttt26')
def test_change_user_time_zone_m2m_26(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)
    profile_page.change_language("Europe/Istanbul [+03:00] Turkey Time", 1)

    expect(profile_page.dd_language_timezone.nth(1)).to_contain_text("Europe/Istanbul [+03:00] Turkey Time") # Перевіряємо зміну часового поясу
    profile_page.change_language("Europe/Kyiv [+02:00] за східноєвропейським часом", 1) # Повертаємо часовий пояс на попередній


# M2M-27 Switch between drop-down lists
@mark.testomatio('@Ttttttt27')
def test_switch_between_drop_down_lists_m2m_27(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)

    profile_page.main_dd_button.nth(0).click(timeout=500)
    expect(profile_page.dd_language_timezone.nth(1)).not_to_be_visible() # Перевіряємо перехід між списками
    profile_page.main_dd_button.nth(1).click(timeout=500)
    expect(profile_page.change_pass_btn).to_be_visible() # Перевіряємо перехід між списками
    profile_page.main_dd_button.nth(2).click(timeout=500)
    expect(profile_page.gmaps_checkbox).to_be_visible() # Перевіряємо перехід між списками


# M2M-28 Change password to a new one using valid values
@pytest.mark.skip(reason="тест ломає передумову аутентифікації у інших тестах. Потрібно переробити")
def test_change_password_m2m_28(page: Page):    
    login_page = LoginPage(page)
    profile_page = ProfilePage(page)
    base_page = BasePage(page)


    login_page.login(test_data['login_current_pass'], test_data['login_current_pass'])
    login_page.acsept_btn.click()

    
    base_page.profile_menu_btn.click()
    profile_page.change_password(test_data['login_current_pass'], test_data['new pass'], test_data['new pass'])
    profile_page.submit_popup_btn.click()

    expect(page).to_have_url(f"{profile_page.BASE_URL}/login", timeout=15000) # Перевіряємо вихід з облікового запису

    # Логінимося з новим паролем і повертаємо старий пароль назад
    login_page.login(test_data['login_current_pass'], test_data['new pass'])
    login_page.acsept_btn.click()

    base_page.profile_menu_btn.click()
    profile_page.change_password(test_data['new pass'], test_data['login_current_pass'], test_data['login_current_pass'])
    profile_page.submit_popup_btn.click()

    expect(page).to_have_url(f"{profile_page.BASE_URL}/login", timeout=15000) # Перевіряємо вихід з облікового запису


# M2M-30 Change the password to a new one using invalid values of the old password
@mark.testomatio('@Ttttttt30')
def test_change_password_invalid_old_pass_m2m_30(selfreg_user: Page):    
    profile_page = ProfilePage(selfreg_user)

    profile_page.change_password(test_data['invalid_current_pass'], test_data['new pass'], test_data['new pass'])
    expect(profile_page.base_page.mandatory_fields_msg).to_have_text("Поточний пароль не співпадає") # Перевіряємо вивід повідомлення про невірний пароль


# M2M-31 Change the password to a new one using invalid values of the new password
@mark.testomatio('@Ttttttt31')
def test_change_password_invalid_new_pass_m2m_31(selfreg_user: Page):    
    profile_page = ProfilePage(selfreg_user)

    profile_page.change_password(test_data['login_current_pass'], test_data['invalid_new_pass'], test_data['new pass'])

    expect(profile_page.base_page.mandatory_fields_msg.first).to_have_text("Мінімум 6 сиволів") # Перевіряємо вивід повідомлення про невірний пароль
    expect(profile_page.base_page.mandatory_fields_msg.last).to_have_text("Цей пароль не відповідає паролю, який ви ввели раніше") # Перевіряємо вивід повідомлення про невірний пароль


# M2M-788 Change the password to a new one using invalid values in the "Enter new password again" input field
@mark.testomatio('@Tttttt788')
def test_change_password_invalid_repeat_pass_m2m_788(selfreg_user: Page):    
    profile_page = ProfilePage(selfreg_user)

    profile_page.change_password(test_data['login_current_pass'], test_data['new pass'], test_data['invalid_new_pass'])

    expect(profile_page.base_page.mandatory_fields_msg).to_have_text("Цей пароль не відповідає паролю, який ви ввели раніше") # Перевіряємо вивід повідомлення про невірний пароль
    expect(profile_page.red_fild_err_border.last).to_have_css("border-color", profile_page.base_page.color_of_red) # Перевіряємо червоний колір поля


# M2M-34 Change lock and change notifications
@mark.testomatio('@Ttttttt34')
def test_change_notifications_m2m_34(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)
    profile_page.main_dd_button.nth(1).click(   )

    if profile_page.radio_btn.nth(0).is_checked():
        profile_page.radio_group(1)

        expect(profile_page.radio_btn.nth(1)).to_be_checked() # Перевіряємо стан радіо кнопки
    else:
        profile_page.radio_btn.nth(0).is_checked()
        profile_page.radio_group(0)

        expect(profile_page.radio_btn.nth(0)).to_be_checked()


# M2M-35 Change position on the map "at the coordinates"
@mark.testomatio('@Ttttttt35')
def test_change_map_position_m2m_35(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)

    profile_page.position_on_map_by_coordinate("51.4501", "20.5234", "4")
    profile_page.submit_popup_btn.click()


# M2M-1464 Change position on the map "at the coordinates" using invalid values
@mark.testomatio('@Ttttt1464')
def test_invalid_change_map_position_m2m_1464(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)

    profile_page.position_on_map_by_coordinate("91", "181", "19")

    expect(profile_page.base_page.mandatory_fields_msg.nth(0)).to_have_text("Максимальне значення 90") # Перевіряємо вивід повідомлення про невірні координати
    expect(profile_page.base_page.mandatory_fields_msg.nth(1)).to_have_text("Максимальне значення 180") # Перевіряємо вивід повідомлення про невірні координати
    expect(profile_page.base_page.mandatory_fields_msg.nth(2)).to_have_text("Максимальне значення 18") # Перевіряємо вивід повідомлення про невірні координати


# M2M-36 Change the position on the map using the " Through the browser" method
@mark.testomatio('@Ttttttt36')
def test_change_map_position_through_browser_m2m_36(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)
    
    expect(profile_page.position_by_browser()).not_to_be_visible() # Перевіряємо відсутність вікна вибору координат


# M2M-38 In the map settings, specify the private key
@mark.testomatio('@Ttttttt38')
def test_input_private_key_m2m_38(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)

    profile_page.disable_googlemaps_chackbox()

    profile_page.google_maps_privet_key("test_key")
    profile_page.main_dd_button.last.click()
    
    expect(profile_page.checkboxes.last).to_be_checked() # Перевіряємо стан чекбокса


# M2M-1460 In the map settings, specify the invalid private key
# M2M-1461 In the map settings, specify the empty value private key
@mark.testomatio('@Ttttt1460')
@mark.testomatio('@Ttttt1461')
@pytest.mark.parametrize(
    "invalid_key, expected_message", [
        ("invalid_key", "Щось пішло не так з ключем Google map API"),
        ("", "Щось пішло не так з ключем Google map API"),
        # Додайте інші значення ключів і очікувані повідомлення за потреби
    ]
)
def test_input_invalid_private_key_m2m_1460_1461(selfreg_user: Page, invalid_key, expected_message):
    profile_page = ProfilePage(selfreg_user)

    profile_page.disable_googlemaps_chackbox()
    profile_page.google_maps_privet_key(invalid_key)

    selfreg_user.goto("/monitoring")
    profile_page.map_layers.hover()
    profile_page.gmap.nth(1).click()

    expect(profile_page.alert_map_msg).to_have_text(expected_message) # Перевіряємо вивід повідомлення про невірний ключ


# M2M-1462 In the map settings, specify the private key and then delete it
@pytest.mark.skip(reason="Not implemented")
def test_delete_private_key_m2m_1462(selfreg_user: Page):
    pass


# M2M-1463 In the map settings, specify the private key and then change it
@pytest.mark.skip(reason="Not implemented")
def test_change_private_key_m2m_1463(selfreg_user: Page):
    pass


# M2M-39 Log out of the system
@mark.testomatio('@Ttttttt39')
def test_logout_m2m_39(selfreg_user: Page):
    profile_page = ProfilePage(selfreg_user)

    profile_page.logout_use_dd_profile()
    expect(selfreg_user).to_have_url("/login") # Перевіряємо вихід з облікового запису







