import pytest
from pytest import mark
import datetime

from pages.e2e.profil_page import ProfilePage, settingUp
from pages.api.auth_api import AuthAPI

from playwright.sync_api import expect, APIRequestContext


@pytest.fixture(scope="class")
def defult_account_properties(api_context: APIRequestContext, token: str):

    auth_api = AuthAPI(api_context, token)
    response = auth_api.update_profile(
        firstName="test",
        lastName="auto",
        language="UKRAINIAN",
        phone="+380681002050",
        timezone="Europe/Kyiv",
        blockingNotifyEmail=True,
        mapLatitude="1",
        mapLongitude="1",
        mapZoom="1",
        positionManual=False,
        mapSourceUseGoogle=True,
        mapSourceUseOwnGoogleKey=True,
        mapSourceOwnGoogleKey="123",
    )
    expect(response).to_be_ok()

    yield

    response = auth_api.update_profile(
        firstName="test",
        lastName="auto",
        language="UKRAINIAN",
        phone="+380681002050",
        timezone="Europe/Kyiv",
        blockingNotifyEmail=True,
        mapLatitude="1",
        mapLongitude="1",
        mapZoom="1",
        positionManual=False,
        mapSourceUseGoogle=True,
        mapSourceUseOwnGoogleKey=True,
        mapSourceOwnGoogleKey="123",
    )
    expect(response).to_be_ok()


@pytest.fixture()
def map_coordinates_def(api_context: APIRequestContext, token: str):
    """Fixture to set default map coordinates for tests."""
    auth_api = AuthAPI(api_context, token)
    response = auth_api.update_profile(
        positionManual=True
    )
    expect(response).to_be_ok()
    yield


@mark.usefixtures("user_page", "defult_account_properties")
class TestProfilePage:

    @pytest.fixture(autouse=True)
    def open_profile_page(self, user_page):
        user_page.goto("/user")
        self.profile_page = ProfilePage(user_page)

    @mark.profile_page
    @mark.testomatio('@Ttttttt22')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_replace_first_name(self):
        expect(self.profile_page.get_general_tab_input("f_name_input", "first name")).to_have_value("first name")

    @mark.profile_page
    @mark.testomatio('@Ttttttt23')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_replace_last_name(self):
        expect(self.profile_page.get_general_tab_input("l_name_input", "last name")).to_have_value("last name")

    @mark.profile_page
    @mark.testomatio('@Ttttttt25')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_replace_phone_number(self):
        expect(self.profile_page.get_general_tab_input("phone_input", "+380774444444")).to_have_value("+380774444444")

    @mark.profile_page
    @mark.testomatio('@Ttttttt24')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_language(self):
        expect(self.profile_page.get_general_tab_dd("language_dropdown", "en")).to_have_text("English")
        expect(self.profile_page.get_general_tab_dd("language_dropdown", "ua")).to_have_text("Українська")

    @mark.profile_page
    @mark.testomatio('@Ttttttt26')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_timezone(self):
        expect(
            self.profile_page.get_general_tab_dd("timezone_dropdown", "london")
        ).to_have_text(
            "Europe/London [+01:00] British Time"
        )

    @mark.profile_page
    @mark.testomatio('@Ttttttt27')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_switch_beatween_tabs(self):
        expect(self.profile_page.switch_beatween_tabs('security_tab')).to_be_visible()
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        expect(self.profile_page.switch_beatween_tabs('general_tab')).to_be_visible()

    @mark.profile_page
    @mark.testomatio('@Ttttttt30')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_pass_using_invalid_old_pass(self):
        expect(self.profile_page.switch_beatween_tabs('security_tab')).to_be_visible()
        expect(
            self.profile_page.change_password("123456", "123123", "123123")).to_have_text("Поточний пароль не співпадає")

    @mark.profile_page
    @mark.testomatio('@Ttttttt31')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_pass_using_invalid_new_pass(self):
        expect(self.profile_page.switch_beatween_tabs('security_tab')).to_be_visible()
        expect(
            self.profile_page.change_password("123456", "123", "123")).to_have_text("Мінімум 6 сиволів")

    @mark.profile_page
    @mark.testomatio('@Tttttt788')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_pass_using_invalid_again_pass(self):
        expect(self.profile_page.switch_beatween_tabs('security_tab')).to_be_visible()
        expect(
            self.profile_page.change_password("123456", "123456", "123")).to_have_text("Паролі не співпадають")

    @mark.profile_page
    @mark.testomatio('@Ttttttt34')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_notification_radio(self):
        expect(self.profile_page.switch_beatween_tabs('security_tab')).to_be_visible()
        expect(self.profile_page.change_block_msg("msg_raio_off")).to_be_checked()
        expect(self.profile_page.change_block_msg("msg_raio_on_email")).to_be_checked()

    @mark.profile_page
    @mark.testomatio('@Ttttttt35')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_map_position_by_coordinates(self):
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        self.profile_page.change_map_coordinates(
            latitude="50.4501",
            longitude="30.5234",
            zoom="4",
            radio="by_coordinates_radio"
        )

    @mark.profile_page
    @mark.testomatio('@Ttttt1464')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_map_position_by_coordinates_invalid_value(self):
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        self.profile_page.change_map_coordinates(
            latitude="123123",
            longitude="123123",
            zoom="123123",
            radio="by_coordinates_radio"
        )

    @mark.profile_page
    @mark.testomatio('@Ttttttt36')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_change_map_position_by_browser(self, map_coordinates_def):
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        expect(self.profile_page.check_map_position("by_browser_radio")).to_have_value("false")

    @mark.profile_page
    @mark.testomatio('@Ttttttt37')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_uncheck_google_maps_checkbox(self):
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        expect(self.profile_page.google_maps_checkbox()).not_to_be_visible

    @mark.profile_page
    @mark.testomatio('@Ttttttt38')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_enter_google_maps_key(self):
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        expect(
            self.profile_page.enter_google_maps_key(
                "AIzaSyD4N49OO07gLL4P5GZWHGG6PjTlsBymqi4"
            )
        ).to_have_value(
            "AIzaSyD4N49OO07gLL4P5GZWHGG6PjTlsBymqi4"
        )

    @mark.profile_page
    @mark.testomatio('@Ttttt1460')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_enter_invalid_google_maps_key(self):
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        expect(self.profile_page.enter_google_maps_key("!@#$^^")).to_have_value("!@#$^^")

    @mark.profile_page
    @mark.testomatio('@Ttttt1461')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_enter_empty_google_maps_key(self):
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        expect(self.profile_page.enter_google_maps_key("")).to_have_value("")

    @mark.profile_page
    @mark.testomatio('@Ttttt1462')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_replace_google_maps_key(self):
        expect(self.profile_page.switch_beatween_tabs('map_tab')).to_be_visible()
        expect(self.profile_page.enter_google_maps_key("999")).to_have_value("999")

