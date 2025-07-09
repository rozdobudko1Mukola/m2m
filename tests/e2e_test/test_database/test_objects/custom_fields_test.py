import time

import pytest
from pytest import mark
from playwright.sync_api import APIRequestContext, expect

from pages.api.devices_api import DeviceAPI
from pages.e2e.database.admin_custom_fields import CustomAdminFieldsPage
from pages.e2e.database.objects import ObjectsPage


@pytest.fixture()
def revove_custom_filds(api_context: APIRequestContext, token: str, class_test_data):
    """Видалити кастомні поля"""
    device_api = DeviceAPI(api_context, token)
    device_ids = class_test_data.get("device_ids", [])

    if device_ids:
        response = device_api.update_custom_fields_for_device(
            device_id=device_ids[0], customFields="{}"
        )
        expect(response).to_be_ok()
    yield


class TestCustomFields:
    """Тестування кастомних полів"""

    err_text_msg = "Обов'язкове поле"
    err_color_msg = "rgb(211, 47, 47)"
    err_msg_100_symbols = "Максимум 100 символів"
    form_err_text = "Поле з таким іменем вже існує. Змініть ім'я для поля"

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T56f7967a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_open_custom_fields_tab(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        """||T56f7967a|| Відкрити вкладку "Довільні поля" в попапі налаштування обʼєкту"""

        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()
        expect(objects_page.object_popap_tablist["custom_f"]).to_be_visible()
        expect(custom_fields_page.empty_fields.nth(0)).to_be_enabled()
        expect(custom_fields_page.empty_fields.nth(1)).to_be_enabled()
        expect(custom_fields_page.save_btn).to_be_disabled()

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@Tbd40696c')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_custom_fields_tab(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "1")
        custom_fields_page.fill_field("value", "q")
        custom_fields_page.save_btn.click()

        expect(custom_fields_page.get_field("name", 0)).to_have_value("1")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("q")
        expect(custom_fields_page.get_field("name", 0)).to_be_disabled()
        expect(custom_fields_page.get_field("value", 0)).to_be_enabled()
        expect(custom_fields_page.save_btn).to_be_disabled()
        expect(custom_fields_page.del_btn.nth(0)).to_be_enabled()

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T53fa39e0')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_custom_fields_tab_max(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        name_f = (
            "name! from counting words and characters, online editor help you to improve word choice and writing!"
        )
        value_f = (
            "value! from counting words and characters, online editor help you to improve word choice and writing"
        )

        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", name_f)
        custom_fields_page.fill_field("value", value_f)
        custom_fields_page.save_btn.click()

        expect(custom_fields_page.get_field("name", 0)).to_have_value(name_f)
        expect(custom_fields_page.get_field("value", 0)).to_have_value(value_f)
        expect(custom_fields_page.get_field("name", 0)).to_be_disabled()
        expect(custom_fields_page.get_field("value", 0)).to_be_enabled()
        expect(custom_fields_page.save_btn).to_be_disabled()
        expect(custom_fields_page.del_btn.nth(0)).to_be_enabled()

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T34f0b7cc')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_remove_custom_fields(
        self, user_page, full_unit_create_and_remove_by_api
    ):
        """||@T34f0b7cc|| Видалення рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту"""
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(1).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.del_btn.nth(0).click()

        expect(custom_fields_page.empty_fields.nth(0)).to_be_enabled()
        expect(custom_fields_page.empty_fields.nth(1)).to_be_enabled()
        expect(custom_fields_page.save_btn).to_be_disabled()
        expect(custom_fields_page.del_btn).not_to_be_visible()

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T053fd448')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_only_name_fild(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        """Створити рядок в вкладці "Довільні поля" заповнивши тільки поле "Імʼя" в попапі налаштування обʼєкту"""
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        expect(objects_page.object_popap_tablist["custom_f"]).to_be_focused()
        expect(custom_fields_page.save_btn).to_be_disabled()

        custom_fields_page.fill_field("name", "test_name")

        expect(custom_fields_page.save_btn).to_be_disabled()

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T3a44f6cc')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_only_value_fild(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        expect(objects_page.object_popap_tablist["custom_f"]).to_be_focused()
        expect(custom_fields_page.save_btn).to_be_disabled()

        custom_fields_page.fill_field("value", "test_name")

        expect(custom_fields_page.save_btn).to_be_disabled()

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T30777dcd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_edit_custom_fields(
        self, user_page, full_unit_create_and_remove_by_api
    ):
        """||T30777dcd|| Редагування рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту"""
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(2).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.get_field("value", 0).fill("test")
        custom_fields_page.save_btn.click()

        expect(custom_fields_page.get_field("value", 0)).to_have_value("test")

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T4652de4e')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_edit_custom_fields_empty_value(
        self, user_page, full_unit_create_and_remove_by_api
    ):
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(2).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()
        time.sleep(2)

        objects_page.object_popap_tablist["custom_f"].click()
        custom_fields_page.get_field("value", 0).fill("")
        custom_fields_page.save_btn.click()

        expect(custom_fields_page.error["msg"]).to_be_visible()
        expect(custom_fields_page.error["msg"]).to_have_text(self.err_text_msg)
        expect(custom_fields_page.error["msg"]).to_have_css("color", self.err_color_msg)

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@Tc7eef2e0')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_check_modal_window(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "test_name")
        custom_fields_page.fill_field("value", "test_value")

        objects_page.object_popap_tablist["main"].click()
        expect(custom_fields_page.modal_window["modal_title"]).to_be_visible()

        custom_fields_page.modal_window["save_btn"].click()
        objects_page.object_popap_tablist["custom_f"].click()
        expect(custom_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("test_value")

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@Te9322835')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_check_modal_window_close_popap(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "test_name")
        custom_fields_page.fill_field("value", "test_value")

        objects_page.popap_btn["x_btn"].click()

        expect(custom_fields_page.modal_window["modal_title"]).to_be_visible()
        custom_fields_page.modal_window["save_btn"].click()
        time.sleep(1)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()
        time.sleep(1)

        objects_page.object_popap_tablist["custom_f"].click()

        expect(custom_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("test_value")

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T3a7c1543')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_check_modal_window_using_valid_data(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "test_name")
        custom_fields_page.fill_field("value", "test_value")
        custom_fields_page.save_btn.click()
        expect(custom_fields_page.save_btn).to_be_disabled()

        objects_page.object_popap_tablist["main"].click()

        objects_page.object_popap_tablist["custom_f"].click()
        expect(custom_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("test_value")

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T7cad8ff8')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_custom_fields_tab_invalid_length(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        invalid_name_f = (
            "In the Details overview you can see the average speaking and reading time for your text, while Readin"
        )

        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", invalid_name_f)
        custom_fields_page.fill_field("value", invalid_name_f)
        custom_fields_page.save_btn.click()

        expect(custom_fields_page.error["input_border"].nth(0)).to_have_css(
            "border-color", self.err_color_msg
        )
        expect(custom_fields_page.error["input_border"].nth(1)).to_have_css(
            "border-color", self.err_color_msg
        )
        expect(custom_fields_page.error["msg"].nth(0)).to_have_text(self.err_msg_100_symbols)
        expect(custom_fields_page.error["msg"].nth(1)).to_have_text(self.err_msg_100_symbols)

    @mark.objects
    @mark.custom_fields
    @mark.testomatio('@T30141880')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_add_multiple_custom_fields(
        self, user_page, full_unit_create_and_remove_by_api, revove_custom_filds
    ):
        objects_page = ObjectsPage(user_page)
        custom_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["custom_f"].click()

        custom_fields_page.fill_field("name", "test_name")
        custom_fields_page.fill_field("value", "test_value")
        custom_fields_page.save_btn.click()

        expect(custom_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(custom_fields_page.get_field("value", 0)).to_have_value("test_value")
        expect(custom_fields_page.empty_fields.nth(0)).to_be_enabled()
        expect(custom_fields_page.empty_fields.nth(1)).to_be_enabled()
        expect(custom_fields_page.save_btn).to_be_disabled()
        expect(custom_fields_page.del_btn.nth(0)).to_be_enabled()

        custom_fields_page.fill_field("name", "test_name")
        custom_fields_page.fill_field("value", "test_value1")
        custom_fields_page.save_btn.click()

        expect(custom_fields_page.error["form_err_msg"]).to_be_visible()
        expect(custom_fields_page.error["form_err_msg"]).to_have_text(self.form_err_text)
