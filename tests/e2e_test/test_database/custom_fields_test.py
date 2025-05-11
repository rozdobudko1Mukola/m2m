import pytest
from pytest import mark
from playwright.sync_api import Page, expect
from pages.e2e.database.objects import ObjectsPage
from pages.e2e.database.admin_custom_fields import CustomAdminFieldsPage
from playwright.sync_api import APIRequestContext 
from pages.api.devices_api import DeviceAPI


@pytest.fixture(autouse=True)
def revove_custom_filds(api_context: APIRequestContext, token: str, test_data):
    """Видалити кастомні поля"""
    yield
    # Clean up code
    device_api = DeviceAPI(api_context, token)
    device_ids = test_data.get("device_ids", [])
    if device_ids:
        response = device_api.update_custom_fields_for_device(device_id=device_ids[0], customFields="{}")
        expect(response).to_be_ok()


class TestCustomFields:
    """Тестування кастомних полів"""

    # Відкрити вкладку "Довільні поля" в попапі налаштування обʼєкту
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T56f7967a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [2], indirect=True)
    def test_open_custom_fields_tab(self, user_page, full_unit_create_and_remove_by_api):
        """ ||T56f7967a|| Відкрити вкладку "Довільні поля" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
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
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [2], indirect=True)
    def test_fill_custom_fields_tab(self, user_page, full_unit_create_and_remove_by_api):
        """ ||Tbd40696c|| Заповнити дані вкладки "Довільні поля" мінімально допустимими значеннями в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "test_name") # Fill the first empty name field
        custom_fields_page.fill_field("value", "test_value") # Fill the first empty value field
        custom_fields_page.save_btn.click() # Click the save button

        expect(custom_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("test_value")
        expect(custom_fields_page.get_field("name", 0)).to_be_disabled() # Check that the first name field is disabled
        expect(custom_fields_page.get_field("value", 0)).to_be_enabled() # Check that the first value field is enabled
        expect(custom_fields_page.save_btn).to_be_disabled() # Check that the save button is disabled
        expect(custom_fields_page.del_btn.nth(0)).to_be_enabled() # Check that the delete button is enabled


    # Заповнити дані вкладки "Довільні поля" максимально допустимими значеннями в попапі налаштування обʼєкту
    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T53fa39e0')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [2], indirect=True)
    def test_fill_custom_fields_tab_max(self, user_page, full_unit_create_and_remove_by_api):
        """ ||T53fa39e0|| Заповнити дані вкладки "Довільні поля" максимально допустимими значеннями в попапі налаштування обʼєкту """
        
        name_f = "name! from counting words and characters, online editor help you to improve word choice and writing!" # 100 symbols
        value_f = "value! from counting words and characters, online editor help you to improve word choice and writing!" # 100 symbols
        
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click() # Open object settings window
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
        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.del_btn.nth(0).click() # Click the delete button

        expect(custom_fields_page.empty_fields.nth(0)).to_be_enabled() # Check that the first empty name field is enabled
        expect(custom_fields_page.empty_fields.nth(1)).to_be_enabled()
        expect(custom_fields_page.save_btn).to_be_disabled() # Check that the save button is disabled
        expect(custom_fields_page.del_btn).not_to_be_visible() # Check that the delete button is not visible
