import pytest
from playwright.sync_api import Page, expect
from pages.database.objects import ObjectsPage
from pages.base_page import BasePage


VEHICLE_DEVICE = {
    "name": "Auto_Test",
    "phone_1": "180455679224",
    "phone_2": "180455679224",
    "model": "Teltonika FMB965",
    "device_type": {
        "VEHICLE": "VEHICLE",
        "FUEL_VEHICLE": "FUEL_VEHICLE",
        "PERSONAL_TRACKER": "PERSONAL_TRACKER",
        "BEACON": "BEACON"
    }
}

expect_text = {
    "VEHICLE": "Транспортний засіб",
    "FUEL_VEHICLE": "Транспортний засіб з контролем пального",
    "PERSONAL_TRACKER": "Персональний трекер",
    "BEACON": "Маяк"
}

expect_deactivate_column = ['', '№', "ОБ'ЄКТИ", 'НАЗВА', 'РЕДАГУВАТИ']
expect_activate_column = ['', '№', "ОБ'ЄКТИ", 'НАЗВА', 'РЕДАГУВАТИ', 'ТИП ОБ’ЄКТУ', 'IMEI', 'SIM 1', 'SIM 2', 'ДАТА СТВОРЕННЯ ОБ’ЄКТА', 'РЕЄСТРАЦІЙНИЙ НОМЕР', 'ОСТАННЄ ПОВІДОМЛЕННЯ ОБ’ЄКТА', 'Пауза']


@pytest.mark.skip("This test is not implemented")
# M2M-337 Пошук об'єкта за Ім'ям з повною валідною назвою
def test_search_object_by_name_m2m_337(auth_new_test_user: Page):
    """||M2M-337|| Пошук об'єкта за Ім'ям з повною валідною назвою"""
    pass


@pytest.mark.skip("This test is not implemented")
# M2M-378 Пошук об'єкта за Ім'ям з не повною валідною назвою
def test_search_object_by_name_m2m_378(auth_new_test_user: Page):
    """||M2M-378|| Пошук об'єкта за Ім'ям з не повною валідною назвою"""
    pass


@pytest.mark.skip("This test is not implemented")
# M2M-339 Пошук об'єкта за Ім'ям з не валідною назвою
def test_search_object_by_name_m2m_339(auth_new_test_user: Page):
    """||M2M-339|| Пошук об'єкта за Ім'ям з не валідною назвою"""
    pass


# M2M-380 Прибрати/додати додаткові колонки на панелі відображення об'єктів
def test_remove_additional_columns_m2m_380(auth_new_test_user: Page):
    """ ||M2M-380|| Прибрати/додати додаткові колонки на панелі відображення об'єктів """
    
    objects_page = ObjectsPage(auth_new_test_user)
    # Preconditions add object
    objects_page.precondition_add_multiple_objects(1,
    f'{VEHICLE_DEVICE["name"]} {VEHICLE_DEVICE["device_type"]["VEHICLE"]}',
    VEHICLE_DEVICE["phone_1"],
    VEHICLE_DEVICE["phone_2"],
    VEHICLE_DEVICE['model'],
    VEHICLE_DEVICE['device_type']['VEHICLE']
    )
    objects_page.head_menu_buttons["settings"].click()

    # Disable all additional columns
    objects_page.edit_object_table()
    assert objects_page.ob_tablet_head.all_inner_texts() == expect_deactivate_column

    # Return the columns to their original state
    objects_page.edit_object_table()
    assert objects_page.ob_tablet_head.all_inner_texts() == expect_activate_column

    # Delete all objects on pause after test
    auth_new_test_user.keyboard.press("Escape")
    objects_page.pause_all_object()


# M2M-382 Створити новий об'єкт типу "Транспортний засіб"
def test_create_new_object_VEHICLE_m2m_382(auth_new_test_user: Page, device_type=VEHICLE_DEVICE["device_type"]["VEHICLE"], expected_text=expect_text["VEHICLE"]):
    """ ||M2M-382|| Створити новий об'єкт типу Транспортний засіб """

    objects_page = ObjectsPage(auth_new_test_user)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {device_type}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type'][device_type]
    )
    objects_page.popap_btn["ok"].click()

    # Check if the object was created
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)

    # Delete all objects on pause after test
    objects_page.pause_all_object()


