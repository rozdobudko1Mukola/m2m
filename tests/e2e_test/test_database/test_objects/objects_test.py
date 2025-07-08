import time

import pytest
from pytest import mark
from playwright.sync_api import Page, expect

from pages.e2e.database.objects import ObjectsPage
from pages.e2e.base_page import BasePage
from pages.e2e.database.on_pause import onPausePage

VEHICLE_DEVICE = {
    "name": "Auto_Test",
    "phone_1": "180455679224",
    "phone_2": "180455679224",
    "model": "Teltonika FMB965",
    "device_type": {
        "VEHICLE": "VEHICLE",
        "FUEL_VEHICLE": "FUEL_VEHICLE",
        "PERSONAL_TRACKER": "PERSONAL_TRACKER",
        "BEACON": "BEACON",
    },
}

expect_text = {
    "VEHICLE": "Транспортний засіб",
    "FUEL_VEHICLE": "Транспортний засіб з контролем пального",
    "PERSONAL_TRACKER": "Персональний трекер",
    "BEACON": "Маяк",
}

stage_expect_deactivate_column = [
    "",
    "№",
    "ОБ'ЄКТИ",
    "НАЗВА",
    "РЕДАГУВАТИ",
]
stage_expect_activate_column = [
    "",
    "№",
    "ОБ'ЄКТИ",
    "НАЗВА",
    "РЕДАГУВАТИ",
    "ТИП ОБ’ЄКТУ",
    "IMEI",
    "SIM 1",
    "SIM 2",
    "ДАТА СТВОРЕННЯ ОБ’ЄКТА",
    "РЕЄСТРАЦІЙНИЙ НОМЕР",
    "ОСТАННЄ ПОВІДОМЛЕННЯ ОБ’ЄКТА",
    "Пауза",
]

expect_deactivate_column = [
    "",
    "№",
    "ОБ'ЄКТИ",
    "ІМ'Я",
    "РЕДАГУВАТИ",
]
expect_activate_column = [
    "",
    "№",
    "ОБ'ЄКТИ",
    "ІМ'Я",
    "РЕДАГУВАТИ",
    "ТИП ОБ’ЄКТУ",
    "ОБЛІКОВИЙ ЗАПИС",
    "МОДЕЛЬ ТРЕКЕРУ",
    "УНІКАЛЬНИЙ ID",
    "SIM 1",
    "SIM 2",
    "ДАТА СТВОРЕННЯ",
    "РЕЄСТРАЦІЙНИЙ НОМЕР",
    "ОСТАННЄ ПОВІДОМЛЕННЯ",
    "КОПІЮВАТИ",
    "Пауза",
    "Видалити",
]


# Objects --------------------------------------------------------------------------------------------

@mark.objects
@mark.unit
@mark.testomatio('@Tttttt382', '@Tttttt383', '@Tttttt384', '@Tttttt385')
@pytest.mark.parametrize(
    "device_type, expected_text",
    [
        (VEHICLE_DEVICE["device_type"]["VEHICLE"], expect_text["VEHICLE"]),
        (VEHICLE_DEVICE["device_type"]["FUEL_VEHICLE"], expect_text["FUEL_VEHICLE"]),
        (VEHICLE_DEVICE["device_type"]["PERSONAL_TRACKER"], expect_text["PERSONAL_TRACKER"]),
        (VEHICLE_DEVICE["device_type"]["BEACON"], expect_text["BEACON"]),
    ],
    ids=["VEHICLE_m2m_382", "FUEL_VEHICLE_m2m_383", "PERSONAL_TRACKER_m2m_384", "BEACON_m2m_385"],
)
@pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
def test_create_new_object_m2m(user_page, test_data, remove_units_by_api, device_type, expected_text):
    objects_page = ObjectsPage(user_page)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {device_type}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE["model"],
        device_type,
    )
    objects_page.popap_btn["ok"].click(force=True)
    user_page.wait_for_timeout(1000)
    if objects_page.popap_btn["ok"].is_visible():
        objects_page.popap_btn["ok"].click()
    objects_page.popap_btn["ok"].wait_for(state="detached", timeout=10000)

    max_retries = 10
    retries = 0
    while not objects_page.unit_table["body_row"].nth(0).is_visible():
        if retries >= max_retries:
            raise AssertionError("Елемент не з'явився після 10 спроб оновлення сторінки")
        user_page.wait_for_load_state("load")
        user_page.goto("/units")
        user_page.wait_for_timeout(1000)
        retries += 1

    expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(expected_text)
    user_page.wait_for_load_state("load")
    user_page.goto("/units")


