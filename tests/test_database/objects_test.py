import os
import pytest
from pytest import mark
from playwright.sync_api import Page, expect
from pages.database.objects import ObjectsPage
from pages.base_page import BasePage
from pages.database.on_pause import onPausePage


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

stage_expect_deactivate_column = ['', '№', "ОБ'ЄКТИ", 'НАЗВА', 'РЕДАГУВАТИ']
stage_expect_activate_column = ['', '№', "ОБ'ЄКТИ", 'НАЗВА', 'РЕДАГУВАТИ', 'ТИП ОБ’ЄКТУ', 'IMEI', 'SIM 1', 'SIM 2', 'ДАТА СТВОРЕННЯ ОБ’ЄКТА', 'РЕЄСТРАЦІЙНИЙ НОМЕР', 'ОСТАННЄ ПОВІДОМЛЕННЯ ОБ’ЄКТА', 'Пауза']

expect_deactivate_column = ['', '№', "ОБ'ЄКТИ", "ІМ'Я", 'РЕДАГУВАТИ']
expect_activate_column = ['', '№', "ОБ'ЄКТИ", "ІМ'Я", 'РЕДАГУВАТИ', 'ТИП ОБ’ЄКТУ', 'ОБЛІКОВИЙ ЗАПИС', 'МОДЕЛЬ ТРЕКЕРУ', 'УНІКАЛЬНИЙ ID', 'SIM 1', 'SIM 2', 'ДАТА СТВОРЕННЯ', 'РЕЄСТРАЦІЙНИЙ НОМЕР', 'ОСТАННЄ ПОВІДОМЛЕННЯ', 'Пауза', 'Видалити']

# Objects-------------------------------------------------------------------------------------------------------------------------------------


# M2M-380 Прибрати/додати додаткові колонки на панелі відображення об'єктів
@mark.testomatio('@Tttttt380')
def test_remove_additional_columns_m2m_380(freebill_user: Page):
    """ ||M2M-380|| Прибрати/додати додаткові колонки на панелі відображення об'єктів """
    
    objects_page = ObjectsPage(freebill_user)

    # Disable all additional columns
    objects_page.head_menu_unit_locators["settings"].wait_for(state="attached")
    objects_page.head_menu_unit_locators["settings"].click()
    objects_page.edit_unit_column_table()
    assert objects_page.unit_table["head_column"].all_inner_texts() == expect_deactivate_column

    # Return the columns to their original state
    objects_page.edit_unit_column_table()
    assert objects_page.unit_table["head_column"].all_inner_texts() == expect_activate_column


# M2M-382, M2M-383, M2M-384, M2M-385 Створити 4 нових об'єкти типу "Транспортний засіб", "Транспортний засіб з контролем пального", "Персональний трекер", "Маяк"
@mark.testomatio('@Tttttt382', '@Tttttt383', '@Tttttt384', '@Tttttt385')
@pytest.mark.parametrize("device_type, expected_text",[ 
(VEHICLE_DEVICE["device_type"]["VEHICLE"], expect_text["VEHICLE"]), 
(VEHICLE_DEVICE["device_type"]["FUEL_VEHICLE"], expect_text["FUEL_VEHICLE"]), 
(VEHICLE_DEVICE["device_type"]["PERSONAL_TRACKER"], expect_text["PERSONAL_TRACKER"]),
(VEHICLE_DEVICE["device_type"]["BEACON"], expect_text["BEACON"])], ids=["VEHICLE_m2m_382", "FUEL_VEHICLE_m2m_383", "PERSONAL_TRACKER_m2m_384", "BEACON_m2m_385"]) 
def test_create_new_object_m2m(selfreg_user: Page, just_remove_units, device_type, expected_text):

    objects_page = ObjectsPage(selfreg_user)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {device_type}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type'][device_type]
    )
    objects_page.popap_btn["ok"].click()

    # Check if the object was created
    expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(expected_text)


