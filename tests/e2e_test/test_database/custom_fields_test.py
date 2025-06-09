import pytest
from pytest import mark
from playwright.sync_api import Page, expect
from pages.e2e.database.objects import ObjectsPage
from pages.e2e.database.admin_custom_fields import CustomAdminFieldsPage
from playwright.sync_api import APIRequestContext 
from pages.api.devices_api import DeviceAPI
import time


@pytest.fixture()
def revove_custom_filds(api_context: APIRequestContext, token: str, test_data):
    """Видалити кастомні поля"""
    
    # Clean up code
    device_api = DeviceAPI(api_context, token)
    device_ids = test_data.get("device_ids", [])
    if device_ids:
        response = device_api.update_custom_fields_for_device(device_id=device_ids[0], customFields="{}")
        expect(response).to_be_ok()

    yield


class TestCustomFields:
    """Тестування кастомних полів"""

    err_text_msg = "Обов'язкове поле"  # Error message for required field
    err_color_msg = "rgb(211, 47, 47)"  # Red color for error message
    
    # Відкрити вкладку "Довільні поля" в попапі налаштування обʼєкту
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T56f7967a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_open_custom_fields_tab(self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds):
        """ ||T56f7967a|| Відкрити вкладку "Довільні поля" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        expect(objects_page.object_popap_tablist["custom_f"]).to_be_visible() # Check that the tab is opened
        expect(custom_fields_page.empty_fields.nth(0)).to_be_enabled() # Check that the first empty name field is enabled
        expect(custom_fields_page.empty_fields.nth(1)).to_be_enabled()
        expect(custom_fields_page.save_btn).to_be_disabled() # Check that the save button is disabled

    
    # Заповнити дані вкладки "Довільні поля" мінімально допустимими значеннями в попапі налаштування обʼєкту
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@Tbd40696c')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_fill_custom_fields_tab(self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds):
        """ ||Tbd40696c|| Заповнити дані вкладки "Довільні поля" мінімально допустимими значеннями в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "1") # Fill the first empty name field
        custom_fields_page.fill_field("value", "q") # Fill the first empty value field
        custom_fields_page.save_btn.click() # Click the save button

        expect(custom_fields_page.get_field("name", 0)).to_have_value("1")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("q")
        expect(custom_fields_page.get_field("name", 0)).to_be_disabled() # Check that the first name field is disabled
        expect(custom_fields_page.get_field("value", 0)).to_be_enabled() # Check that the first value field is enabled
        expect(custom_fields_page.save_btn).to_be_disabled() # Check that the save button is disabled
        expect(custom_fields_page.del_btn.nth(0)).to_be_enabled() # Check that the delete button is enabled


    # Заповнити дані вкладки "Довільні поля" максимально допустимими значеннями в попапі налаштування обʼєкту
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T53fa39e0')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_fill_custom_fields_tab_max(self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds):
        """ ||T53fa39e0|| Заповнити дані вкладки "Довільні поля" максимально допустимими значеннями в попапі налаштування обʼєкту """
        
        name_f = "name! from counting words and characters, online editor help you to improve word choice and writing!" # 100 symbols
        value_f = "value! from counting words and characters, online editor help you to improve word choice and writing!" # 100 symbols
        
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", name_f) # Fill the first empty name field
        custom_fields_page.fill_field("value", value_f) # Fill the first empty value field
        custom_fields_page.save_btn.click() # Click the save button

        expect(custom_fields_page.get_field("name", 0)).to_have_value(name_f)
        expect(custom_fields_page.get_field("value", 0)).to_have_value(value_f)
        expect(custom_fields_page.get_field("name", 0)).to_be_disabled() # Check that the first name field is disabled
        expect(custom_fields_page.get_field("value", 0)).to_be_enabled() # Check that the first value field is enabled
        expect(custom_fields_page.save_btn).to_be_disabled() # Check that the save button is disabled
        expect(custom_fields_page.del_btn.nth(0)).to_be_enabled() # Check that the delete button is enabled


    # Видалення рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T34f0b7cc')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [2], indirect=True)
    def test_remove_custom_fields(self, user_page, full_unit_create_and_remove_by_api):
        """ ||@T34f0b7cc|| Видалення рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(1).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.del_btn.nth(0).click() # Click the delete button

        expect(custom_fields_page.empty_fields.nth(0)).to_be_enabled() # Check that the first empty name field is enabled
        expect(custom_fields_page.empty_fields.nth(1)).to_be_enabled()
        expect(custom_fields_page.save_btn).to_be_disabled() # Check that the save button is disabled
        expect(custom_fields_page.del_btn).not_to_be_visible() # Check that the delete button is not visible


    # Створити рядок в вкладці "Довільні поля" заповнивши тільки поле "Імʼя" в попапі налаштування обʼєкту
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T053fd448')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_fill_only_name_fild(self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds):
        """ Створити рядок в вкладці "Довільні поля" заповнивши тільки поле "Імʼя" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        expect(objects_page.object_popap_tablist["custom_f"]).to_be_focused() # Check that the tab is opened
        expect(custom_fields_page.save_btn).to_be_disabled() # Check that the save button is disabled

        custom_fields_page.fill_field("name", "test_name") # Fill the first empty name field
        
        expect(custom_fields_page.save_btn).to_be_disabled()


    # Створити рядок в вкладці "Довільні поля" заповнивши тільки поле "Значення" в попапі налаштування обʼєкту @function @negative
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T3a44f6cc')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_fill_only_value_fild(self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds):
        """ Створити рядок в вкладці "Довільні поля" заповнивши тільки поле "Значення" в попапі налаштування обʼєкту @function @negative """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        expect(objects_page.object_popap_tablist["custom_f"]).to_be_focused() # Check that the tab is opened
        expect(custom_fields_page.save_btn).to_be_disabled() # Check that the save button is disabled

        custom_fields_page.fill_field("value", "test_name") # Fill the first empty name field
        
        expect(custom_fields_page.save_btn).to_be_disabled()


    # Редагування рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту 
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T30777dcd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_edit_custom_fields(self, user_page, full_unit_create_and_remove_by_api):
        """ ||T30777dcd|| Редагування рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(2).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.get_field("value", 0).fill("test") # Fill the first empty value field with new value
        custom_fields_page.save_btn.click() # Click the save button

        expect(custom_fields_page.get_field("value", 0)).to_have_value("test")


    # Редагування рядку з даними вкладки "Довільні поля" вказавши пусті дані поля "Значення" в попапі налаштування обʼєкту 
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T4652de4e')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_edit_custom_fields_empty_value(self, user_page, full_unit_create_and_remove_by_api):
        """ ||T4652de4e|| Редагування рядку з даними вкладки "Довільні поля" вказавши пусті дані поля "Значення" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(2).click()

        # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty
        time.sleep(2)  # Wait for the modal to open

        objects_page.object_popap_tablist["custom_f"].click()
        custom_fields_page.get_field("value", 0).fill("")
        # Fill the first empty value field with new value
        custom_fields_page.save_btn.click()

        expect(custom_fields_page.error["msg"]).to_be_visible()
        expect(custom_fields_page.error["msg"]).to_have_text(self.err_text_msg)
        expect(custom_fields_page.error["msg"]).to_have_css("color", self.err_color_msg)


    # Перевірка появи модального вікна при переході на іншу вкладку якшо є не збережені дані у вкладці "Довільні поля" в попапі налаштування обʼєкту
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@Tc7eef2e0')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_check_modal_window(self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds):
        """ ||Tc7eef2e0|| Перевірка появи модального вікна при переході на іншу вкладку якшо є не збережені дані у вкладці "Довільні поля" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "test_name") # Fill the first empty name field
        custom_fields_page.fill_field("value", "test_value") # Fill the first empty value field

        objects_page.object_popap_tablist["main"].click()
        expect(custom_fields_page.modal_window["modal_title"]).to_be_visible() # Check that the modal window is visible

        custom_fields_page.modal_window["save_btn"].click()
        objects_page.object_popap_tablist["custom_f"].click()
        expect(custom_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("test_value")


    # Перевірка появи модального вікна при закриті попапу налаштування обʼєкту якшо є не збережені дані у вкладці "Довільні поля"
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@Te9322835')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_check_modal_window_close_popap(self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds):
        """ ||Te9322835|| Перевірка появи модального вікна при закриті попапу налаштування обʼєкту якшо є не збережені дані у вкладці "Довільні поля" """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "test_name") # Fill the first empty name field
        custom_fields_page.fill_field("value", "test_value") # Fill the first empty value field

        objects_page.popap_btn["x_btn"].click() # Close the pop-up window

        expect(custom_fields_page.modal_window["modal_title"]).to_be_visible() # Check that the modal window is visible
        custom_fields_page.modal_window["save_btn"].click()
        time.sleep(1)  # Wait for the modal to close

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty() # Check that the model field is not empty
        time.sleep(1)  # Wait for the modal to close

        objects_page.object_popap_tablist["custom_f"].click()

        expect(custom_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("test_value")
