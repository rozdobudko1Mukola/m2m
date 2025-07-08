from playwright.sync_api import Page
from pages.e2e.base_page import BasePage
from playwright.sync_api import Locator
import re


class ProfilePage:

    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.page.goto("/user")

        self.bg_color_locator = self.page.locator("body main")
        self.black_bg_color = "rgb(12, 31, 55)"
        self.white_bg_color = "rgb(245, 245, 245)"
        self.red_fild_err_border = self.page.locator("form fieldset")
        self.alert_map_msg = self.page.locator("//div[contains(@class, 'btn-layers')]/div[@role='alert']")

        # /user page locators
        self.replace_email_btn = self.page.locator("//div[@id='panel1bh-content']/div/button")
        self.f_name_input = self.page.locator("input[name='firstName']")
        self.l_name_input = self.page.locator("input[name='lastName']")
        self.phone_input = self.page.locator("input[name='phone']")
        self.save_btn = self.page.locator("//div[@id='panel1bh-content']/div/div[7]/button")
        self.listbox = self.page.locator("//ul")
        self.dd_language_timezone = self.page.locator("//div[@id='demo-simple-select']")
        self.sequrety_save_btn = self.page.get_by_role("button", name="Зберегти")

        # confirm popap locators
        self.new_email_input = self.page.locator("input[name='newEmail']")
        self.current_pass_input = self.page.locator("input[name='oldPassword']")
        self.new_pass_input = self.page.locator("input[name='newPassword']")
        self.repeat_pass_input = self.page.locator("input[name='repeatPassword']")
        self.submit_popup_btn = self.page.locator("//div[@role='dialog']//button")

        self.apiKey_input = self.page.locator("//div[@role='presentation']//input")

        # dropdown list locator
        self.dropdown_list = self.page.locator("ul")
        self.main_dd_button = self.page.locator("//h3/button")

        # security tab locators
        self.change_pass_btn = self.page.get_by_role("button", name="Змінити пароль")
        self.radio_btn = self.page.locator("//input[@type='radio']")

        # maps tab locators
        self.gmaps_checkbox = self.page.get_by_text("Google Maps")
        self.mapLatitude_input = self.page.locator("input[name='mapLatitude']")
        self.mapLongitude_input = self.page.locator("input[name='mapLongitude']")
        self.mapZoom_input = self.page.locator("input[name='mapZoom']")
        self.checkboxes = self.page.locator("input[type='checkbox']")

        # map layers locators
        self.map_layers = self.page.locator("//div[contains(@class, 'btn-layers')]")
        self.gmap = self.page.locator("//div[contains(@class, 'btn-layers')]//input")

    def switch_bg_color(self):
        bg_color = self.bg_color_locator.evaluate(
            "element => getComputedStyle(element).backgroundColor"
        )
        if bg_color == self.black_bg_color:
            self.base_page.bg_color_switcher.click()
        self.base_page.bg_color_switcher.click()

    def open_notifications(self):
        self.base_page.open_notifications_btn.click()

    def close_notifications(self):
        self.base_page.close_notifications_btn.click()

    def get_time_on_site(self) -> str:
        current_time = self.base_page.current_time.text_content()
        if current_time is not None:
            current_time_formatted = ":".join(current_time.split(":")[:2])
            return current_time_formatted
        else:
            return ""

    def customize_menu_deactivate_checkbox(self):
        self.base_page.customize_menu_btn.click()
        checkboxes = self.base_page.customize_menu_list_checkbox

        for i in range(checkboxes.count()):
            if checkboxes.nth(i).is_enabled():
                if checkboxes.nth(i).is_checked():
                    checkboxes.nth(i).click()
            else:
                continue

    def customize_menu_activate_checkbox(self):
        checkboxes = self.base_page.customize_menu_list_checkbox

        for i in range(checkboxes.count()):
            if checkboxes.nth(i).is_enabled():
                if not checkboxes.nth(i).is_checked():
                    checkboxes.nth(i).click()
            else:
                continue

    def get_sidebar_list(self):
        sidebar_text = self.base_page.nav_sidebar.nth(0).text_content()
        # Використовуємо регулярний вираз для видалення тексту з числом і "UAH"
        cleaned_text = re.sub(r"-?\d+(\.\d+)?\s*UAH", "", sidebar_text or "")
        return cleaned_text

    def go_to_the_user_profile_page(self):
        self.page.goto("")
        self.base_page.avatar_btn.click()
        self.base_page.user_dd_window.nth(3).click()

    def logout_use_user_window(self):
        self.base_page.avatar_btn.click()
        self.base_page.user_dd_window.nth(4).click()

    def replace_email_invalid_data(self, new_email) -> Locator:
        self.replace_email_btn.click()
        self.new_email_input.fill(new_email)
        self.submit_popup_btn.last.click()
        self.err_msg = self.base_page.mandatory_fields_msg
        return self.err_msg

    def repalce_username(self, f_name: str):
        self.f_name_input.clear()
        self.f_name_input.fill(f_name)
        self.save_btn.click()
        self.submit_popup_btn.click()

    def repalce_lastname(self, l_name: str):
        self.l_name_input.clear()
        self.l_name_input.fill(l_name)
        self.save_btn.click()
        self.submit_popup_btn.click()

    def replace_phone(self, phone: str):
        self.phone_input.clear()
        self.phone_input.fill(phone)
        self.save_btn.click()
        self.submit_popup_btn.click()

    def change_timezone(self, option: str, index: int) -> Locator:
        self.dd_language_timezone.nth(index).click()
        self.listbox.locator("li", has_text=option).click()
        self.page.wait_for_load_state("networkidle")
        self.save_btn.click()
        self.submit_popup_btn.click()
        return self.page.locator("header h1")

    def change_language(self, option: str, index: int) -> Locator:
        self.dd_language_timezone.nth(index).click()
        self.listbox.locator(f"//li[@data-value='{option}']").click()
        self.page.wait_for_load_state("networkidle")
        self.save_btn.click()
        self.submit_popup_btn.click()
        return self.page.locator("header h1")

    def change_password(self, current_pass: str, new_pass: str, repeat_pass):
        self.page.get_by_text("Безпека").click()
        self.change_pass_btn.click()
        self.current_pass_input.fill(current_pass)
        self.new_pass_input.fill(new_pass)
        self.repeat_pass_input.fill(repeat_pass)
        self.submit_popup_btn.click()

    def radio_group(self, index_input):
        self.radio_btn.nth(index_input).click()
        self.sequrety_save_btn.click()
        self.submit_popup_btn.click()

    def input_coordinat_filds(self, mapLatitude, mapLongitude, mapZoom):
        self.mapLatitude_input.clear()
        self.mapLatitude_input.fill(mapLatitude)
        self.mapLongitude_input.clear()
        self.mapLongitude_input.fill(mapLongitude)
        self.mapZoom_input.clear()
        self.mapZoom_input.fill(mapZoom)

    def position_on_map_by_coordinate(self, mapLatitude, mapLongitude, mapZoom):
        self.main_dd_button.last.click()
        if not self.mapLatitude_input.is_visible():
            self.radio_btn.nth(3).click()
        self.radio_btn.nth(2).click(timeout=500)

        self.input_coordinat_filds(mapLatitude, mapLongitude, mapZoom)
        self.sequrety_save_btn.click()

    def position_by_browser(self):
        self.main_dd_button.last.click()
        self.radio_btn.nth(3).click()
        self.sequrety_save_btn.click()
        self.submit_popup_btn.click()
        return self.mapLatitude_input

    def disable_googlemaps_chackbox(self):
        self.main_dd_button.last.click()

        if self.page.get_by_text("Використати приватний ключ Google").is_visible():
            self.checkboxes.last.click()
            self.sequrety_save_btn.click()
            self.submit_popup_btn.click()
            self.main_dd_button.last.click()

    def google_maps_privet_key(self, key):
        self.checkboxes.last.click()
        self.apiKey_input.fill(key)
        self.submit_popup_btn.last.click()
        self.sequrety_save_btn.click()
        self.submit_popup_btn.click()

    def logout_use_dd_profile(self):
        self.base_page.avatar_btn.click()
        self.base_page.user_dd_window.nth(4).click()