# M2M-383 Створити новий об'єкт типу "Транспортний засіб з контролем пального"
def test_create_new_object_FUEL_VEHICLE_m2m_383(auth_new_test_user: Page, device_type=VEHICLE_DEVICE["device_type"]["FUEL_VEHICLE"], expected_text=expect_text["FUEL_VEHICLE"]):
    """ ||M2M-383|| Створити новий об'єкт типу Транспортний засіб з контролем пального """

    objects_page = ObjectsPage(auth_new_test_user)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {device_type}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type'][device_type]
    )
    objects_page.popap_btn["ok"].click()
    # Check if the object was created
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)

    # Delete all objects on pause after test
    objects_page.pause_all_object()


# M2M-384 Створити новий об'єкт типу "Персональний трекер"
def test_create_new_object_PERSONAL_TRACKER_m2m_384(auth_new_test_user: Page, device_type=VEHICLE_DEVICE["device_type"]["PERSONAL_TRACKER"], expected_text=expect_text["PERSONAL_TRACKER"]):
    """ ||M2M-384|| Створити новий об'єкт типу Персональний трекер """

    objects_page = ObjectsPage(auth_new_test_user)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {device_type}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type'][device_type]
    )
    objects_page.popap_btn["ok"].click()

    # Check if the object was created
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)

    # Delete all objects on pause after test
    objects_page.pause_all_object()


# M2M-385 Створити новий об'єкт типу "Маяк"
def test_create_new_object_BEACON_m2m_385(auth_new_test_user: Page, device_type=VEHICLE_DEVICE["device_type"]["BEACON"], expected_text=expect_text["BEACON"]):
    """ ||M2M-385|| Створити новий об'єкт типу Маяк """

    objects_page = ObjectsPage(auth_new_test_user)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {device_type}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type'][device_type]
    )
    objects_page.popap_btn["ok"].click()

    # Check if the object was created
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)

    # Delete all objects on pause after test
    objects_page.pause_all_object()


# M2M-1540 Створити новий об'єкт при умові, що ліміт кількості пристроїв вичерпаний
def test_create_new_object_when_the_device_limit_is_exhausted_m2m_1540(login_free_paln_user: Page):
    """ ||M2M-1540|| Створити новий об'єкт при умові, що ліміт кількості пристроїв вичерпаний """

    objects_page = ObjectsPage(login_free_paln_user)

    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {VEHICLE_DEVICE['device_type']['VEHICLE']}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type']['VEHICLE']
    )
    objects_page.popap_btn["ok"].click()

    # Check if the error message is displayed
    expect(objects_page.error_msg).to_contain_text("Досягнуто ліміту для нових пристроїв")


# M2M-387 Відмінити створення нового об'єкта
def test_cancel_creating_new_object_m2m_387(auth_new_test_user: Page):
    """ ||M2M-387|| Відмінити створення нового об'єкта """
    objects_page = ObjectsPage(auth_new_test_user)

    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {VEHICLE_DEVICE['device_type']['VEHICLE']}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type']['VEHICLE']
    )
    objects_page.popap_btn["cancel"].click()

    # Check if the object was not created
    auth_new_test_user.wait_for_timeout(1000)
    expect(objects_page.ob_tablet_body).not_to_be_visible()

# M2M-388 Створити новий об'єкт не заповнивши поля "Ім'я", "Унікальний ID", "Тип" "Модель"
def test_create_new_object_without_filling_in_the_fields_m2m_388(auth_new_test_user: Page):
    """ ||M2M-388|| Створити новий об'єкт не заповнивши поля "Ім'я", "Унікальний ID", "Тип" "Модель" """

    objects_page = ObjectsPage(auth_new_test_user)

    objects_page.add_new_object("", "", "", "", "")
    objects_page.popap_btn["ok"].click()

    # Check if input color is red
    base_page = BasePage(auth_new_test_user)
    for index in [2, 3, 4, 10]:
        expect(base_page.red_fild_color.nth(index)).to_have_css("border-color", base_page.color_of_red)
    # Check if the error message is displayed
    expect(base_page.mandatory_fields_msg).to_have_count(4)


# M2M-389 Взаємодія з неактивними полями та розділами
def test_interaction_with_inactive_fields_and_sections_m2m_389(auth_new_test_user: Page):
    """ ||M2M-389|| Взаємодія з неактивними полями та розділами """

    objects_page = ObjectsPage(auth_new_test_user)
    objects_page.head_menu_buttons["add"].click()

    # Check if the fields are inactive
    for popup_input in ["protocol", "adress_server", "owner", "date_of_create"]:
        expect(objects_page.object_main_popap_inputs[popup_input]).to_be_disabled()

    # Check if the tabs are inactive
    for tab_name in ["access", "sensors", "custom_f", "Char", "commands"]:
        expect(objects_page.object_popap_tablist[tab_name]).to_be_disabled()