@mark.objects
@mark.unit
@mark.testomatio('@Ttttt1540')
@pytest.mark.parametrize("user_page", ["FREEBILL"], indirect=True)
def test_create_new_object_when_the_device_limit_is_exhausted_m2m_1540(user_page: Page):
    """||M2M-1540|| Створити новий об'єкт при умові, що ліміт кількості пристроїв вичерпаний"""
    objects_page = ObjectsPage(user_page)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {VEHICLE_DEVICE['device_type']['VEHICLE']}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE["model"],
        VEHICLE_DEVICE["device_type"]["VEHICLE"],
    )
    objects_page.popap_btn["ok"].click()
    expect(objects_page.popap_btn["err_msg"]).to_contain_text("Досягнуто ліміту для нових пристроїв")


@mark.objects
@mark.unit
@mark.testomatio('@Tttttt387')
@pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
def test_cancel_creating_new_object_m2m_387(user_page):
    """||M2M-387|| Відмінити створення нового об'єкта"""
    objects_page = ObjectsPage(user_page)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {VEHICLE_DEVICE['device_type']['VEHICLE']}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE["model"],
        VEHICLE_DEVICE["device_type"]["VEHICLE"],
    )
    objects_page.popap_btn["cancel"].click()
    user_page.wait_for_timeout(1000)
    expect(objects_page.unit_table["body_row"]).not_to_be_visible()


@mark.objects
@mark.unit
@mark.testomatio('@Tttttt388')
@pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
def test_create_new_object_without_filling_in_the_fields_m2m_388(user_page):
    """||M2M-388|| Створити новий об'єкт не заповнивши поля "Ім'я", "Унікальний ID", "Тип" "Модель" """
    objects_page = ObjectsPage(user_page)
    objects_page.add_new_object("", "", "", "", "")
    objects_page.popap_btn["ok"].click()
    base_page = BasePage(user_page)
    for index in [3, 4, 5, 11]:
        expect(base_page.red_fild_color.nth(index)).to_have_css("border-color", base_page.color_of_red)
    expect(base_page.mandatory_fields_msg).to_have_count(4)


@mark.objects
@mark.unit
@mark.testomatio('@Tttttt389')
@pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
def test_interaction_with_inactive_fields_and_sections_m2m_389(user_page):
    """||M2M-389|| Взаємодія з неактивними полями та розділами"""
    objects_page = ObjectsPage(user_page)
    objects_page.head_menu_unit_locators["add_unit"].click()
    for popup_input in ["protocol", "adress_server", "owner", "date_of_create"]:
        expect(objects_page.object_main_popap_inputs[popup_input]).to_be_disabled()
    for index in range(1, 6):
        expect(objects_page.object_popap_tablist["new_object_tabs"].nth(index)).to_be_disabled()


@mark.objects
@mark.unit
@mark.testomatio('@Tttttt394')
@pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
@pytest.mark.parametrize("create_and_remove_units_by_api", [1], indirect=True)
def test_pause_the_object_m2m_394(user_page, test_data, create_and_remove_units_by_api):
    """||M2M-394|| Поставити на паузу об'єкт"""
    objects_page = ObjectsPage(user_page)
    objects_page.unit_table["pause_btn"].click()
    expect(objects_page.popap_btn["popap_title"]).to_contain_text("Підтвердження видалення")
    objects_page.popap_btn["confirm_del"].click(timeout=1000)
    time.sleep(1)
    expect(objects_page.popap_btn["popap_title"]).not_to_be_visible()
    user_page.reload()
    expect(objects_page.unit_table["body_row"]).not_to_be_visible()
    on_pause_page = onPausePage(user_page)
    expect(on_pause_page.ob_tablet_body).to_contain_text(test_data["uniqueId"])


