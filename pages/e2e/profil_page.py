from playwright.sync_api import Page, expect, Locator
import time
from pages.e2e.base_page import BasePage
import re


class ProfilePage:

    def __init__(self, page: Page):
        self.page = page

        self.general_tab = {
            "f_name_input": page.locator("input[name='firstName']"),
            "l_name_input": page.locator("input[name='lastName']"),
            "phone_input": page.locator("input[name='phone']"),
            "replace_email_btn": page.get_by_role("button", name="Змінити email"),
            "save_btn": page.locator("((//h3)[1]//following-sibling::div//button)[2]"),
            "general_tab_btn": page.locator("h3 button").nth(0),
            "language_dropdown": page.locator("//input[@name='language']/preceding-sibling::div"),
            "timezone_dropdown": page.locator("//input[@name='timezone']/preceding-sibling::div"),
            "current_email_input": page.locator("input[id='outlined-basic']").first,
        }

        self.language_lists = {
            'en': page.get_by_role("option", name="English"),
            'ua': page.get_by_role("option", name="Українська"),
            'ru': page.get_by_role("option", name="Русский"),
        }

        self.timezone_lists = {
            'kiev': page.get_by_role("option", name="Europe/Kyiv [+03:00]"),
            'london': page.get_by_role("option", name="Europe/London [+01:00]"),
        }

        self.repalse_email_popup = {
            "new_email_input": page.locator("input[name='newEmail']"),
        }

        self.security_tab = {
            "sequrity_tab_btn": page.locator("h3 button").nth(1),
            "change_pass_btn": page.locator("((//h3)[2]//following-sibling::div//button)[1]"),
            "save_btn": page.locator("((//h3)[2]//following-sibling::div//button)[2]"),
            "msg_raio_off": page.locator("((//h3)[2]//following-sibling::div//div[@role='radiogroup']//input)[1]"),
            "msg_raio_on_email": page.locator("((//h3)[2]//following-sibling::div//div[@role='radiogroup']//input)[2]"),
        }

        self.change_pass_popup = {
            "current_pass_input": page.locator("input[name='oldPassword']"),
            "new_pass_input": page.locator("input[name='newPassword']"),
            "repeat_pass_input": page.locator("input[name='repeatPassword']"),
        }

        self.pop_confirm_btn = {
            "submit_popup_btn": page.locator("div[role='presentation'] form button[type='submit']").first,
            "change_save_apply_btn": page.locator("div[role='presentation'] form button[type='submit']").last,
            "confirm_btn": page.locator("div[role='dialog'] button[type='button']"),
            "modal_name": page.locator(
                "//span[contains(text(), 'Changes saved') or "
                "contains(text(), 'Зміни збережено') or "
                "contains(text(), 'Изменения сохранены')]"
            ),
        }

        self.map_tab = {
            "map_tab_btn": page.locator("h3 button").nth(2),
            "by_coordinates_radio": page.locator("(((//h3)[3]/following-sibling::div//div[@role='radiogroup'])[1]//input)[1]"),
            "by_browser_radio": page.locator("(((//h3)[3]/following-sibling::div//div[@role='radiogroup'])[1]//input)[2]"),
            "save_btn": page.locator("((//h3)[3]//following-sibling::div//button)"),
            "google_maps_checkbox": page.locator("((//h3)[3]/following-sibling::div//input[@type='checkbox'])[2]"),
            "open_street_maps_checkbox": page.locator("((//h3)[3]/following-sibling::div//input[@type='checkbox'])[1]"),
            "map_latitude_input": page.locator("input[name='mapLatitude']"),
            "map_longitude_input": page.locator("input[name='mapLongitude']"),
            "map_zoom_input": page.locator("input[name='mapZoom']"),
            "google_privat_key_radio": page.locator("(((//h3)[3]/following-sibling::div//div[@role='radiogroup'])[2])")
        }

        self.privet_key_google_pop = {
            "input": page.locator("div[role='dialog'] input"),
            "cancel_btn": page.locator("div[role='dialog'] button").first,
            "ok_btn": page.locator("div[role='dialog'] button").last,
            "popup": page.locator("div[role='dialog'] h2[id='alert-dialog-title']"),
        }

        self.errors = {
            "err_msg": page.locator("form p")
        }

    def get_general_tab_input(self, input_name: str, test_value: str,) -> Locator:
        """
        input_name are "f_name_input", "l_name_input", "phone_input"
        Заповнює поле у вкладці 'Загальні' тестовим значенням, зберігає зміни
        та повертає локатор цього поля для подальшої перевірки.
        """
        self.page.wait_for_load_state("networkidle")
        self.general_tab[input_name].clear()
        self.general_tab[input_name].fill(test_value)
        self.general_tab["save_btn"].click()
        expect(self.pop_confirm_btn["modal_name"]).to_be_visible()
        self.pop_confirm_btn["confirm_btn"].click()
        return self.general_tab[input_name]  # Returns the updated input value

    def get_general_tab_dd(self, dd_name: str, option: str) -> Locator:
        """
        dd_name are "language_dropdown", "timezone_dropdown"
        option are "en", "ua", "ru" for language and "kiev", "london" for timezone
        """
        self.general_tab[dd_name].click()
        self.page.wait_for_timeout(500)  # Wait for the dropdown to open

        if dd_name == "language_dropdown":
            self.language_lists[option].click()
        elif dd_name == "timezone_dropdown":
            self.timezone_lists[option].click()

        self.general_tab["save_btn"].click()
        expect(self.pop_confirm_btn["modal_name"]).to_be_visible()
        self.pop_confirm_btn["confirm_btn"].click()
        return self.general_tab[dd_name]

    def switch_beatween_tabs(self, tab_name: str) -> Locator:
        """
        tab_name are "general_tab", "security_tab", "map_tab"
        Switches to the specified tab and returns the locator for that tab.
        """
        if tab_name == "general_tab":
            self.general_tab["general_tab_btn"].click()
            return self.general_tab["f_name_input"]
        elif tab_name == "security_tab":
            self.security_tab["sequrity_tab_btn"].click()
            return self.security_tab["change_pass_btn"]
        elif tab_name == "map_tab":
            self.map_tab["map_tab_btn"].click()
            return self.map_tab["by_coordinates_radio"]
        raise ValueError(f"Unknown tab_name: {tab_name}")

    def change_password(self, current_pass: str, new_pass: str, repeat_pass: str) -> Locator:
        """
        Changes the password by filling in the current password, new password, and repeat password fields.
        Returns the locator for the change password button.
        """
        self.security_tab["change_pass_btn"].click()
        self.change_pass_popup["current_pass_input"].fill(current_pass)
        self.change_pass_popup["new_pass_input"].fill(new_pass)
        self.change_pass_popup["repeat_pass_input"].fill(repeat_pass)
        self.pop_confirm_btn["submit_popup_btn"].click()
        return self.errors["err_msg"]

    def change_block_msg(self, option: str,) -> Locator:
        """
        Changes the block message setting by clicking the corresponding radio button.
        option are "msg_raio_off", "msg_raio_on_email"
        """
        self.security_tab[option].click()
        self.security_tab["save_btn"].click()
        self.pop_confirm_btn["confirm_btn"].click()
        return self.security_tab[option]

    def check_map_position(self, radio) -> Locator:
        """
        radio is either "by_coordinates_radio" or "by_browser_radio"
        """
        self.map_tab[radio].click()
        self.map_tab["save_btn"].click()
        self.pop_confirm_btn["confirm_btn"].click()
        self.map_tab["map_tab_btn"].click()
        return self.map_tab[radio]

    def change_map_coordinates(self, latitude: str, longitude: str, zoom: str, radio):
        """
        Changes the map coordinates by filling in the latitude, longitude, and zoom fields.
        radio is either "by_coordinates_radio" or "by_browser_radio"
        """

        # обираємо потрібний спосіб
        self.map_tab[radio].click()

        # вводимо значення
        self.map_tab["map_latitude_input"].clear()
        self.map_tab["map_latitude_input"].fill(latitude)

        self.map_tab["map_longitude_input"].clear()
        self.map_tab["map_longitude_input"].fill(longitude)

        self.map_tab["map_zoom_input"].clear()
        self.map_tab["map_zoom_input"].fill(zoom)

        # зберігаємо
        self.map_tab["save_btn"].click()
        time.sleep(1)  # Дочекаємось появи попапу

        if self.pop_confirm_btn["modal_name"].is_visible():
            # успішний сценарій
            self.pop_confirm_btn["confirm_btn"].click()
            self.map_tab["map_tab_btn"].click()

            expect(self.map_tab["map_latitude_input"]).to_have_value(latitude)
            expect(self.map_tab["map_longitude_input"]).to_have_value(longitude)
            expect(self.map_tab["map_zoom_input"]).to_have_value(zoom)
        else:
            # невалідні дані → перевіряємо помилки
            expect(self.errors["err_msg"].first).to_have_text("Максимальне значення 90")
            expect(self.errors["err_msg"].nth(1)).to_have_text("Максимальне значення 180")
            expect(self.errors["err_msg"].nth(2)).to_have_text("Максимальне значення 18")

    def google_maps_checkbox(self):
        self.map_tab["google_maps_checkbox"].click(force=True)
        self.map_tab["save_btn"].click()
        self.pop_confirm_btn["confirm_btn"].click()
        self.map_tab["map_tab_btn"].click()
        return self.map_tab["google_privat_key_radio"]

    def enter_google_maps_key(self, key: str) -> Locator:
        """
        Enters the Google Maps API key in the popup dialog.
        """
        if self.map_tab["google_privat_key_radio"].is_visible():
            self.map_tab["google_maps_checkbox"].click(force=True)
            time.sleep(1)
            self.map_tab["google_maps_checkbox"].click(force=True)
            self.privet_key_google_pop["input"].fill(key)
            self.privet_key_google_pop["ok_btn"].click()
            time.sleep(1)  # Дочекаємось появи попапу
            self.map_tab["save_btn"].click()
            self.pop_confirm_btn["confirm_btn"].click()
            self.map_tab["map_tab_btn"].click()
            time.sleep(1)
            if self.map_tab["google_privat_key_radio"].is_visible():
                self.map_tab["google_maps_checkbox"].click(force=True)
                time.sleep(1)
                self.map_tab["google_maps_checkbox"].click(force=True)
                time.sleep(1)
            else:
                self.map_tab["google_maps_checkbox"].click(force=True)
            return self.privet_key_google_pop["input"]
        else:
            # Якщо чекбокс не видимий, то повертаємо помилку
            raise ValueError("Google Maps checkbox is not visible. Cannot enter API key.")

# elder class ProfilePage:


class settingUp:
    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)

        self.bg_color_locator = self.page.locator("header")
        self.black_bg_color = "rgb(26, 46, 71)"
        self.white_bg_color = "rgb(255, 255, 255)"
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

    def logout_use_dd_profile(self):
        self.base_page.avatar_btn.click()
        self.base_page.user_dd_window.nth(4).click()