# M2M-1540 Створити новий об'єкт при умові, що ліміт кількості пристроїв вичерпаний
@mark.testomatio('@Ttttt1540')
def test_create_new_object_when_the_device_limit_is_exhausted_m2m_1540(freebill_user: Page):
    """ ||M2M-1540|| Створити новий об'єкт при умові, що ліміт кількості пристроїв вичерпаний """

    objects_page = ObjectsPage(freebill_user)

    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {VEHICLE_DEVICE['device_type']['VEHICLE']}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type']['VEHICLE']
    )
    objects_page.popap_btn["ok"].click()

    # Check if the error message is displayed
    expect(objects_page.popap_btn["err_msg"]).to_contain_text("Досягнуто ліміту для нових пристроїв")


# M2M-387 Відмінити створення нового об'єкта
@mark.testomatio('@Tttttt387')
def test_cancel_creating_new_object_m2m_387(selfreg_user: Page):
    """ ||M2M-387|| Відмінити створення нового об'єкта """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {VEHICLE_DEVICE['device_type']['VEHICLE']}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type']['VEHICLE']
    )
    objects_page.popap_btn["cancel"].click()

    # Check if the object was not created
    selfreg_user.wait_for_timeout(1000)
    expect(objects_page.unit_table["body_row"]).not_to_be_visible()


# M2M-388 Створити новий об'єкт не заповнивши поля "Ім'я", "Унікальний ID", "Тип" "Модель"
@mark.testomatio('@Tttttt388')
def test_create_new_object_without_filling_in_the_fields_m2m_388(selfreg_user: Page):
    """ ||M2M-388|| Створити новий об'єкт не заповнивши поля "Ім'я", "Унікальний ID", "Тип" "Модель" """

    objects_page = ObjectsPage(selfreg_user)

    objects_page.add_new_object("", "", "", "", "")
    objects_page.popap_btn["ok"].click()

    # Check if input color is red
    base_page = BasePage(selfreg_user)
    for index in [3, 4, 5, 11]:
        expect(base_page.red_fild_color.nth(index)).to_have_css("border-color", base_page.color_of_red)
    # Check if the error message is displayed
    expect(base_page.mandatory_fields_msg).to_have_count(4)


# M2M-389 Взаємодія з неактивними полями та розділами
@mark.testomatio('@Tttttt389')
def test_interaction_with_inactive_fields_and_sections_m2m_389(selfreg_user: Page):
    """ ||M2M-389|| Взаємодія з неактивними полями та розділами """

    objects_page = ObjectsPage(selfreg_user)
    objects_page.head_menu_unit_locators["add_unit"].click()

    # Check if the fields are inactive
    for popup_input in ["protocol", "adress_server", "owner", "date_of_create"]:
        expect(objects_page.object_main_popap_inputs[popup_input]).to_be_disabled()

    # Check if the tabs are inactive
    for index in range(1, 6):
        expect(objects_page.object_popap_tablist["new_object_tabs"].nth(index)).to_be_disabled()


# M2M-390 Відобразити наступну та попередню сторінку зі списку об'єктів.
@mark.testomatio('@Tttttt390')
def test_display_the_next_and_previous_page_m2m_390(admin_user: Page):
    """ ||M2M-390|| Відобразити наступну та попередню сторінку зі списку об'єктів. """
    objects_page = ObjectsPage(admin_user)
    
    expect(objects_page.check_pagelist("next_page", "unit_total_p")).to_contain_text("101-200")
    admin_user.wait_for_timeout(1000)
    expect(objects_page.check_pagelist("previous_page", "unit_total_p")).to_contain_text("1-100")


# M2M-391 Збільшити/зменшити кількість об'єктів, які відображаються на сторінці
@mark.testomatio('@Tttttt391')
def test_increase_decrease_the_number_of_objects_m2m_391(admin_user: Page):
    """ ||M2M-391|| Збільшити/зменшити кількість об'єктів, які відображаються на сторінці """

    objects_page = ObjectsPage(admin_user)
    for count in ["10", "25", "50", "100"]:
        expect(objects_page.increase_decrease_the_number(count)).to_have_count(int(count))


