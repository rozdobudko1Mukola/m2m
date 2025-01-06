from playwright.sync_api import Page
from pages.base_page import BasePage
import re


class ProfilePage:

    BASE_URL = "https://staging.m2m.eu"
    PROFILE_PAGE_URL = f"{BASE_URL}/user"

    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page) 
        self.page.goto(self.PROFILE_PAGE_URL)

        self.bg_color_locator = self.page.locator("body main")
        self.black_bg_color = "rgb(12, 31, 55)"
        self.white_bg_color = "rgb(245, 245, 245)"
        self.red_fild_err_border = self.page.locator("form fieldset")

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

        # dropdown list locator
        self.dropdown_list = self.page.locator("ul")
        self.main_dd_button = self.page.locator("//main//div[@role='button']")

        # security tab locators
        self.radio_group = self.page.get_by_role("radiogroup")
        self.change_pass_btn = self.page.get_by_role("button", name="Змінити пароль")
        self.radio_msg_onmail = self.page.locator("//input[@type='radio']")

        # maps tab locators
        self.gmaps_checkbox = self.page.get_by_text("Google Maps")

    
    def switch_bg_color(self):
        self.base_page.bg_color_switcher.click()


    def open_notifications(self):
        self.base_page.open_notifications_btn.click()


    def close_notifications(self):
        self.base_page.close_notifications_btn.click()


    def get_time_on_site(self) -> str:
        current_time = self.base_page.current_time.text_content()
        current_time_formatted = ":".join(current_time.split(":")[:2])
        return current_time_formatted


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
                if checkboxes.nth(i).is_checked() == False:
                    checkboxes.nth(i).click()
            else:
                continue

    
    def get_sidebar_list(self):
        sidebar_text = self.base_page.nav_sidebar.nth(0).text_content()
        # Використовуємо регулярний вираз для видалення тексту з числом і "UAH"
        cleaned_text = re.sub(r"-?\d+(\.\d+)?\s*UAH", "", sidebar_text)
        return cleaned_text
        

    def go_to_the_user_profile_page(self):
        self.page.goto(self.BASE_URL)
        self.base_page.avatar_btn.click()
        self.base_page.user_dd_window.nth(3).click()


    def logout_use_user_window(self):
        self.base_page.avatar_btn.click()
        self.base_page.user_dd_window.nth(4).click()


    def replace_email_invalid_data(self, new_email) -> str:
        self.replace_email_btn.click()
        self.new_email_input.fill(new_email)
        self.submit_popup_btn.last.click()
        self.err_msg = self.base_page.mandatory_fields_msg
        return self.err_msg


    def repalce_username(self, f_name="", l_name="", phone="") -> str:
        self.f_name_input.clear()
        self.f_name_input.fill(f_name)
        self.l_name_input.clear()
        self.l_name_input.fill(l_name)
        self.phone_input.clear()
        self.phone_input.fill(phone)
        self.save_btn.click()
        self.submit_popup_btn.click()


    def change_language(self, option: str, index: int) -> str:
        self.dd_language_timezone.nth(index).click()
        self.listbox.locator(f"//li[text()='{option}']").click()
        self.save_btn.click()
        self.submit_popup_btn.click()
        return self.page.locator("header h1")

    
    def change_password(self, current_pass: str, new_pass: str, repeat_pass) -> str:
        self.page.get_by_text("Безпека").click()
        self.change_pass_btn.click()
        self.current_pass_input.fill(current_pass)
        self.new_pass_input.fill(new_pass)
        self.repeat_pass_input.fill(repeat_pass)
        self.submit_popup_btn.click()

    
    def notification_radio_group(self, index) -> str:
        self.page.get_by_text("Безпека").click()
        self.radio_msg_onmail.nth(index).click()
        self.sequrety_save_btn.nth(1).click()
        self.submit_popup_btn.click()
        return self.radio_msg_onmail.nth(index)



    

    