# elder tests setting up m2m system


@mark.usefixtures("user_page")
class TestSetiingUp:

    @pytest.fixture(autouse=True)
    def open_profile_page(self, user_page):
        user_page.goto("/monitoring")
        self.setting_up = settingUp(user_page)

    # M2M-15 Change the background color of the site
    @mark.profile_page
    @mark.testomatio('')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_bg_color_switcher_m2m_15(self):
        self.setting_up.switch_bg_color()

        expect(self.setting_up.bg_color_locator).to_have_css(
            "background-color", self.setting_up.black_bg_color
        )  # Перевіряємо зміну кольору фону
        self.setting_up.base_page.bg_color_switcher.click()

    # M2M-781 Open the notification window
    @mark.profile_page
    @mark.testomatio('')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_open_close_notifications_m2m_781(self):

        self.setting_up.open_notifications()
        # Перевіряємо відкриття вікна сповіщень
        expect(self.setting_up.page.locator("ul div span").nth(0)).to_contain_text("Сповіщення")

        self.setting_up.close_notifications()
        # Перевіряємо закриття вікна сповіщень
        expect(self.setting_up.page.locator("ul div span").nth(0)).not_to_be_visible()

    # M2M-16 The time displayed in the system is up to date
    @mark.profile_page
    @mark.testomatio('')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_current_time_m2m_16(self):
        current_time_on_site = self.setting_up.get_time_on_site()

        now = datetime.datetime.now().strftime("%H:%M")

        assert current_time_on_site == now, f"час на сайті {current_time_on_site}"  # Перевіряємо час на сайті з часом на ПК

    # M2M-17 Customize the menu
    @mark.profile_page
    @mark.testomatio('')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_customize_menu_m2m_17(self):

        hide_sidebar_nav = "МоніторингЗвітиБаза данихБілінгБаланс:ПідтримкаДокументаціяПрофіль користувачаВихід"
        show_sidebar_nav = (
            "АналітикаМоніторингГеозониЗвітиТрекиПовідомленняБаза даних"
            "БілінгБаланс:ПідтримкаДокументаціяПрофіль користувачаВихід"
        )

        self.setting_up.customize_menu_deactivate_checkbox()
        assert self.setting_up.get_sidebar_list() == hide_sidebar_nav

        self.setting_up.customize_menu_activate_checkbox()
        print(self.setting_up.get_sidebar_list())
        assert self.setting_up.get_sidebar_list() == show_sidebar_nav

    # M2M-783 Open the "User window"
    @mark.profile_page
    @mark.testomatio('')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_open_user_window_m2m_783(self):

        self.setting_up.base_page.avatar_btn.click()
        # Перевіряємо відкриття вікна користувача
        expect(self.setting_up.page.get_by_role("menu")).to_contain_text("Дані облікового запису")

    # M2M-786 Use the user window to go to the "User Profile" page
    @mark.profile_page
    @mark.testomatio('')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_go_to_the_user_profile_page_m2m_786(self):

        self.setting_up.go_to_the_user_profile_page()
        # Перевіряємо перехід на сторінку профілю користувача
        expect(self.setting_up.page.locator("header h1")).to_have_text("Профіль користувача")

    # M2M-787 Use the user window to log out of your account
    @mark.profile_page
    @mark.testomatio('')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_logout_from_account_m2m_787(self):

        self.setting_up.logout_use_user_window()
        expect(self.setting_up.page).to_have_url("/login")  # Перевіряємо вихід з облікового запису
