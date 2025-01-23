from playwright.sync_api import Page
from pages.base_page import BasePage
import random


class ObjectsPage:

    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.page.goto("/units")


# Head menu objects page locators
        self.search_input = self.page.locator("#display-tabpanel-0 input#outlined-basic")
        self.heaer_menu_locators = self.page.locator("#display-tabpanel-0 .MuiGrid-container:first-of-type button")
        self.customize_panel_checkbox = self.page.locator("ul[role='menu'] input")

        self.head_menu_buttons = {
            "objects": self.heaer_menu_locators.nth(0),
            "groups": self.heaer_menu_locators.nth(1),
            "search_input": self.search_input,
            "add": self.heaer_menu_locators.nth(3),
            "settings": self.heaer_menu_locators.nth(4),
            "transfer": self.heaer_menu_locators.nth(6)
        }

# Edit objectd popap locators
        self.popap_btn = {
            "cancel": self.page.locator("form button[tabindex='0']").nth(0),
            "ok": self.page.locator("form button[tabindex='0']").nth(1),
            "confirm_del": self.page.locator("div[role='dialog'] button").nth(0),
            "cancel_del": self.page.locator("div[role='dialog'] button").nth(1)
        }

        self.object_popap_tablist = {
            "main": self.page.locator("button#simple-tab-1"),
            "access": self.page.locator("button#simple-tab-2"),
            "sensors": self.page.locator("button#simple-tab-3"),
            "custom_f": self.page.locator("button#simple-tab-4"),
            "Char": self.page.locator("button#simple-tab-5"),
            "commands": self.page.locator("button#simple-tab-6")
        }

        self.object_main_popap_inputs = {
            "name": self.page.locator("input[name='name']"),
            "unique_id": self.page.locator("input[name='uniqueId']"),
            "phone_1": self.page.locator("form input#outlined-basic").nth(0),
            "phone_2": self.page.locator("form input#outlined-basic").nth(1),
            "model": self.page.locator("input#combo-box-demo"),
            "device_type": self.page.locator("#demo-simple-select"),
            "protocol": self.page.locator("form input").nth(3),
            "adress_server": self.page.locator("form input").nth(5),
            "owner": self.page.locator("form input").nth(7),
            "date_of_create": self.page.locator("form input").nth(9),
        }

        self.types_of_objects = {
            "VEHICLE": self.page.locator("ul li[data-value='VEHICLE']"),
            "FUEL_VEHICLE": self.page.locator("ul li[data-value='FUEL_VEHICLE']"),
            "PERSONAL_TRACKER": self.page.locator("ul li[data-value='PERSONAL_TRACKER']"),
            "BEACON": self.page.locator("ul li[data-value='BEACON']")
        }

# Objects lable locators
        self.ob_tablet_head = self.page.locator("table thead tr th")
        self.ob_tablet_body = self.page.locator("table tbody tr")

# Error message locators
        self.error_msg = self.page.locator("//form/span")


    def unique_id(self):
        unique_id = ''.join(random.choices('0123456789', k=random.randint(5, 20)))
        return unique_id


    def add_new_object(self, name: str, phone_1: str, phone_2: str, model: str, device_type: str):
        """device_type = VEHICLE, FUEL_VEHICLE, PERSONAL_TRACKER, BEACON"""
        unique_id = self.unique_id()
        self.head_menu_buttons["add"].click()
        self.object_main_popap_inputs["name"].fill(name)
        self.object_main_popap_inputs["phone_1"].fill(phone_1)
        self.object_main_popap_inputs["phone_2"].fill(phone_2)
        if device_type:
            self.object_main_popap_inputs["unique_id"].fill(unique_id)
            self.object_main_popap_inputs["device_type"].click()  
            self.types_of_objects[device_type].click()
        self.object_main_popap_inputs["model"].fill(model)

        
    def pause_all_object(self):
        if self.ob_tablet_body.nth(0).is_visible():
            self.ob_tablet_head.nth(0).click()
            self.page.wait_for_timeout(1000)
            self.ob_tablet_head.nth(12).click()
            self.popap_btn["confirm_del"].click()
            self.page.wait_for_timeout(1000)

    
    def edit_object_table(self):
        checkbox = self.customize_panel_checkbox
        for index in range(checkbox.count()):
            checkbox.nth(index).click()


    def precondition_add_multiple_objects(self, count: int, name: str, phone_1: str, phone_2: str, model: str, device_type: str):
        for _ in range(count):
            self.add_new_object(name, phone_1, phone_2, model, device_type)
            self.popap_btn["ok"].click()
            self.page.wait_for_timeout(1000)