# M2M-392 Вибрати всі/один об'єкт(и) на панелі
@mark.testomatio('@Tttttt392')
def test_select_all_one_object_on_the_panel_m2m_392(admin_user: Page):
    """ ||M2M-392|| Вибрати всі/один об'єкт(и) на панелі """

    objects_page = ObjectsPage(admin_user)

    # Select all objects
    objects_page.unit_table["head_column"].filter(has=admin_user.locator("input")).click()

    for index in range(1, objects_page.unit_table["body_row"].count() + 1):
        expect(admin_user.locator(f"//div[@id='display-tabpanel-0']//tbody/tr[{index}]/td[1]//input")).to_be_checked()
    
    objects_page.unit_table["head_column"].nth(0).click() # Deselect all objects
    admin_user.wait_for_timeout(1000)
    # select one object
    admin_user.locator("//div[@id='display-tabpanel-0']//tbody/tr[2]/td[1]//input").click()
    expect(admin_user.locator("//div[@id='display-tabpanel-0']//tbody/tr[2]/td[1]//input")).to_be_checked()


# M2M-393 Відкрити вікно налаштування об'єкта
@mark.testomatio('@Tttttt393')
def test_open_object_settings_window_m2m_393(freebill_user: Page):
    """ ||M2M-393|| Відкрити вікно налаштування об'єкта """

    objects_page = ObjectsPage(freebill_user)
    objects_page.unit_table["btns_in_row"].nth(0).click() # Open object settings window
    for tab in ["main", "access", "sensors", "custom_f", "admin_f", "char", "commands", "drive_detection"]:
        objects_page.object_popap_tablist[tab].click()
        expect(objects_page.object_popap_tabpanel[tab]).not_to_be_hidden()


# M2M-394 Поставити на паузу об'єкт
@mark.testomatio('@Tttttt394')
def test_pause_the_object_m2m_394(selfreg_user: Page, just_remove_units, move_unnit_to_trash):
    """ ||M2M-394|| Поставити на паузу об'єкт """

    objects_page = ObjectsPage(selfreg_user)

    # Preconditions add object
    objects_page.precondition_add_multiple_objects(1,
    f'PAUSE {VEHICLE_DEVICE["name"]} {VEHICLE_DEVICE["device_type"]["VEHICLE"]}',
    VEHICLE_DEVICE["phone_1"],
    VEHICLE_DEVICE["phone_2"],
    VEHICLE_DEVICE['model'],
    VEHICLE_DEVICE['device_type']['VEHICLE']
    )

    objects_page.pause_all_object()
    selfreg_user.goto("/on-pause")
    expect(selfreg_user.locator("table tbody tr").nth(0)).to_contain_text('PAUSE')


# M2M-395 Скасувати переведення об'єкта на паузу
@mark.testomatio('@Tttttt395')
def test_cancel_pause_the_object_m2m_395(selfreg_user: Page, create_and_remove_one_units):
    """ ||M2M-395|| Скасувати переведення об'єкта на паузу """

    objects_page = ObjectsPage(selfreg_user)
    selfreg_user.reload()
    objects_page.unit_table["head_column"].nth(0).click(timeout=1000)
    objects_page.unit_table["head_column"].nth(14).click(timeout=1000)
    objects_page.popap_btn["cancel_del"].click()
    selfreg_user.wait_for_timeout(1000)

    # Check if the object was not paused
    selfreg_user.goto("/on-pause")
    expect(selfreg_user.locator("table tbody tr").nth(0)).not_to_be_visible()
    selfreg_user.goto("/units")


# Group of objects----------------------------------------------------------------------------------------------------------------------------

