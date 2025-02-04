import pytest
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

expect_deactivate_column = ['', '№', "ОБ'ЄКТИ", 'НАЗВА', 'РЕДАГУВАТИ']
expect_activate_column = ['', '№', "ОБ'ЄКТИ", 'НАЗВА', 'РЕДАГУВАТИ', 'ТИП ОБ’ЄКТУ', 'IMEI', 'SIM 1', 'SIM 2', 'ДАТА СТВОРЕННЯ ОБ’ЄКТА', 'РЕЄСТРАЦІЙНИЙ НОМЕР', 'ОСТАННЄ ПОВІДОМЛЕННЯ ОБ’ЄКТА', 'Пауза']


# M2M-380 Прибрати/додати додаткові колонки на панелі відображення об'єктів
def test_remove_additional_columns_m2m_380(freebill_user: Page):
    """ ||M2M-380|| Прибрати/додати додаткові колонки на панелі відображення об'єктів """
    
    objects_page = ObjectsPage(freebill_user)

    # Disable all additional columns
    objects_page.head_menu_buttons["settings"].click()
    objects_page.edit_object_table()
    assert objects_page.ob_tablet_head.all_inner_texts() == expect_deactivate_column

    # Return the columns to their original state
    objects_page.edit_object_table()
    assert objects_page.ob_tablet_head.all_inner_texts() == expect_activate_column

    # # Delete all objects on pause after test
    # freebill_user.keyboard.press("Escape")


# M2M-382 Створити новий об'єкт типу "Транспортний засіб"
def test_create_new_object_VEHICLE_m2m_382(selfreg_user: Page, just_remove_units, device_type=VEHICLE_DEVICE["device_type"]["VEHICLE"], expected_text=expect_text["VEHICLE"]):
    """ ||M2M-382|| Створити новий об'єкт типу Транспортний засіб """

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
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)


# M2M-383 Створити новий об'єкт типу "Транспортний засіб з контролем пального"
def test_create_new_object_FUEL_VEHICLE_m2m_383(selfreg_user: Page, just_remove_units, device_type=VEHICLE_DEVICE["device_type"]["FUEL_VEHICLE"], expected_text=expect_text["FUEL_VEHICLE"]):
    """ ||M2M-383|| Створити новий об'єкт типу Транспортний засіб з контролем пального """

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
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)


# M2M-384 Створити новий об'єкт типу "Персональний трекер"
def test_create_new_object_PERSONAL_TRACKER_m2m_384(selfreg_user: Page, just_remove_units, device_type=VEHICLE_DEVICE["device_type"]["PERSONAL_TRACKER"], expected_text=expect_text["PERSONAL_TRACKER"]):
    """ ||M2M-384|| Створити новий об'єкт типу Персональний трекер """

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
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)


# M2M-385 Створити новий об'єкт типу "Маяк"
def test_create_new_object_BEACON_m2m_385(selfreg_user: Page, just_remove_units, device_type=VEHICLE_DEVICE["device_type"]["BEACON"], expected_text=expect_text["BEACON"]):
    """ ||M2M-385|| Створити новий об'єкт типу Маяк """

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
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)


# M2M-1540 Створити новий об'єкт при умові, що ліміт кількості пристроїв вичерпаний
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
    expect(objects_page.error_msg).to_contain_text("Досягнуто ліміту для нових пристроїв")


# M2M-387 Відмінити створення нового об'єкта
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
    expect(objects_page.ob_tablet_body).not_to_be_visible()


# M2M-388 Створити новий об'єкт не заповнивши поля "Ім'я", "Унікальний ID", "Тип" "Модель"
def test_create_new_object_without_filling_in_the_fields_m2m_388(selfreg_user: Page):
    """ ||M2M-388|| Створити новий об'єкт не заповнивши поля "Ім'я", "Унікальний ID", "Тип" "Модель" """

    objects_page = ObjectsPage(selfreg_user)

    objects_page.add_new_object("", "", "", "", "")
    objects_page.popap_btn["ok"].click()

    # Check if input color is red
    base_page = BasePage(selfreg_user)
    for index in [2, 3, 4, 10]:
        expect(base_page.red_fild_color.nth(index)).to_have_css("border-color", base_page.color_of_red)
    # Check if the error message is displayed
    expect(base_page.mandatory_fields_msg).to_have_count(4)


