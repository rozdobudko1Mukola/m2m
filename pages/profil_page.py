from playwright.sync_api import Page
from pages.base_page import BasePage
import re


class ProfilePage:

    PROFILE_PAGE_URL = "https://staging.m2m.eu/user"

    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page) 
        self.page.goto(self.PROFILE_PAGE_URL)

    
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
        
