from playwright.sync_api import Page
from pages.base_page import BasePage
import random


class ObjectsPage:

    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.page.goto("/units")

# Dev locators(only for dev) ------------------------------------------------

    # unit head menu locators    
        self.page_tab_buttons = {
            "objects": self.page.locator("#simple-tab-0").nth(1),
            "groups": self.page.locator("#simple-tab-1").nth(0)
        }

        self.head_menu_unit_locators = {
            "filter": self.page.get_by_role("combobox").nth(0),
            "unit_search_input": self.page.locator("input#outlined-basic").nth(0),
            "add_unit": self.page.locator(".MuiGrid-container div > button:nth-child(1)").nth(0),
            "export": self.page.locator(".MuiGrid-container div > button:nth-child(2)"),
            "settings": self.page.locator(".MuiGrid-container div > button button"),
            "customize_panel": self.page.locator("ul[role='menu'] input"),
        }

        self.filter_list = {
            "DEVICE_NAME": self.page.locator("li[data-value='DEVICE_NAME']"),
            "UNIQUE_ID": self.page.locator("li[data-value='UNIQUE_ID']"),
            "PHONE_1": self.page.locator("li[data-value='PHONE']"),
            "PHONE_2": self.page.locator("li[data-value='PHONE_2']"),
            "ACCOUNT": self.page.locator("li[data-value='ACCOUNT']"),
            "MODEL_TRECKER": self.page.locator("li[data-value='MODEL']"),
            "ADMIN_FIELDS": self.page.locator("li[data-value='ADMIN_FIELDS']"),
            "CUSTOM_FIELDS": self.page.locator("li[data-value='CUSTOM_FIELDS']")
        }

    # Edit unit popap locators
        self.popap_btn = {
            "cancel": self.page.locator("button:has(+ button[type='submit'])"),
            "ok": self.page.locator("button[type='submit']"),
            "confirm_del": self.page.locator("div[role='dialog'] button").nth(0),
            "cancel_del": self.page.locator("div[role='dialog'] button").nth(1),
            "err_msg": self.page.locator("//form/span"),
            "group_checkboxes": self.page.locator("form input[type='checkbox']")
        }

        self.object_popap_tablist = {
            "new_object_tabs": self.page.locator("div[role='dialog'] div[role='tablist'] button"),
            "main": self.page.locator("div[role='dialog'] button#simple-tab-0"),
            "access": self.page.locator("div[role='dialog'] button#simple-tab-1"),
            "sensors": self.page.locator("div[role='dialog'] button#simple-tab-2"),
            "custom_f": self.page.locator("div[role='dialog'] button#simple-tab-3"),
            "admin_f": self.page.locator("div[role='dialog'] button#simple-tab-4"),
            "char": self.page.locator("div[role='dialog'] button#simple-tab-5"),
            "commands": self.page.locator("div[role='dialog'] button#simple-tab-6"),
            "drive_detection": self.page.locator("div[role='dialog'] button#simple-tab-7")
        }

        self.object_popap_tabpanel = {
            "main": self.page.locator("#simple-tabpanel-0"),
            "access": self.page.locator("#simple-tabpanel-1"),
            "sensors": self.page.locator("#simple-tabpanel-2"),
            "custom_f": self.page.locator("#simple-tabpanel-3"),
            "admin_f": self.page.locator("#simple-tabpanel-4"),
            "char": self.page.locator("#simple-tabpanel-5"),
            "commands": self.page.locator("#simple-tabpanel-6"),
            "drive_detection": self.page.locator("#simple-tabpanel-7")
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

    # Row on the page locators
        self.row_on_page = {
            "unit_dd_btn": self.page.get_by_role("combobox").nth(1),
            "groups_dd_btn": self.page.locator("div[role='combobox']").nth(2),
            "previous_page": self.page.get_by_role("button", name="Go to previous page"),
            "next_page": self.page.get_by_role("button", name="Go to next page"),
            "10": self.page.locator("ul li").nth(0),
            "25": self.page.locator("ul li").nth(1),
            "50": self.page.locator("ul li").nth(2),
            "100": self.page.locator("ul li").nth(3),
            "unit_total_p": self.page.locator("#display-tabpanel-0 .MuiTablePagination-displayedRows"),
            "groups_total_p": self.page.locator("#display-tabpanel-1 .MuiTablePagination-displayedRows")
        }
        
    # group head menu locators
        self.head_menu_group_locators = {
            "add_group": self.page.locator(".MuiGrid-container div > button:nth-child(1)").nth(1),
            "group_search_input": self.page.locator("input#outlined-basic").nth(1),
        }

    # table locators
        self.unit_table = {
            "head_column": self.page.locator("#display-tabpanel-0 table thead tr th"),
            "body_row": self.page.locator("#display-tabpanel-0 table tbody tr"),
            "btns_in_row": self.page.locator("#display-tabpanel-0 table tbody tr td button"),
        }
        
        self.group_table = {
            "head_column": self.page.locator("#display-tabpanel-1 table thead tr th"),
            "body_row": self.page.locator("#display-tabpanel-1 table tbody tr"),
            "btns_in_row": self.page.locator("#display-tabpanel-1 table tbody tr td button"),
            "expand_btn": self.page.locator("svg[role='openGroup']"),
            "del_btn_in_row": self.page.locator("#display-tabpanel-1 tbody tr:first-child td:last-child button"),
            "alert_msg": self.page.locator("div[role='alert']")
        }

# -----------------------------------------------------------------------------


# # Head menu objects page locators
#         self.search_input = self.page.locator("input#outlined-basic")
#         self.heaer_menu_object_locators = self.page.locator("#display-tabpanel-0 .MuiGrid-container:first-of-type button")
#         self.head_menu_gruop_locators = self.page.locator("#display-tabpanel-1 .MuiGrid-container:first-of-type button")
#         self.customize_panel_checkbox = self.page.locator("ul[role='menu'] input")

#         self.head_menu_buttons = {
#             "objects": self.heaer_menu_object_locators.nth(0),
#             "groups": self.heaer_menu_object_locators.nth(1),
#             "search_input": self.search_input.nth(0),
#             "add": self.heaer_menu_object_locators.nth(3),
#             "settings": self.heaer_menu_object_locators.nth(4),
#             "transfer": self.heaer_menu_object_locators.nth(6)
#         }
    
#     # Group locators
#         self.head_menu_gruop_buttons = {
#             "object": self.head_menu_gruop_locators.nth(0),
#             "group": self.head_menu_gruop_locators.nth(1),
#             "search_input": self.search_input.nth(1),
#             "add": self.head_menu_gruop_locators.nth(3),

#         }

#         # New group popap locators
#         self.group_checkboxes = self.page.locator("form input[type='checkbox']")

#         self.group_popap = {
#         "search_group_in_group": self.search_input.nth(2),
#         "group_name": self.page.locator("input[name='name']"),
#         "cancel": self.page.locator("//button[@type='submit']/preceding-sibling::button"),
#         "ok": self.page.locator("//button[@type='submit']")
#         }

# # Edit objectd popap locators
#         self.popap_btn = {
#             "cancel": self.page.locator("form button[tabindex='0']").nth(0),
#             "ok": self.page.locator("form button[tabindex='0']").nth(1),
#             "confirm_del": self.page.locator("div[role='dialog'] button").nth(0),
#             "cancel_del": self.page.locator("div[role='dialog'] button").nth(1)
#         }

#         self.object_popap_tablist = {
#             "new_object_tabs": self.page.locator("div[role='dialog'] div[role='tablist'] button"),
#             "main": self.page.locator("div[role='dialog'] button#simple-tab-0"),
#             "access": self.page.locator("div[role='dialog'] button#simple-tab-1"),
#             "sensors": self.page.locator("div[role='dialog'] button#simple-tab-2"),
#             "custom_f": self.page.locator("div[role='dialog'] button#simple-tab-3"),
#             "admin_f": self.page.locator("div[role='dialog'] button#simple-tab-4"),
#             "char": self.page.locator("div[role='dialog'] button#simple-tab-5"),
#             "commands": self.page.locator("div[role='dialog'] button#simple-tab-6"),
#             "drive_detection": self.page.locator("div[role='dialog'] button#simple-tab-7")
#         }

#         self.object_popap_tabpanel = {
#             "main": self.page.locator("#simple-tabpanel-0"),
#             "access": self.page.locator("#simple-tabpanel-1"),
#             "sensors": self.page.locator("#simple-tabpanel-2"),
#             "custom_f": self.page.locator("#simple-tabpanel-3"),
#             "admin_f": self.page.locator("#simple-tabpanel-4"),
#             "char": self.page.locator("#simple-tabpanel-5"),
#             "commands": self.page.locator("#simple-tabpanel-6"),
#             "drive_detection": self.page.locator("#simple-tabpanel-7")
#         }


#         self.object_main_popap_inputs = {
#             "name": self.page.locator("input[name='name']"),
#             "unique_id": self.page.locator("input[name='uniqueId']"),
#             "phone_1": self.page.locator("form input#outlined-basic").nth(0),
#             "phone_2": self.page.locator("form input#outlined-basic").nth(1),
#             "model": self.page.locator("input#combo-box-demo"),
#             "device_type": self.page.locator("#demo-simple-select"),
#             "protocol": self.page.locator("form input").nth(3),
#             "adress_server": self.page.locator("form input").nth(5),
#             "owner": self.page.locator("form input").nth(7),
#             "date_of_create": self.page.locator("form input").nth(9),
#         }

#         self.types_of_objects = {
#             "VEHICLE": self.page.locator("ul li[data-value='VEHICLE']"),
#             "FUEL_VEHICLE": self.page.locator("ul li[data-value='FUEL_VEHICLE']"),
#             "PERSONAL_TRACKER": self.page.locator("ul li[data-value='PERSONAL_TRACKER']"),
#             "BEACON": self.page.locator("ul li[data-value='BEACON']")
#         }

# # Objects table locators
#         self.ob_tablet_head = self.page.locator("#display-tabpanel-0 table thead tr th")
#         self.ob_tablet_body = self.page.locator("#display-tabpanel-0 table tbody tr")
#         self.group_tablet_head = self.page.locator("#display-tabpanel-1 table thead tr th")
#         self.group_tablet_body = self.page.locator("#display-tabpanel-1 table tbody tr")

#         self.group_table_btns = self.page.locator("#display-tabpanel-1 table tbody tr td button")
#         self.expand_btn = self.page.locator("svg[role='openGroup']")
#         self.alert_msg = self.page.locator("div[role='alert']")
#         self.del_group_btn = self.page.locator("#display-tabpanel-1 tbody tr:first-child td:last-child button")

# # Error message locators
#         self.error_msg = self.page.locator("//form/span")

# # Row on the page locators
#         self.row_on_page = {
#             "objects_dd_btn": self.page.get_by_role("combobox").nth(0),
#             "groups_dd_btn": self.page.locator("div[role='combobox']").nth(1),
#             "objects_previous_page": self.page.get_by_role("button", name="Go to previous page"),
#             "objects_next_page": self.page.get_by_role("button", name="Go to next page"),
#             "group_previous_page": self.page.get_by_role("button", name="Go to previous page"),
#             "group_next_page": self.page.get_by_role("button", name="Go to next page"),
#             "10": self.page.locator("ul li").nth(0),
#             "25": self.page.locator("ul li").nth(1),
#             "50": self.page.locator("ul li").nth(2),
#             "100": self.page.locator("ul li").nth(3),
#             "objects_total_p": self.page.locator(".MuiTablePagination-displayedRows").nth(0),
#             "groups_total_p": self.page.locator(".MuiTablePagination-displayedRows").nth(1)
#         }


    def unique_id(self):
        unique_id = ''.join(random.choices('0123456789', k=random.randint(5, 20)))
        return unique_id


    # def add_new_object(self, name: str, phone_1: str, phone_2: str, model: str, device_type: str):
    #     """device_type = VEHICLE, FUEL_VEHICLE, PERSONAL_TRACKER, BEACON"""
    #     unique_id = self.unique_id()
    #     self.head_menu_buttons["add"].click()
    #     self.object_main_popap_inputs["name"].fill(name)
    #     self.object_main_popap_inputs["phone_1"].fill(phone_1)
    #     self.object_main_popap_inputs["phone_2"].fill(phone_2)
    #     if device_type:
    #         self.object_main_popap_inputs["unique_id"].fill(unique_id)
    #         self.object_main_popap_inputs["device_type"].click()  
    #         self.types_of_objects[device_type].click()
    #     self.object_main_popap_inputs["model"].fill(model)

    def add_new_object(self, name: str, phone_1: str, phone_2: str, model: str, device_type: str): # dev-staging
        """device_type = VEHICLE, FUEL_VEHICLE, PERSONAL_TRACKER, BEACON"""
        unique_id = self.unique_id()
        self.head_menu_unit_locators["add_unit"].click()
        self.object_main_popap_inputs["name"].fill(name)
        self.object_main_popap_inputs["phone_1"].fill(phone_1)
        self.object_main_popap_inputs["phone_2"].fill(phone_2)
        if device_type:
            self.object_main_popap_inputs["unique_id"].fill(unique_id)
            self.object_main_popap_inputs["device_type"].click()  
            self.types_of_objects[device_type].click()
        self.object_main_popap_inputs["model"].fill(model)

        
    def pause_all_object(self):
        self.page.wait_for_timeout(1000)
        if self.unit_table["body_row"].nth(0).is_visible():
            self.unit_table["head_column"].nth(0).click()
            self.page.wait_for_timeout(1000)
            self.unit_table["head_column"].nth(14).click()
            self.popap_btn["confirm_del"].click()
            self.page.wait_for_timeout(1000)


    def move_to_trash_all_object(self): # dev-staging
        self.page.wait_for_timeout(1000)
        if self.unit_table["body_row"].nth(0).is_visible():
            self.unit_table["head_column"].nth(0).click()
            self.page.wait_for_timeout(1000)
            self.unit_table["head_column"].last.click()
            self.popap_btn["confirm_del"].click()
            self.page.wait_for_timeout(1000)

    
    def edit_unit_column_table(self):
        checkbox = self.head_menu_unit_locators["customize_panel"]
        for index in range(checkbox.count()):
            checkbox.nth(index).click()


    def precondition_add_multiple_objects(self, count: int, name: str, phone_1: str, phone_2: str, model: str, device_type: str):
        for _ in range(count):
            self.add_new_object(name, phone_1, phone_2, model, device_type)
            self.popap_btn["ok"].click()
            self.page.wait_for_timeout(1000)


    def search_object(self, filter: str, query: str):
        self.head_menu_unit_locators["filter"].click()
        self.filter_list[filter].click()
        self.head_menu_unit_locators["unit_search_input"].fill(query)
        self.page.wait_for_timeout(1000)


    def check_pagelist(self, arrow_btn: str, total_expect):
        self.row_on_page[arrow_btn].click()
        self.page.wait_for_timeout(1000)

        return self.row_on_page[total_expect]


    def increase_decrease_the_number(self, number: str):
        self.row_on_page["unit_dd_btn"].click()
        self.row_on_page[number].click()
        self.page.wait_for_timeout(1000)
        
        return self.unit_table["body_row"]


    def increase_decrease_the_number_group(self, number: str):
        self.row_on_page["groups_dd_btn"].click()
        self.row_on_page[number].click()
        self.page.wait_for_timeout(1000)
        
        return self.group_table["body_row"]
      

    def add_new_group(self, name: str, units: int):
        self.head_menu_group_locators["add_group"].click()
        self.object_main_popap_inputs["name"].fill(name)
        for i in range(1, units + 1):
            self.popap_btn["group_checkboxes"].nth(i).check()
        self.page.wait_for_timeout(500)

    def remove_group(self):
        self.group_table["del_btn_in_row"].click()
        self.popap_btn["confirm_del"].click() 