# M2M-389 Взаємодія з неактивними полями та розділами
def test_interaction_with_inactive_fields_and_sections_m2m_389(selfreg_user: Page):
    """ ||M2M-389|| Взаємодія з неактивними полями та розділами """

    objects_page = ObjectsPage(selfreg_user)
    objects_page.head_menu_buttons["add"].click()

    # Check if the fields are inactive
    for popup_input in ["protocol", "adress_server", "owner", "date_of_create"]:
        expect(objects_page.object_main_popap_inputs[popup_input]).to_be_disabled()

    # Check if the tabs are inactive
    for index in range(1, 6):
        expect(objects_page.object_popap_tablist["new_object_tabs"].nth(index)).to_be_disabled()


# M2M-390 Відобразити наступну та попередню сторінку зі списку об'єктів.
def test_display_the_next_and_previous_page_m2m_390(admin_user: Page):
    """ ||M2M-390|| Відобразити наступну та попередню сторінку зі списку об'єктів. """
    objects_page = ObjectsPage(admin_user)
    
    expect(objects_page.check_pagelist("objects_next_page", "objects_total_p")).to_contain_text("101-200")
    expect(objects_page.check_pagelist("objects_previous_page", "objects_total_p")).to_contain_text("1-100")


# M2M-391 Збільшити/зменшити кількість об'єктів, які відображаються на сторінці
def test_increase_decrease_the_number_of_objects_m2m_391(admin_user: Page):
    """ ||M2M-391|| Збільшити/зменшити кількість об'єктів, які відображаються на сторінці """

    objects_page = ObjectsPage(admin_user)
    for count in ["10", "25", "50", "100"]:
        expect(objects_page.increase_decrease_the_number(count)).to_have_count(int(count))


# M2M-392 Вибрати всі/один об'єкт(и) на панелі
def test_select_all_one_object_on_the_panel_m2m_392(admin_user: Page):
    """ ||M2M-392|| Вибрати всі/один об'єкт(и) на панелі """

    objects_page = ObjectsPage(admin_user)

    # Select all objects
    objects_page.ob_tablet_head.nth(0).click()
    for index in range(1, objects_page.ob_tablet_body.count() + 1):
        expect(admin_user.locator(f"//div[@id='display-tabpanel-0']//tbody/tr[{index}]/td[1]//input")).to_be_checked()
    objects_page.ob_tablet_head.nth(0).click() # Deselect all objects

    # select one object
    admin_user.locator("//div[@id='display-tabpanel-0']//tbody/tr[2]/td[1]//input").click()
    expect(admin_user.locator("//div[@id='display-tabpanel-0']//tbody/tr[2]/td[1]//input")).to_be_checked()


# M2M-393 Відкрити вікно налаштування об'єкта
def test_open_object_settings_window_m2m_393(freebill_user: Page):
    """ ||M2M-393|| Відкрити вікно налаштування об'єкта """

    objects_page = ObjectsPage(freebill_user)
    objects_page.ob_tablet_body.nth(0).filter(has=freebill_user.locator("button")).nth(0).click() # Open object settings window
    for tab in ["main", "access", "sensors", "custom_f", "admin_f", "char", "commands", "drive_detection"]:
        objects_page.object_popap_tablist[tab].click()
        expect(objects_page.object_popap_tabpanel[tab]).not_to_be_hidden()


# M2M-394 Поставити на паузу об'єкт
def test_pause_the_object_m2m_394(selfreg_user: Page, just_remove_units):
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
    selfreg_user.goto("/trash")
    expect(selfreg_user.locator("table tbody tr").nth(0)).to_contain_text('PAUSE')


# M2M-395 Скасувати переведення об'єкта на паузу
def test_cancel_pause_the_object_m2m_395(selfreg_user: Page, just_remove_units):
    """ ||M2M-395|| Скасувати переведення об'єкта на паузу """

    objects_page = ObjectsPage(selfreg_user)

    # Preconditions add object
    objects_page.precondition_add_multiple_objects(1,
    f'PAUSE {VEHICLE_DEVICE["name"]} {VEHICLE_DEVICE["device_type"]["VEHICLE"]}',
    VEHICLE_DEVICE["phone_1"],
    VEHICLE_DEVICE["phone_2"],
    VEHICLE_DEVICE['model'],
    VEHICLE_DEVICE['device_type']['VEHICLE']
    )

    objects_page.ob_tablet_head.nth(0).click(timeout=1000)
    objects_page.ob_tablet_head.nth(12).click(timeout=1000)
    objects_page.popap_btn["cancel_del"].click()
    selfreg_user.wait_for_timeout(1000)

    # Check if the object was not paused
    selfreg_user.goto("/trash")
    expect(selfreg_user.locator("table tbody tr").nth(0)).not_to_be_visible()
    selfreg_user.goto("/units")


