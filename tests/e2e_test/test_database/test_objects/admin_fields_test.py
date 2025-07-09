import pytest
from pytest import mark
from playwright.sync_api import expect
from pages.e2e.database.objects import ObjectsPage
from pages.e2e.database.admin_custom_fields import CustomAdminFieldsPage
from playwright.sync_api import APIRequestContext
from pages.api.devices_api import DeviceAPI
import time


@pytest.fixture()
def revove_admin_filds(api_context: APIRequestContext, token: str, class_test_data):
    """Видалити кастомні поля"""

    # Clean up code
    device_api = DeviceAPI(api_context, token)
    device_ids = class_test_data.get("device_ids", [])
    if device_ids:
        # Clear admin fields for the first device
        response = device_api.update_admin_fields_for_device(device_ids[0], adminFields="{}")
        expect(response).to_be_ok()

    yield


class TestAdminFields:
    """Тестування кастомних полів"""

    err_text_msg = "Обов'язкове поле"  # Error message for required field
    err_color_msg = "rgb(211, 47, 47)"  # Red color for error message
    err_msg_100_symbols = "Максимум 100 символів"  # Error message for max length of 100 symbols
    form_err_text = "Поле з таким іменем вже існує. Змініть ім'я для поля"  # Error message for duplicate field name

    # Відкрити вкладку "Довільні поля" в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_open_admin_fields_tab(self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds):
        """ ||T56f7967a|| Відкрити вкладку "Довільні поля" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["admin_f"].click()

        expect(objects_page.object_popap_tablist["admin_f"]).to_be_visible()  # Check the tab is opened
        expect(admin_fields_page.empty_fields.nth(0)).to_be_enabled()
        expect(admin_fields_page.empty_fields.nth(1)).to_be_enabled()
        expect(admin_fields_page.save_btn).to_be_disabled()  # Check the save button is disabled

    # Заповнити дані вкладки "Довільні поля" мінімально допустимими значеннями в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@Tbd40696c')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_admin_fields_tab(self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds):
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()

        objects_page.object_popap_tablist["admin_f"].click()

        admin_fields_page.fill_field("name", "1")  # Fill the first empty name field
        admin_fields_page.fill_field("value", "q")  # Fill the first empty value field
        admin_fields_page.save_btn.click()  # Click the save button

        expect(admin_fields_page.get_field("name", 0)).to_have_value("1")
        expect(admin_fields_page.get_field("value", 0)).to_have_value("q")
        expect(admin_fields_page.get_field("name", 0)).to_be_disabled()  # Check the first name field is disabled
        expect(admin_fields_page.get_field("value", 0)).to_be_enabled()  # Check the first value field is enabled
        expect(admin_fields_page.save_btn).to_be_disabled()  # Check the save button is disabled
        expect(admin_fields_page.del_btn.nth(0)).to_be_enabled()  # Check the delete button is enabled

    # Заповнити дані вкладки "Довільні поля" максимально допустимими значеннями в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T53fa39e0')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_admin_fields_tab_max(self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds):

        # 100 symbols
        name_f = "name! from counting words and characters, online editor help you to improve word choice and writing!"
        value_f = "value! from counting words and characters, online editor help you to improve word choice and writing"

        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        admin_fields_page.fill_field("name", name_f)  # Fill the first empty name field
        admin_fields_page.fill_field("value", value_f)  # Fill the first empty value field
        admin_fields_page.save_btn.click()  # Click the save button

        expect(admin_fields_page.get_field("name", 0)).to_have_value(name_f)
        expect(admin_fields_page.get_field("value", 0)).to_have_value(value_f)
        expect(admin_fields_page.get_field("name", 0)).to_be_disabled()  # Check the first name field is disabled
        expect(admin_fields_page.get_field("value", 0)).to_be_enabled()  # Check the first value field is enabled
        expect(admin_fields_page.save_btn).to_be_disabled()  # Check the save button is disabled
        expect(admin_fields_page.del_btn.nth(0)).to_be_enabled()  # Check the delete button is enabled

    # Видалення рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T34f0b7cc')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_remove_admin_fields(self, user_page, full_unit_create_and_remove_by_api):
        """ ||@T34f0b7cc|| Видалення рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(1).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        admin_fields_page.del_btn.nth(0).click()  # Click the delete button

        expect(admin_fields_page.empty_fields.nth(0)).to_be_enabled()  # Check the first empty name field is enabled
        expect(admin_fields_page.empty_fields.nth(1)).to_be_enabled()
        expect(admin_fields_page.save_btn).to_be_disabled()  # Check the save button is disabled
        expect(admin_fields_page.del_btn).not_to_be_visible()  # Check the delete button is not visible

    # Створити рядок в вкладці "Довільні поля" заповнивши тільки поле "Імʼя" в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T053fd448')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_only_name_fild(self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds):
        """ Створити рядок в вкладці "Довільні поля" заповнивши тільки поле "Імʼя" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        expect(objects_page.object_popap_tablist["admin_f"]).to_be_focused()  # Check the tab is opened
        expect(admin_fields_page.save_btn).to_be_disabled()  # Check the save button is disabled

        admin_fields_page.fill_field("name", "test_name")  # Fill the first empty name field

        expect(admin_fields_page.save_btn).to_be_disabled()

    # Створити рядок в вкладці "Довільні поля" заповнивши тільки поле "Значення" в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T3a44f6cc')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_only_value_fild(self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds):
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        expect(objects_page.object_popap_tablist["admin_f"]).to_be_focused()  # Check the tab is opened
        expect(admin_fields_page.save_btn).to_be_disabled()  # Check the save button is disabled

        admin_fields_page.fill_field("value", "test_name")  # Fill the first empty name field

        expect(admin_fields_page.save_btn).to_be_disabled()

    # Редагування рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T30777dcd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_edit_admin_fields(self, user_page, full_unit_create_and_remove_by_api):
        """ ||T30777dcd|| Редагування рядку з даними вкладки "Довільні поля" в попапі налаштування обʼєкту """
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(2).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        admin_fields_page.get_field("value", 0).fill("test")  # Fill the first empty value field with new value
        admin_fields_page.save_btn.click()  # Click the save button

        expect(admin_fields_page.get_field("value", 0)).to_have_value("test")

    # Редагування рядку з даними вкладки "Довільні поля" вказавши пусті поля "Значення" в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T4652de4e')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_edit_admin_fields_empty_value(self, user_page, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(2).click()

        # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty
        time.sleep(2)  # Wait for the modal to open

        objects_page.object_popap_tablist["admin_f"].click()
        admin_fields_page.get_field("value", 0).fill("")
        # Fill the first empty value field with new value
        admin_fields_page.save_btn.click()

        expect(admin_fields_page.error["msg"]).to_be_visible()
        expect(admin_fields_page.error["msg"]).to_have_text(self.err_text_msg)
        expect(admin_fields_page.error["msg"]).to_have_css("color", self.err_color_msg)

    # Перевірка появи модального вікна при переході на іншу вкладку якшо є не збережені дані у вкладці "Довільні поля"
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@Tc7eef2e0')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_check_modal_window(self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds):
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        admin_fields_page.fill_field("name", "test_name")   # Fill the first empty name field
        admin_fields_page.fill_field("value", "test_value")   # Fill the first empty value field

        objects_page.object_popap_tablist["main"].click()
        expect(admin_fields_page.modal_window["modal_title"]).to_be_visible()  # Check the modal window is visible

        admin_fields_page.modal_window["save_btn"].click()
        objects_page.object_popap_tablist["admin_f"].click()
        expect(admin_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(admin_fields_page.get_field("value", 0)).to_have_value("test_value")

    # Перевірка появи вікна при закриті попапу налаштування обʼєкту якшо є не збережені дані у вкладці "Довільні поля"
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@Te9322835')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_check_modal_window_close_popap(self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds):
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        # Fill the first empty name field
        admin_fields_page.fill_field("name", "test_name")
        admin_fields_page.fill_field("value", "test_value")

        objects_page.popap_btn["x_btn"].click()  # Close the pop-up window

        expect(admin_fields_page.modal_window["modal_title"]).to_be_visible()  # Check the modal window is visible
        admin_fields_page.modal_window["save_btn"].click()
        time.sleep(1)  # Wait for the modal to close

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty
        time.sleep(1)  # Wait for the modal to close

        objects_page.object_popap_tablist["admin_f"].click()

        expect(admin_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(admin_fields_page.get_field("value", 0)).to_have_value("test_value")

    # Перевірка появи модального вікна при переході на іншу вкладку якшо дані збережені у вкладці "Довільні поля"
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T3a7c1543')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_check_modal_window_using_valid_data(
        self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds
    ):
        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        admin_fields_page.fill_field("name", "test_name")  # Fill the first empty name field
        admin_fields_page.fill_field("value", "test_value")  # Fill the first empty value field
        admin_fields_page.save_btn.click()  # Click the save button
        expect(admin_fields_page.save_btn).to_be_disabled()  # Check the save button is disabled

        objects_page.object_popap_tablist["main"].click()

        objects_page.object_popap_tablist["admin_f"].click()
        expect(admin_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(admin_fields_page.get_field("value", 0)).to_have_value("test_value")

    # Заповнити дані вкладки "Довільні поля" вказавши НЕ валідну довжину симовлів в поя вводу в попапі налаштування
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T7cad8ff8')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_fill_admin_fields_tab_invalid_length(
        self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds
    ):

        # 101 symbols, invalid length
        invalid_name_f = (
            "In the Details overview you can see the average speaking and reading time for your text, "
            "while Readin"
        )

        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        admin_fields_page.fill_field("name", invalid_name_f)  # Fill the first empty name field
        admin_fields_page.fill_field("value", invalid_name_f)  # Fill the first empty value field
        admin_fields_page.save_btn.click()  # Click the save button

        # Поля вводу "Імʼя" та "Значення" підсвічуються червоним кольором
        # Check the input border color is red in name field
        expect(admin_fields_page.error["input_border"].nth(0)).to_have_css("border-color", self.err_color_msg)
        expect(admin_fields_page.error["input_border"].nth(1)).to_have_css("border-color", self.err_color_msg)

        # Під полями вводу відображаються повідомлення про помилку "Максимум 100 символів"
        # Check the error message is displayed under the name field
        expect(admin_fields_page.error["msg"].nth(0)).to_have_text(self.err_msg_100_symbols)
        expect(admin_fields_page.error["msg"].nth(1)).to_have_text(self.err_msg_100_symbols)

    # Додавання декількох рядків з однаковими даними у вкладці "Довільні поля" в попапі налаштування обʼєкту
    @mark.objects
    @mark.admin_fields
    @mark.testomatio('@T30141880')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_add_multiple_admin_fields(self, user_page, full_unit_create_and_remove_by_api, revove_admin_filds):

        objects_page = ObjectsPage(user_page)
        admin_fields_page = CustomAdminFieldsPage(user_page)

        objects_page.unit_table["edit_btn"].nth(0).click()  # Open object settings window
        expect(objects_page.object_main_popap_inputs["model"]).not_to_be_empty()  # Check the model field is not empty

        objects_page.object_popap_tablist["admin_f"].click()

        admin_fields_page.fill_field("name", "test_name")  # Fill the first empty name field
        admin_fields_page.fill_field("value", "test_value")  # Fill the first empty value field
        admin_fields_page.save_btn.click()  # Click the save button

        # Check first name field is filled
        expect(admin_fields_page.get_field("name", 0)).to_have_value("test_name")
        expect(admin_fields_page.get_field("value", 0)).to_have_value("test_value")
        # Check first empty name field is enabled
        expect(admin_fields_page.empty_fields.nth(0)).to_be_enabled()
        expect(admin_fields_page.empty_fields.nth(1)).to_be_enabled()
        # Check save button is disabled
        expect(admin_fields_page.save_btn).to_be_disabled()
        expect(admin_fields_page.del_btn.nth(0)).to_be_enabled()

        # Add another row with the same data
        admin_fields_page.fill_field("name", "test_name")  # Fill the second empty name field
        admin_fields_page.fill_field("value", "test_value1")  # Fill the second empty value field
        admin_fields_page.save_btn.click()  # Click the save button

        expect(admin_fields_page.error["form_err_msg"]).to_be_visible()  # Check the error message is displayed
        expect(admin_fields_page.error["form_err_msg"]).to_have_text(self.form_err_text)
