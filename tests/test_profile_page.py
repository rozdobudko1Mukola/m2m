import pytest
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
def test_bg_color_switcher_m2m_15(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)    
    profile_page.switch_bg_color()

    expect(profile_page.bg_color_locator).to_have_css("background-color", profile_page.black_bg_color) # Перевіряємо зміну кольору фону
    profile_page.base_page.bg_color_switcher.click()



# M2M-781 Open the notification window
def test_open_close_notifications_m2m_781(authenticated_page: Page):
    profile_page = ProfilePage(authenticated_page)

    profile_page.open_notifications()
    expect(authenticated_page.locator("ul div span").nth(0)).to_contain_text("Сповіщення") # Перевіряємо відкриття вікна сповіщень

    profile_page.close_notifications()
    expect(authenticated_page.locator("ul div span").nth(0)).not_to_be_visible() # Перевіряємо закриття вікна сповіщень


pytest.mark.skip(reason="Not implemented")
# M2M-782 Clear notifications in the Notifications window
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


pytest.mark.skip(reason="Not implemented")
# M2M-19 Replace user's email
def test_change_user_email_m2m_19(authenticated_page: Page):
    pass


# M2M-21 Replace user's email with invalid data
def test_replace_email_invalid_data_m2m_21(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    expect(profile_page.replace_email_invalid_data(test_data['invalid_email'])).to_have_text("Введіть корекно Email") # Перевіряємо зміну email на невірний формат
    expect(profile_page.base_page.red_fild_color.last).to_have_css("border-color", profile_page.base_page.color_of_red) # Перевіряємо червоний колір поля


# M2M-22 Replace the username
def test_change_user_name_m2m_22(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)
    profile_page.repalce_username(f_name=test_data['first user name'])

    expect(profile_page.f_name_input).to_have_value(test_data["first user name"]) # Перевіряємо зміну імені користувача


# M2M-23 Replace the user's last name
def test_change_user_last_name_m2m_23(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)
    profile_page.repalce_username(l_name=test_data['last user name'])

    expect(profile_page.l_name_input).to_have_value(test_data["last user name"]) # Перевіряємо зміну прізвища користувача


# M2M-24 Change the language of the site
def test_change_site_language_m2m_24(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    expect(profile_page.change_language("English", 0)).to_have_text("User") # Перевіряємо зміну мови на "English"
    expect(profile_page.change_language("Русский", 0)).to_have_text("Профиль пользователя") # Перевіряємо зміну мови на "Русский"
    expect(profile_page.change_language("Українська", 0)).to_have_text("Профіль користувача") # Перевіряємо зміну мови на "Українська"

# M2M-25 Change the phone number
def test_change_phone_number_m2m_25(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)
    profile_page.repalce_username(phone=test_data['phone number'])

    expect(profile_page.phone_input).to_have_value(test_data["phone number"]) # Перевіряємо зміну номера телефону


# M2M-26 Replace user time zone
def test_change_user_time_zone_m2m_26(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)
    profile_page.change_language("Europe/Istanbul [+03:00] Turkey Time", 1)

    expect(profile_page.dd_language_timezone.nth(1)).to_contain_text("Europe/Istanbul [+03:00] Turkey Time") # Перевіряємо зміну часового поясу
    profile_page.change_language("Europe/Kyiv [+02:00] за східноєвропейським часом", 1) # Повертаємо часовий пояс на попередній


# M2M-27 Switch between drop-down lists
def test_switch_between_drop_down_lists_m2m_27(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.main_dd_button.nth(0).click(timeout=500)
    expect(profile_page.dd_language_timezone.nth(1)).not_to_be_visible() # Перевіряємо перехід між списками
    profile_page.main_dd_button.nth(1).click(timeout=500)
    expect(profile_page.change_pass_btn).to_be_visible() # Перевіряємо перехід між списками
    profile_page.main_dd_button.nth(2).click(timeout=500)
    expect(profile_page.gmaps_checkbox).to_be_visible() # Перевіряємо перехід між списками

@pytest.mark.skip(reason="тест ломає передумову аутентифікації у інших тестах. Потрібно переробити")
# M2M-28 Change password to a new one using valid values
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
def test_change_password_invalid_old_pass_m2m_30(auth_new_test_user: Page):    
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.change_password(test_data['invalid_current_pass'], test_data['new pass'], test_data['new pass'])
    expect(profile_page.base_page.mandatory_fields_msg).to_have_text("Поточний пароль не співпадає") # Перевіряємо вивід повідомлення про невірний пароль


# M2M-31 Change the password to a new one using invalid values of the new password
def test_change_password_invalid_new_pass_m2m_31(auth_new_test_user: Page):    
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.change_password(test_data['login_current_pass'], test_data['invalid_new_pass'], test_data['new pass'])

    expect(profile_page.base_page.mandatory_fields_msg.first).to_have_text("Мінімум 6 сиволів") # Перевіряємо вивід повідомлення про невірний пароль
    expect(profile_page.base_page.mandatory_fields_msg.last).to_have_text("Цей пароль не відповідає паролю, який ви ввели раніше") # Перевіряємо вивід повідомлення про невірний пароль


# M2M-788 Change the password to a new one using invalid values in the "Enter new password again" input field
def test_change_password_invalid_repeat_pass_m2m_788(auth_new_test_user: Page):    
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.change_password(test_data['login_current_pass'], test_data['new pass'], test_data['invalid_new_pass'])

    expect(profile_page.base_page.mandatory_fields_msg).to_have_text("Цей пароль не відповідає паролю, який ви ввели раніше") # Перевіряємо вивід повідомлення про невірний пароль
    expect(profile_page.red_fild_err_border.last).to_have_css("border-color", profile_page.base_page.color_of_red) # Перевіряємо червоний колір поля


# M2M-34 Change lock and change notifications
def test_change_notifications_m2m_34(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)
    profile_page.main_dd_button.nth(1).click(   )

    if profile_page.radio_btn.nth(0).is_checked():
        profile_page.radio_group(1)

        expect(profile_page.radio_btn.nth(1)).to_be_checked() # Перевіряємо стан радіо кнопки
    else:
        profile_page.radio_btn.nth(0).is_checked()
        profile_page.radio_group(0)

        expect(profile_page.radio_btn.nth(0)).to_be_checked()


# M2M-35 Change position on the map "at the coordinates"
def test_change_map_position_m2m_35(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.position_on_map_by_coordinate("51.4501", "20.5234", "4")
    profile_page.submit_popup_btn.click()


# M2M-1464 Change position on the map "at the coordinates" using invalid values
def test_invalid_change_map_position_m2m_1464(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.position_on_map_by_coordinate("91", "181", "19")

    expect(profile_page.base_page.mandatory_fields_msg.nth(0)).to_have_text("Максимальне значення 90") # Перевіряємо вивід повідомлення про невірні координати
    expect(profile_page.base_page.mandatory_fields_msg.nth(1)).to_have_text("Максимальне значення 180") # Перевіряємо вивід повідомлення про невірні координати
    expect(profile_page.base_page.mandatory_fields_msg.nth(2)).to_have_text("Максимальне значення 18") # Перевіряємо вивід повідомлення про невірні координати


# M2M-36 Change the position on the map using the " Through the browser" method
def test_change_map_position_through_browser_m2m_36(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)
    
    expect(profile_page.position_by_browser()).not_to_be_visible() # Перевіряємо відсутність вікна вибору координат


# M2M-38 In the map settings, specify the private key
def test_input_private_key_m2m_38(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.disable_googlemaps_chackbox()

    profile_page.google_maps_privet_key("test_key")
    profile_page.main_dd_button.last.click()

    expect(profile_page.checkboxes.last).to_be_checked() # Перевіряємо стан чекбокса


# M2M-1460 In the map settings, specify the invalid private key
# M2M-1461 In the map settings, specify the empty value private key
@pytest.mark.parametrize(
    "invalid_key, expected_message", [
        ("invalid_key", "Щось пішло не так з ключем Google map API"),
        ("", "Щось пішло не так з ключем Google map API"),
        # Додайте інші значення ключів і очікувані повідомлення за потреби
    ]
)
def test_input_invalid_private_key_m2m_1460_1461(auth_new_test_user: Page, invalid_key, expected_message):
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.disable_googlemaps_chackbox()
    profile_page.google_maps_privet_key(invalid_key)

    auth_new_test_user.goto(f"{profile_page.BASE_URL}/monitoring")
    profile_page.map_layers.hover()
    profile_page.gmap.nth(1).click()

    expect(profile_page.alert_map_msg).to_have_text(expected_message) # Перевіряємо вивід повідомлення про невірний ключ


@pytest.mark.skip(reason="Not implemented")
# M2M-1462 In the map settings, specify the private key and then delete it
def test_delete_private_key_m2m_1462(auth_new_test_user: Page):
    pass


@pytest.mark.skip(reason="Not implemented")
# M2M-1463 In the map settings, specify the private key and then change it
def test_change_private_key_m2m_1463(auth_new_test_user: Page):
    pass


# M2M-39 Log out of the system
def test_logout_m2m_39(auth_new_test_user: Page):
    profile_page = ProfilePage(auth_new_test_user)

    profile_page.logout_use_dd_profile()
    expect(auth_new_test_user).to_have_url(f"{profile_page.BASE_URL}/login") # Перевіряємо вихід з облікового запису