@mark.objects
@mark.unit
@mark.testomatio('@Tttttt395')
@pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
def test_cancel_pause_the_object_m2m_395(user_page, test_data, create_and_remove_units_by_api):
    """||M2M-395|| Скасувати переведення об'єкта на паузу"""
    objects_page = ObjectsPage(user_page)
    objects_page.unit_table["pause_btn"].click()
    expect(objects_page.popap_btn["popap_title"]).to_contain_text("Підтвердження видалення")
    objects_page.popap_btn["cancel_del"].click(timeout=1000)
    time.sleep(1)
    expect(objects_page.popap_btn["popap_title"]).not_to_be_visible()
    user_page.reload()
    expect(objects_page.unit_table["body_row"]).to_contain_text(test_data["uniqueId"])


# Group of objects ----------------------------------------------------------------------------------------

class TestObjectsGroup:

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt396')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_and_remove_units_by_api", [3], indirect=True)
    def test_create_a_new_group_of_objects_m2m_396(
        self, user_page, create_and_remove_units_by_api, delete_device_groups_after_test
    ):
        """||M2M-396|| Створити нову групу обєктів"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.add_new_group("Test_group", 3)
        objects_page.popap_btn["ok"].click()
        user_page.wait_for_selector("#display-tabpanel-1 table")
        expect(objects_page.group_table["body_row"]).to_have_count(1)

    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1564')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_create_a_new_group_of_objects_without_name_m2m_1564(self, user_page):
        """||M2M-1564|| Створити нову групу обєктів не заповнивши обов'язкові поля"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.add_new_group("", 0)
        objects_page.popap_btn["ok"].click()
        base_page = BasePage(user_page)
        expect(base_page.red_fild_color.nth(3)).to_have_css("border-color", base_page.color_of_red)
        expect(base_page.mandatory_fields_msg.nth(0)).to_have_text("Обов'язкове поле")

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt397')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_cancel_creating_a_new_group_of_objects_m2m_397(self, user_page):
        """||M2M-397|| Відмінити створення нової групи об'єктів"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.add_new_group("Test_group", 0)
        objects_page.popap_btn["cancel"].click()
        expect(objects_page.group_table["body_row"]).not_to_be_visible()

    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1542')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_add_objects_to_a_group_of_objects_m2m_1542(
        self, user_page, create_and_remove_units_by_api, create_and_del_device_groups
    ):
        """||M2M-1542|| Додати об'єкти до групи обєктів"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.group_table["btns_in_row"].nth(0).click()
        objects_page.popap_groups["group_checkboxes"].last.check()
        objects_page.popap_btn["ok"].click()
        objects_page.group_table["expand_btn"].click(timeout=500)
        expect(objects_page.group_table["body_row"]).to_have_count(2)

    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1543')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_remove_objects_from_a_group_of_objects_m2m_1543(
        self, user_page, create_and_remove_units_by_api, create_and_del_device_groups
    ):
        """||M2M-1543|| Видалити об'єкти з групи обєктів"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.group_table["btns_in_row"].nth(0).click()
        objects_page.popap_groups["group_checkboxes"].last.check()
        objects_page.popap_btn["ok"].click()
        objects_page.group_table["btns_in_row"].nth(0).click()
        objects_page.popap_groups["group_checkboxes"].last.uncheck()
        objects_page.popap_btn["ok"].click()
        objects_page.group_table["expand_btn"].click(timeout=500)
        expect(objects_page.group_table["body_row"]).to_have_count(1)

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt401')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_and_del_device_groups", [12], indirect=True)
    def test_display_the_next_and_previous_page_of_the_group_list_m2m_401(
        self, user_page, create_and_del_device_groups
    ):
        """||M2M-401|| Відобразити наступну та попередню сторінку зі списку груп."""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        expect(objects_page.check_pagelist("next_page", "groups_total_p")).to_have_text("11-12 із 12")
        user_page.wait_for_timeout(1000)
        expect(objects_page.check_pagelist("previous_page", "groups_total_p")).to_have_text("1-10 із 12")

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt402')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_and_del_device_groups", [25], indirect=True)
    def test_increase_decrease_the_number_of_groups_m2m_402(self, user_page, create_and_del_device_groups):
        """||M2M-402|| Збільшити/зменшити кількість груп, які відображаються на сторінці"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        for count in ["25", "10"]:
            expect(objects_page.increase_decrease_the_number_group(count)).to_have_count(int(count))
            expect(objects_page.group_table["body_row"]).to_have_count(int(count))

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt404')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_delete_a_group_m2m_404(self, user_page):
        """||M2M-404|| Видалити групу"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.add_new_group("Test_group", 0)
        objects_page.popap_btn["ok"].click()
        objects_page.remove_group()
        expect(objects_page.group_table["body_row"]).not_to_be_visible()

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt403')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_and_del_device_groups", [11], indirect=True)
    def test_remove_last_group_in_list_of_groups_M2M_403(self, user_page, create_and_del_device_groups):
        """||M2M-403|| Видалити останню групу в сторінці"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.row_on_page["next_page"].click()
        objects_page.group_table["del_btn_in_row"].click()
        objects_page.popap_btn["confirm_del"].click()
        expect(objects_page.group_table["body_row"]).to_have_count(10)

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt405')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_cancel_deleting_a_group_m2m_405(self, user_page, create_and_del_device_groups):
        """||M2M-405|| Відмінити видалення групи"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.group_table["del_btn_in_row"].click()
        objects_page.popap_btn["cancel_del"].click()
        expect(objects_page.group_table["body_row"]).to_have_count(1)

    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1604')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_dispaly_group_members_in_an_empty_group_m2m_1604(self, user_page, create_and_del_device_groups):
        """||M2M-1604|| Відобразити учасників групи в порожній групі"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.group_table["expand_btn"].click(timeout=500)
        expect(objects_page.group_table["alert_msg"]).to_be_visible()

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt407')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_open_the_object_properties_window_in_the_list_of_group_members_m2m_407(
        self, user_page, create_and_del_device_groups, create_and_remove_units_by_api
    ):
        """||M2M-407|| Відкрити вікно властивості об'єкта в списку учасників групи"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.group_table["btns_in_row"].nth(0).click()
        objects_page.popap_groups["group_checkboxes"].last.check()
        objects_page.popap_btn["ok"].click()
        objects_page.group_table["expand_btn"].click()
        objects_page.group_table["btns_in_row"].nth(2).click()
        expect(objects_page.object_main_popap_inputs["name"]).to_have_value("Test device 1")
        objects_page.popap_btn["cancel"].click()

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt408')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    def test_open_the_group_edit_window_m2m_408(self, user_page, create_and_del_device_groups):
        """||M2M-408|| Відкрити вікно редагування групи об'єктів"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.group_table["btns_in_row"].nth(0).click()
        expect(objects_page.object_main_popap_inputs["name"]).to_have_value("Test Device Group 1")
        objects_page.popap_btn["cancel"].click()

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt398')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_and_del_device_groups", [3], indirect=True)
    def test_search_for_a_group_m2m_398(self, user_page, create_and_del_device_groups):
        """||M2M-398|| Пошук групи з повною валідною назвою"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.head_menu_group_locators["group_search_input"].fill("Test Device Group 1")
        expect(objects_page.group_table["body_row"]).to_have_count(1)

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt399')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_and_del_device_groups", [3], indirect=True)
    def test_search_for_a_group_m2m_399(self, user_page, create_and_del_device_groups):
        """M2M-399 Пошук групи з не повною валідною назвою з не валідною назвою"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.head_menu_group_locators["group_search_input"].fill("Group 1")
        expect(objects_page.group_table["body_row"]).to_have_count(1)

    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt400')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_and_del_device_groups", [3], indirect=True)
    def test_search_for_a_group_m2m_400(self, user_page, create_and_del_device_groups):
        """M2M-400 Пошук групи з не валідною назвою"""
        objects_page = ObjectsPage(user_page)
        objects_page.page_tab_buttons["groups"].click()
        objects_page.head_menu_group_locators["group_search_input"].fill("213qwe123")
        expect(objects_page.group_table["body_row"]).to_have_count(0)

# ... (The rest of the file should be formatted in the same way, following PEP8 and flake8 guidelines)