# Group of objects----------------------------------------------------------------------------------------------------------------------------

# M2M-396 Створити нову групу обєктів
def test_create_a_new_group_of_objects_m2m_396(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-396|| Створити нову групу обєктів """

    objects_page = ObjectsPage(freebill_user)

    objects_page.head_menu_buttons["groups"].click()
    objects_page.expand_btn.click(timeout=1000)
    expect(objects_page.group_tablet_body).to_have_count(4)
    objects_page.expand_btn.click(timeout=1000)


# M2M-1564 Створити нову групу обєктів не заповнивши обов'язкові поля
def test_create_a_new_group_of_objects_without_name_m2m_1564(freebill_user: Page):
    """ ||M2M-1564|| Створити нову групу обєктів не заповнивши обов'язкові поля """
    objects_page = ObjectsPage(freebill_user)
    objects_page.head_menu_buttons["groups"].click()
    objects_page.add_new_group("", 3)
    objects_page.group_popap["ok"].click()

    base_page = BasePage(freebill_user)
    expect(base_page.red_fild_color.nth(2)).to_have_css("border-color", base_page.color_of_red)
    expect(base_page.mandatory_fields_msg.nth(0)).to_have_text("Обов'язкове поле")


# M2M-397 Відмінити створення нової групи об'єктів
def test_cancel_creating_a_new_group_of_objects_m2m_397(freebill_user: Page):
    """ ||M2M-397|| Відмінити створення нової групи об'єктів """

    objects_page = ObjectsPage(freebill_user)
    objects_page.head_menu_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 3)
    objects_page.group_popap["cancel"].click()
    expect(objects_page.group_tablet_body).not_to_be_visible()


# M2M-1542 Додати об'єкти до групи обєктів
def test_add_objects_to_a_group_of_objects_m2m_1542(freebill_user: Page, just_remove_groups):
    """ ||M2M-1542|| Додати об'єкти до групи обєктів """
    
    # Create group
    objects_page = ObjectsPage(freebill_user)
    objects_page.head_menu_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 2)
    objects_page.group_popap["ok"].click()

    # Add objects to group
    objects_page.group_table_btns.nth(0).click()
    objects_page.group_checkboxes.last.check()
    objects_page.group_popap["ok"].click()

    # Check if objects were added to the group
    objects_page.expand_btn.click(timeout=500)
    expect(objects_page.group_tablet_body).to_have_count(4)
    objects_page.expand_btn.click(timeout=500)


# M2M-1543 Видалити об'єкти з групи обєктів
def test_remove_objects_from_a_group_of_objects_m2m_1543(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-1543|| Видалити об'єкти з групи обєктів """
    objects_page = ObjectsPage(freebill_user)

    # Remove objects from group
    objects_page.head_menu_buttons["groups"].click()
    objects_page.group_table_btns.nth(0).click()
    objects_page.group_checkboxes.nth(3).click()
    objects_page.group_popap["ok"].click()

    # Check if objects were added to the group
    objects_page.expand_btn.click(timeout=500)
    expect(objects_page.group_tablet_body).to_have_count(3)
    objects_page.expand_btn.click(timeout=500)


# M2M-401 Відобразити наступну та попередню сторінку зі списку груп.
def test_display_the_next_and_previous_page_of_the_group_list_m2m_401(freebill_user: Page, create_and_remove_12_group):
    """ ||M2M-401|| Відобразити наступну та попередню сторінку зі списку груп. """
    objects_page = ObjectsPage(freebill_user)   

    objects_page.head_menu_buttons["groups"].click()
    expect(objects_page.check_pagelist("objects_next_page", "groups_total_p")).to_have_text("11-12 із 12")
    expect(objects_page.check_pagelist("objects_previous_page", "groups_total_p")).to_have_text("1-10 із 12")


# M2M-402 Збільшити/зменшити кількість груп, які відображаються на сторінці
def test_increase_decrease_the_number_of_groups_m2m_402(freebill_user: Page, create_and_remove_25_group):
    """ ||M2M-402|| Збільшити/зменшити кількість груп, які відображаються на сторінці """
    objects_page = ObjectsPage(freebill_user)

    objects_page.head_menu_buttons["groups"].click()
    for count in ["25", "10"]:
        expect(objects_page.increase_decrease_the_number_group(count)).to_have_count(int(count))


# M2M-404 Видалити групу
def test_delete_a_group_m2m_404(freebill_user: Page, just_remove_groups):
    """ ||M2M-404|| Видалити групу """
    objects_page = ObjectsPage(freebill_user)

    # Create group
    objects_page.head_menu_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 3)
    objects_page.group_popap["ok"].click()

    # Remove group
    objects_page.remove_group()
    expect(objects_page.group_tablet_body).not_to_be_visible()