# M2M-396 Створити нову групу обєктів
@mark.testomatio('@Tttttt396')
def test_create_a_new_group_of_objects_m2m_396(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-396|| Створити нову групу обєктів """
    objects_page = ObjectsPage(freebill_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["expand_btn"].click(timeout=1000)
    expect(objects_page.group_table["body_row"]).to_have_count(4)


# M2M-1564 Створити нову групу обєктів не заповнивши обов'язкові поля
@mark.testomatio('@Ttttt1564')
def test_create_a_new_group_of_objects_without_name_m2m_1564(freebill_user: Page):
    """ ||M2M-1564|| Створити нову групу обєктів не заповнивши обов'язкові поля """
    objects_page = ObjectsPage(freebill_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("", 3)
    objects_page.popap_btn["ok"].click()

    base_page = BasePage(freebill_user)
    expect(base_page.red_fild_color.nth(3)).to_have_css("border-color", base_page.color_of_red)
    expect(base_page.mandatory_fields_msg.nth(0)).to_have_text("Обов'язкове поле")


# M2M-397 Відмінити створення нової групи об'єктів
@mark.testomatio('@Tttttt397')
def test_cancel_creating_a_new_group_of_objects_m2m_397(freebill_user: Page):
    """ ||M2M-397|| Відмінити створення нової групи об'єктів """
    objects_page = ObjectsPage(freebill_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 3)
    objects_page.popap_btn["cancel"].click()
    expect(objects_page.group_table["body_row"]).not_to_be_visible()


# M2M-1542 Додати об'єкти до групи обєктів
@mark.testomatio('@Ttttt1542')
def test_add_objects_to_a_group_of_objects_m2m_1542(freebill_user: Page, just_remove_groups):
    """ ||M2M-1542|| Додати об'єкти до групи обєктів """
    objects_page = ObjectsPage(freebill_user)

    # Create group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 2)
    objects_page.popap_btn["ok"].click()

    # Add objects to group
    objects_page.group_table["btns_in_row"].nth(0).click()
    objects_page.popap_btn["group_checkboxes"].last.check()
    objects_page.popap_btn["ok"].click()

    # Check if objects were added to the group
    objects_page.group_table["expand_btn"].click(timeout=500)
    expect(objects_page.group_table["body_row"]).to_have_count(4)


# M2M-1543 Видалити об'єкти з групи обєктів
@mark.testomatio('@Ttttt1543')
def test_remove_objects_from_a_group_of_objects_m2m_1543(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-1543|| Видалити об'єкти з групи обєктів """
    objects_page = ObjectsPage(freebill_user)

    # Remove objects from group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["btns_in_row"].nth(0).click()
    objects_page.popap_btn["group_checkboxes"].nth(3).click()
    objects_page.popap_btn["ok"].click()

    # Check if objects were added to the group
    objects_page.group_table["expand_btn"].click(timeout=500)
    expect(objects_page.group_table["body_row"]).to_have_count(3)


# M2M-401 Відобразити наступну та попередню сторінку зі списку груп.
@mark.testomatio('@Tttttt401')
def test_display_the_next_and_previous_page_of_the_group_list_m2m_401(freebill_user: Page, create_and_remove_12_group):
    """ ||M2M-401|| Відобразити наступну та попередню сторінку зі списку груп. """
    objects_page = ObjectsPage(freebill_user)   

    objects_page.page_tab_buttons["groups"].click()
    expect(objects_page.check_pagelist("next_page", "groups_total_p")).to_have_text("11-12 із 12")
    expect(objects_page.check_pagelist("previous_page", "groups_total_p")).to_have_text("1-10 із 12")


# M2M-402 Збільшити/зменшити кількість груп, які відображаються на сторінці
@mark.testomatio('@Tttttt402')
def test_increase_decrease_the_number_of_groups_m2m_402(freebill_user: Page, create_and_remove_25_group):
    """ ||M2M-402|| Збільшити/зменшити кількість груп, які відображаються на сторінці """
    objects_page = ObjectsPage(freebill_user)

    objects_page.page_tab_buttons["groups"].click()
    for count in ["25", "10"]:
        expect(objects_page.increase_decrease_the_number_group(count)).to_have_count(int(count))


# M2M-404 Видалити групу
@mark.testomatio('@Tttttt404')
def test_delete_a_group_m2m_404(freebill_user: Page):
    """ ||M2M-404|| Видалити групу """
    objects_page = ObjectsPage(freebill_user)

    # Create group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 3)
    objects_page.popap_btn["ok"].click()

    # Remove group
    objects_page.remove_group()
    expect(objects_page.group_table["body_row"]).not_to_be_visible()


# M2M-403 Видалити останню групу в сторінці
@mark.testomatio('@Tttttt403')
def test_remove_last_group_in_list_of_groups_M2M_403(freebill_user: Page, create_and_remove_12_group):
    """ ||M2M-403|| Видалити останню групу в сторінці """
    objects_page = ObjectsPage(freebill_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.row_on_page["next_page"].click()

    # Remove group
    objects_page.group_table["del_btn_in_row"].click()
    objects_page.popap_btn["confirm_del"].click()     
    expect(objects_page.group_table["body_row"]).to_have_count(1)


# M2M-405 Відмінити видалення групи
@mark.testomatio('@Tttttt405')
def test_cancel_deleting_a_group_m2m_405(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-405|| Відмінити видалення групи """
    objects_page = ObjectsPage(freebill_user)

    # Remove group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["del_btn_in_row"].click()
    objects_page.popap_btn["cancel_del"].click()  
    expect(objects_page.group_table["body_row"]).to_have_count(1)


# M2M-1604 Відобразити учасників групи в порожній групі
@mark.testomatio('@Ttttt1604')
def test_dispaly_group_members_in_an_empty_group_m2m_1604(freebill_user: Page, just_remove_groups):
    """ ||M2M-1604|| Відобразити учасників групи в порожній групі """
    objects_page = ObjectsPage(freebill_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 1)
    objects_page.popap_btn["ok"].click()

    # Remove objects from group
    objects_page.group_table["btns_in_row"].nth(0).click()
    objects_page.popap_btn["group_checkboxes"].nth(1).uncheck()
    objects_page.popap_btn["ok"].click()

    objects_page.group_table["expand_btn"].click(timeout=500)
    expect(objects_page.group_table["alert_msg"]).to_be_visible()


# M2M-407 Відкрити вікно властивості об'єкта в списку учасників групи
@mark.testomatio('@Tttttt407')
def test_open_the_object_properties_window_in_the_list_of_group_members_m2m_407(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-407|| Відкрити вікно властивості об'єкта в списку учасників групи """
    objects_page = ObjectsPage(freebill_user)

    # Open object settings window
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["expand_btn"].click()
    objects_page.group_table["btns_in_row"].nth(2).click()

    # Check if the object settings window is open
    expect(objects_page.object_main_popap_inputs["name"]).to_have_value("test 1")
    objects_page.popap_btn["cancel"].click()


# M2M-408 Відкрити вікно редагування групи об'єктів
@mark.testomatio('@Tttttt408')
def test_open_the_group_edit_window_m2m_408(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-408|| Відкрити вікно редагування групи об'єктів """
    objects_page = ObjectsPage(freebill_user)

    # Open group edit window
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["btns_in_row"].nth(0).click()

    # Check if the group edit window is open
    expect(objects_page.object_main_popap_inputs["name"]).to_have_value("Test_group")
    objects_page.popap_btn["cancel"].click()


# ||M2M-398|| M2M-399 || M2M-400 || Пошук групи з повною валідною назвою\\з не повною валідною назвою\\з не валідною назвою
@mark.testomatio('@Tttttt398', '@Tttttt399', '@Tttttt400')
@pytest.mark.parametrize("query, index", [("Test group 0", 1), ("group 0", 1), ("213qwe123", 0)], ids=["||M2M-398|| full_valid_name", "||M2M-399|| not_full_valid_name", "||M2M-400|| not_valid_name"])
def test_search_for_a_group_m2m_398_399_400(freebill_user: Page, create_and_remove_3_groups, query, index):
    """ ||M2M-398|| M2M-399 || M2M-400 || Пошук групи з повною валідною назвою\\з не повною валідною назвою\\з не валідною назвою """
    objects_page = ObjectsPage(freebill_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.head_menu_group_locators["group_search_input"].fill(query)

    expect(objects_page.group_table["body_row"]).to_have_count(index)
    
    

# Search-------------------------------------------------------------------------------------------------------------------------------------

# Search for an object using filters UNIQUE_ID
@mark.testomatio('@Ttttt1939', '@Ttttt1867', '@Ttttt1945')
@pytest.mark.parametrize("query, result", 
[("1005001010", 1), 
("123123", 2), 
("qwerty123", 0)], ids=["M2M-1939", "M2M-1945", "M2M-1867"])
def test_search_for_an_object_using_filters_unique_id(search_units: Page, query: str, result: int):
    """ ||M2M-406|| Пошук об'єкта за фільтрами """

    objects_page = ObjectsPage(search_units)
    objects_page.search_object("UNIQUE_ID", query)
    expect(objects_page.unit_table["body_row"]).to_have_count(int(result))


# Search for an object using filters NAME
@mark.testomatio('@Tttttt377', '@Ttttt1940', '@Ttttt1941')
@pytest.mark.parametrize("query, result",
[("Test unit 2", 1),
("Test unit", 3),
("qwerty", 0)], ids=["M2M-377", "M2M-1940", "M2M-1941"])
def test_search_for_an_object_using_filters_name(search_units: Page, query: str, result: int):
    """ ||M2M-406|| Пошук об'єкта за фільтрами """

    objects_page = ObjectsPage(search_units)
    objects_page.search_object("DEVICE_NAME", query)
    expect(objects_page.unit_table["body_row"]).to_have_count(int(result))


# Search for an object using filters PHONE_1
@mark.testomatio('@Ttttt1942')
@pytest.mark.parametrize("query, result",
[("380631231122", 1),
("068", 2),
("345345345", 0)], ids=["full valid value", "not full valid value", "not valid value"])
def test_search_object_using_filters_phone_1_m2m_1942(search_units: Page, query: str, result: int):
    """ ||M2M-406|| Пошук об'єкта за фільтрами """

    objects_page = ObjectsPage(search_units)
    objects_page.search_object("PHONE_1", query)
    expect(objects_page.unit_table["body_row"]).to_have_count(int(result))


# Search for an object using filters PHONE_2
@mark.testomatio('@Ttttt1943')
@pytest.mark.parametrize("query, result",
[("380681001010", 1),
("1122", 2),
("345345345", 0)], ids=["full valid value", "not full valid value", "not valid value"])
def test_search_object_using_filters_phone_2_m2m_1943(search_units: Page, query: str, result: int):
    """ ||M2M-406|| Пошук об'єкта за фільтрами """

    objects_page = ObjectsPage(search_units)
    objects_page.search_object("PHONE_2", query)
    expect(objects_page.unit_table["body_row"]).to_have_count(int(result))


# Filter Пошук за параметром "Обліковий запис"
@mark.testomatio('@Ttttt1946')
@pytest.mark.parametrize("query, result",
[("m2m.test.auto+search_unit@gmail.com", 3),
("search_unit@gmai", 3),
("qwerty@ddd", 0)], ids=["full valid value", "not full valid value", "not valid value"])
def test_search_object_using_filters_account_m2m_1946(search_units: Page, query: str, result: int):
    """ ||M2M-406|| Пошук об'єкта за фільтрами """

    objects_page = ObjectsPage(search_units)
    objects_page.search_object("ACCOUNT", query)
    expect(objects_page.unit_table["body_row"]).to_have_count(int(result))


# Здійснити експорт списку об'єктів в форматі CSV / XLS
@mark.testomatio('@Ttttt1957')
@pytest.mark.parametrize("chose_item, expected_format", [("second", ".csv"), ("first", ".xls")], ids=["CSV", "XLS"])
def test_export_objects_in_file_m2m_1957(search_units: Page, chose_item: str, expected_format: str):
    """ ||M2M-1957|| Здійснити експорт списку об'єктів в форматі CSV """
    
    base_page = BasePage(search_units)
    objects_page = ObjectsPage(search_units)

    objects_page.head_menu_unit_locators["export"].click()

    # Викликаємо функцію завантаження
    download = base_page.trigger_download(chose_item)

    # Перевіряємо, що файл справді завантажився
    assert download is not None, "Файл не завантажився!"
    filename = f"downloads/{download.suggested_filename}"
    print(f"Файл завантажено: {filename}")
    assert filename.lower().endswith(expected_format), f"Файл має неправильне розширення: {filename}"

    # Зберігаємо файл
    download.save_as(filename)

    # Очищення після тесту
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Файл {filename} видалено.")