# M2M-403 Видалити останню групу в сторінці
def test_remove_last_group_in_list_of_groups_M2M_403(freebill_user: Page, create_and_remove_12_group):
    """ ||M2M-403|| Видалити останню групу в сторінці """
    objects_page = ObjectsPage(freebill_user)

    objects_page.head_menu_buttons["groups"].click()
    objects_page.row_on_page["group_next_page"].click()

    # Remove group
    objects_page.group_table_btns.nth(1).click()
    objects_page.popap_btn["confirm_del"].click()     
    expect(objects_page.group_tablet_body).to_have_count(1)


# M2M-405 Відмінити видалення групи
def test_cancel_deleting_a_group_m2m_405(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-405|| Відмінити видалення групи """
    objects_page = ObjectsPage(freebill_user)

    # Remove group
    objects_page.head_menu_buttons["groups"].click()
    objects_page.group_table_btns.nth(1).click()
    objects_page.popap_btn["cancel_del"].click()
    expect(objects_page.group_tablet_body).to_have_count(1)


# M2M-1604 Відобразити учасників групи в порожній групі
def test_dispaly_group_members_in_an_empty_group_m2m_1604(freebill_user: Page, just_remove_groups):
    """ ||M2M-1604|| Відобразити учасників групи в порожній групі """
    objects_page = ObjectsPage(freebill_user)

    objects_page.head_menu_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 1)
    objects_page.group_popap["ok"].click()

    # Remove objects from group
    objects_page.group_table_btns.nth(0).click()
    objects_page.group_checkboxes.nth(1).uncheck()
    objects_page.group_popap["ok"].click()

    objects_page.expand_btn.click(timeout=500)
    expect(objects_page.alert_msg).to_be_visible()


# M2M-407 Відкрити вікно властивості об'єкта в списку учасників групи
def test_open_the_object_properties_window_in_the_list_of_group_members_m2m_407(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-407|| Відкрити вікно властивості об'єкта в списку учасників групи """
    objects_page = ObjectsPage(freebill_user)

    # Open object settings window
    
    objects_page.head_menu_buttons["groups"].click()
    objects_page.expand_btn.click()
    objects_page.group_table_btns.nth(2).click()

    # Check if the object settings window is open
    expect(objects_page.object_main_popap_inputs["name"]).to_have_value("test 1")
    objects_page.popap_btn["cancel"].click()


# M2M-408 Відкрити вікно редагування групи об'єктів
def test_open_the_group_edit_window_m2m_408(freebill_user: Page, create_and_remove_one_group):
    """ ||M2M-408|| Відкрити вікно редагування групи об'єктів """
    objects_page = ObjectsPage(freebill_user)

    # Open group edit window
    objects_page.head_menu_buttons["groups"].click()
    objects_page.group_table_btns.nth(0).click()

    # Check if the group edit window is open
    expect(objects_page.group_popap["group_name"]).to_have_value("Test_group")
    objects_page.group_popap["cancel"].click()


# ||M2M-398|| M2M-399 || M2M-400 || Пошук групи з повною валідною назвою\\з не повною валідною назвою\\з не валідною назвою
@pytest.mark.parametrize("query, index", [("Test group 0", 1), ("group 0", 1), ("213qwe123", 0)], ids=["||M2M-398|| full_valid_name", "||M2M-399|| not_full_valid_name", "||M2M-400|| not_valid_name"])
def test_search_for_a_group_m2m_398_399_400(freebill_user: Page, create_and_remove_3_groups, query, index):
    """ ||M2M-398|| M2M-399 || M2M-400 || Пошук групи з повною валідною назвою\\з не повною валідною назвою\\з не валідною назвою """
    objects_page = ObjectsPage(freebill_user)

    objects_page.head_menu_buttons["groups"].click()
    objects_page.head_menu_gruop_buttons["search_input"].fill(query)

    expect(objects_page.group_tablet_body).to_have_count(index)
    
    