import os
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
@mark.objects
@mark.unit
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


# M2M-381 Створити новий об'єкт типу з параметрами
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt382', '@Tttttt383', '@Tttttt384', '@Tttttt385')
@pytest.mark.parametrize("device_type, expected_text", [ 
    (VEHICLE_DEVICE["device_type"]["VEHICLE"], expect_text["VEHICLE"]), 
    (VEHICLE_DEVICE["device_type"]["FUEL_VEHICLE"], expect_text["FUEL_VEHICLE"]), 
    (VEHICLE_DEVICE["device_type"]["PERSONAL_TRACKER"], expect_text["PERSONAL_TRACKER"]),
    (VEHICLE_DEVICE["device_type"]["BEACON"], expect_text["BEACON"])], 
    ids=["VEHICLE_m2m_382", "FUEL_VEHICLE_m2m_383", "PERSONAL_TRACKER_m2m_384", "BEACON_m2m_385"]) 
def test_create_new_object_m2m(selfreg_user: Page, test_data, remove_units_by_api, device_type, expected_text):

    objects_page = ObjectsPage(selfreg_user)
    # Виправлено: передається device_type напряму, а не через ключ
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {device_type}",
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        device_type  # Використовуємо device_type напряму
    )
    objects_page.popap_btn["ok"].click(force=True)  # Додаємо force=True, щоб клікнути на кнопку, навіть якщо вона не видима
    selfreg_user.wait_for_timeout(1000)  # Чекаємо 1 секунду, щоб дати час на створення об'єкта
    if objects_page.popap_btn["ok"].is_visible():
        objects_page.popap_btn["ok"].click()

    objects_page.popap_btn["ok"].wait_for(state="detached", timeout=10000)  # Чекаємо, поки вікно зникне

    # Безкінечний цикл поки елемент не стане видимим
    max_retries = 10  # Максимальна кількість спроб
    retries = 0

    while not objects_page.unit_table["body_row"].nth(0).is_visible():
        if retries >= max_retries:
            raise AssertionError("Елемент не з'явився після 10 спроб оновлення сторінки")

        selfreg_user.wait_for_load_state("load")  # Чекаємо завантаження сторінки
        selfreg_user.goto("/units")  # Якщо елемент ще не з’явився, оновлюємо сторінку
        selfreg_user.wait_for_timeout(1000)  # Чекаємо 1 секунду перед повторною перевіркою

        retries += 1

    # Check if the object was created
    expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(expected_text)

    selfreg_user.wait_for_load_state("load")  # Чекаємо завантаження сторінки
    selfreg_user.goto("/units")  # Якщо елемент ще не з’явився, оновлюємо сторінку


# M2M-1540 Створити новий об'єкт при умові, що ліміт кількості пристроїв вичерпаний
@mark.objects
@mark.unit
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
@mark.objects
@mark.unit
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
@mark.objects
@mark.unit
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
@mark.objects
@mark.unit
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
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt390')
def test_display_the_next_and_previous_page_m2m_390(admin_user: Page):
    """ ||M2M-390|| Відобразити наступну та попередню сторінку зі списку об'єктів. """
    objects_page = ObjectsPage(admin_user)
    
    expect(objects_page.check_pagelist("next_page", "unit_total_p")).to_contain_text("101-200")
    admin_user.wait_for_timeout(1000)
    expect(objects_page.check_pagelist("previous_page", "unit_total_p")).to_contain_text("1-100")


# M2M-391 Збільшити/зменшити кількість об'єктів, які відображаються на сторінці
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt391')
def test_increase_decrease_the_number_of_objects_m2m_391(admin_user: Page):
    """ ||M2M-391|| Збільшити/зменшити кількість об'єктів, які відображаються на сторінці """

    objects_page = ObjectsPage(admin_user)
    for count in ["10", "25", "50", "100"]:
        expect(objects_page.increase_decrease_the_number(count)).to_have_count(int(count))


# M2M-392 Вибрати всі/один об'єкт(и) на панелі

@mark.testomatio('@Tttttt392')
@pytest.mark.parametrize("create_and_remove_units_by_api", [3], indirect=True)
def test_select_all_one_object_on_the_panel_m2m_392(selfreg_user: Page, create_and_remove_units_by_api):
    """ ||M2M-392|| Вибрати всі/один об'єкт(и) на панелі """

    objects_page = ObjectsPage(selfreg_user)

    # Select all objects
    objects_page.unit_table["head_column"].filter(has=selfreg_user.locator("input")).click()

    for index in range(1, objects_page.unit_table["body_row"].count() + 1):
        expect(selfreg_user.locator(f"//div[@id='display-tabpanel-0']//tbody/tr[{index}]/td[1]//input")).to_be_checked()
    
    objects_page.unit_table["head_column"].nth(0).click() # Deselect all objects
    selfreg_user.wait_for_timeout(1000)
    # select one object
    selfreg_user.locator("//div[@id='display-tabpanel-0']//tbody/tr[2]/td[1]//input").click()
    expect(selfreg_user.locator("//div[@id='display-tabpanel-0']//tbody/tr[2]/td[1]//input")).to_be_checked()


# M2M-393 Відкрити вікно налаштування об'єкта
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt393')
def test_open_object_settings_window_m2m_393(freebill_user: Page):
    """ ||M2M-393|| Відкрити вікно налаштування об'єкта """

    objects_page = ObjectsPage(freebill_user)
    objects_page.unit_table["btns_in_row"].nth(0).click() # Open object settings window
    for tab in ["main", "access", "sensors", "custom_f", "admin_f", "char", "commands", "drive_detection"]:
        objects_page.object_popap_tablist[tab].click()
        expect(objects_page.object_popap_tabpanel[tab]).not_to_be_hidden()


# M2M-394 Поставити на паузу об'єкт
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt394')
def test_pause_the_object_m2m_394(selfreg_user: Page, test_data, create_and_remove_units_by_api):
    """ ||M2M-394|| Поставити на паузу об'єкт """

    objects_page = ObjectsPage(selfreg_user)

    objects_page.pause_all_object()
    selfreg_user.goto("/on-pause")
    expect(selfreg_user.locator("table tbody tr").nth(0)).to_contain_text(test_data['uniqueId'])


# M2M-395 Скасувати переведення об'єкта на паузу
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt395')
def test_cancel_pause_the_object_m2m_395(selfreg_user: Page, test_data, create_and_remove_units_by_api):
    """ ||M2M-395|| Скасувати переведення об'єкта на паузу """

    objects_page = ObjectsPage(selfreg_user)
    objects_page.unit_table["head_column"].nth(0).click(timeout=1000)
    objects_page.unit_table["head_column"].nth(14).click(timeout=1000)
    objects_page.popap_btn["cancel_del"].click()
    selfreg_user.wait_for_timeout(1000)
    expect(selfreg_user.locator("table tbody tr").nth(0)).to_contain_text(test_data['uniqueId'])

    # Check if the object was not paused
    selfreg_user.goto("/on-pause")
    expect(selfreg_user.locator("table tbody tr").nth(0)).not_to_be_visible()



# Group of objects----------------------------------------------------------------------------------------------------------------------------


# M2M-396 Створити нову групу обєктів
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt396')
@pytest.mark.parametrize("create_and_remove_units_by_api", [3], indirect=True)
def test_create_a_new_group_of_objects_m2m_396(selfreg_user: Page, create_and_remove_units_by_api, delete_device_groups_after_test):
    """ ||M2M-396|| Створити нову групу обєктів """
    objects_page = ObjectsPage(selfreg_user)

    # Create group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 3)
    objects_page.popap_btn["ok"].click()
    selfreg_user.wait_for_selector("#display-tabpanel-1 table")
    expect(objects_page.group_table["body_row"]).to_have_count(1)


# M2M-1564 Створити нову групу обєктів не заповнивши обов'язкові поля
@mark.objects
@mark.unit
@mark.testomatio('@Ttttt1564')
def test_create_a_new_group_of_objects_without_name_m2m_1564(selfreg_user: Page):
    """ ||M2M-1564|| Створити нову групу обєктів не заповнивши обов'язкові поля """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("", 0)
    objects_page.popap_btn["ok"].click()

    base_page = BasePage(selfreg_user)
    expect(base_page.red_fild_color.nth(3)).to_have_css("border-color", base_page.color_of_red)
    expect(base_page.mandatory_fields_msg.nth(0)).to_have_text("Обов'язкове поле")


# M2M-397 Відмінити створення нової групи об'єктів
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt397')
def test_cancel_creating_a_new_group_of_objects_m2m_397(selfreg_user: Page):
    """ ||M2M-397|| Відмінити створення нової групи об'єктів """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 0)
    objects_page.popap_btn["cancel"].click()
    expect(objects_page.group_table["body_row"]).not_to_be_visible()


# M2M-1542 Додати об'єкти до групи обєктів
@mark.objects
@mark.unit
@mark.testomatio('@Ttttt1542')
def test_add_objects_to_a_group_of_objects_m2m_1542(selfreg_user: Page, create_and_remove_units_by_api, create_and_del_device_groups):
    """ ||M2M-1542|| Додати об'єкти до групи обєктів """
    objects_page = ObjectsPage(selfreg_user)

    # Add objects to group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["btns_in_row"].nth(0).click() # edit group btn
    objects_page.popap_groups["group_checkboxes"].last.check()
    objects_page.popap_btn["ok"].click()

    # Check if objects were added to the group
    objects_page.group_table["expand_btn"].click(timeout=500)
    expect(objects_page.group_table["body_row"]).to_have_count(2) # 1 is group itself and 1 is object


# M2M-1543 Видалити об'єкти з групи обєктів
@mark.objects
@mark.unit
@mark.testomatio('@Ttttt1543')
def test_remove_objects_from_a_group_of_objects_m2m_1543(selfreg_user: Page, create_and_remove_units_by_api, create_and_del_device_groups):
    """ ||M2M-1543|| Видалити об'єкти з групи обєктів """
    objects_page = ObjectsPage(selfreg_user)

    # Add objects to group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["btns_in_row"].nth(0).click() # edit group btn
    objects_page.popap_groups["group_checkboxes"].last.check()
    objects_page.popap_btn["ok"].click()

    # Remove objects from group
    # objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["btns_in_row"].nth(0).click() # edit group btn
    objects_page.popap_groups["group_checkboxes"].last.uncheck()
    objects_page.popap_btn["ok"].click()

    # Check if objects were added to the group
    objects_page.group_table["expand_btn"].click(timeout=500)
    expect(objects_page.group_table["body_row"]).to_have_count(1) # 1 is group itself


# M2M-401 Відобразити наступну та попередню сторінку зі списку груп.
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt401')
@pytest.mark.parametrize("create_and_del_device_groups", [12], indirect=True)
def test_display_the_next_and_previous_page_of_the_group_list_m2m_401(selfreg_user: Page, create_and_del_device_groups):
    """ ||M2M-401|| Відобразити наступну та попередню сторінку зі списку груп. """
    objects_page = ObjectsPage(selfreg_user)   

    objects_page.page_tab_buttons["groups"].click()
    expect(objects_page.check_pagelist("next_page", "groups_total_p")).to_have_text("11-12 із 12")
    expect(objects_page.check_pagelist("previous_page", "groups_total_p")).to_have_text("1-10 із 12")


# M2M-402 Збільшити/зменшити кількість груп, які відображаються на сторінці
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt402')
@pytest.mark.parametrize("create_and_del_device_groups", [25], indirect=True)
def test_increase_decrease_the_number_of_groups_m2m_402(selfreg_user: Page, create_and_del_device_groups):
    """ ||M2M-402|| Збільшити/зменшити кількість груп, які відображаються на сторінці """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.page_tab_buttons["groups"].click()
    for count in ["25", "10"]:
        expect(objects_page.increase_decrease_the_number_group(count)).to_have_count(int(count))
        expect(objects_page.group_table["body_row"]).to_have_count(int(count))


# M2M-404 Видалити групу
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt404')
def test_delete_a_group_m2m_404(selfreg_user: Page):
    """ ||M2M-404|| Видалити групу """
    objects_page = ObjectsPage(selfreg_user)

    # Create group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 0)
    objects_page.popap_btn["ok"].click()

    # Remove group
    objects_page.remove_group()
    expect(objects_page.group_table["body_row"]).not_to_be_visible()


# M2M-403 Видалити останню групу в сторінці
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt403')
@pytest.mark.parametrize("create_and_del_device_groups", [11], indirect=True)
def test_remove_last_group_in_list_of_groups_M2M_403(selfreg_user: Page, create_and_del_device_groups):
    """ ||M2M-403|| Видалити останню групу в сторінці """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.row_on_page["next_page"].click()

    # Remove group
    objects_page.group_table["del_btn_in_row"].click()
    objects_page.popap_btn["confirm_del"].click()     
    expect(objects_page.group_table["body_row"]).to_have_count(10) # 10 - це кількість груп, які залишилися на сторінці


# M2M-405 Відмінити видалення групи
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt405')
def test_cancel_deleting_a_group_m2m_405(selfreg_user: Page, create_and_del_device_groups):
    """ ||M2M-405|| Відмінити видалення групи """
    objects_page = ObjectsPage(selfreg_user)

    # Remove group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["del_btn_in_row"].click()
    objects_page.popap_btn["cancel_del"].click()  
    expect(objects_page.group_table["body_row"]).to_have_count(1)


# M2M-1604 Відобразити учасників групи в порожній групі
@mark.objects
@mark.unit
@mark.testomatio('@Ttttt1604')
def test_dispaly_group_members_in_an_empty_group_m2m_1604(selfreg_user: Page, create_and_del_device_groups):
    """ ||M2M-1604|| Відобразити учасників групи в порожній групі """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["expand_btn"].click(timeout=500)
    expect(objects_page.group_table["alert_msg"]).to_be_visible()


# M2M-407 Відкрити вікно властивості об'єкта в списку учасників групи
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt407')
def test_open_the_object_properties_window_in_the_list_of_group_members_m2m_407(selfreg_user: Page, create_and_del_device_groups, create_and_remove_units_by_api):
    """ ||M2M-407|| Відкрити вікно властивості об'єкта в списку учасників групи """
    objects_page = ObjectsPage(selfreg_user)

    # Add objects to group
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["btns_in_row"].nth(0).click() # edit group btn
    objects_page.popap_groups["group_checkboxes"].last.check()
    objects_page.popap_btn["ok"].click()

    # Open object settings window
    objects_page.group_table["expand_btn"].click()
    objects_page.group_table["btns_in_row"].nth(2).click() # edit object btn

    # Check if the object settings window is open
    expect(objects_page.object_main_popap_inputs["name"]).to_have_value("Test device 1")
    objects_page.popap_btn["cancel"].click()


# M2M-408 Відкрити вікно редагування групи об'єктів
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt408')
def test_open_the_group_edit_window_m2m_408(selfreg_user: Page, create_and_del_device_groups):
    """ ||M2M-408|| Відкрити вікно редагування групи об'єктів """
    objects_page = ObjectsPage(selfreg_user)

    # Open group edit window
    objects_page.page_tab_buttons["groups"].click()
    objects_page.group_table["btns_in_row"].nth(0).click()

    # Check if the group edit window is open
    expect(objects_page.object_main_popap_inputs["name"]).to_have_value("Test Device Group 1")
    objects_page.popap_btn["cancel"].click()


# ||M2M-398|| Пошук групи з повною валідною назвою
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt398')
@pytest.mark.parametrize("create_and_del_device_groups", [3], indirect=True)
def test_search_for_a_group_m2m_398(selfreg_user: Page, create_and_del_device_groups):
    """ ||M2M-398|| Пошук групи з повною валідною назвою """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.head_menu_group_locators["group_search_input"].fill("Test Device Group 1")

    expect(objects_page.group_table["body_row"]).to_have_count(1)


#  M2M-399 з не повною валідною назвою
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt399')
@pytest.mark.parametrize("create_and_del_device_groups", [3], indirect=True)
def test_search_for_a_group_m2m_399(selfreg_user: Page, create_and_del_device_groups):
    """  M2M-399 Пошук групи з не повною валідною назвою\\з не валідною назвою """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.head_menu_group_locators["group_search_input"].fill("Group 1")

    expect(objects_page.group_table["body_row"]).to_have_count(1)


# || M2M-400 || з не валідною назвою
@mark.objects
@mark.unit
@mark.testomatio('@Tttttt400')
@pytest.mark.parametrize("create_and_del_device_groups", [3], indirect=True)
def test_search_for_a_group_m2m_400(selfreg_user: Page, create_and_del_device_groups):
    """  M2M-400 Пошук групи з не валідною назвою """
    objects_page = ObjectsPage(selfreg_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.head_menu_group_locators["group_search_input"].fill("213qwe123")

    expect(objects_page.group_table["body_row"]).to_have_count(1)


# Здійснити пошук об'єктів в вікні створення групи об'єктів
@mark.objects
@mark.unit
@mark.testomatio('@Ttttt1565')
@pytest.mark.parametrize("query, result", [("Alfa Romeo", 2), ("Alfa", 2), ("qwerty!@#", 1)], 
ids=["full_valid_name", "not_full_valid_name", "not_valid_name"])
def test_search_unit_in_the_group_popup(admin_user: Page, query: str, result: int):
    """ ||M2M-1565|| Здійснити пошук об'єктів в вікні створення групи об'єктів """
    objects_page = ObjectsPage(admin_user)

    expect(objects_page.search_unit_in_group(query)).to_have_count(result) # очікуємо 1 об'єкт. 2 - це тому що спіску завжди одна пуста li
    
    
# Збільшити/зменшити кількість рядків на сторінці в вікні створення групи об'єктів
@mark.objects
@mark.unit
@mark.testomatio('@Ttttt1568')
def test_increase_decrease_the_units_group_popup(admin_user: Page):
    """ ||M2M-1568|| Збільшити/зменшити кількість рядків на сторінці в вікні створення групи об'єктів """
    objects_page = ObjectsPage(admin_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.head_menu_group_locators["add_group"].click()

    for count in ["25", "50", "100", "10"]:
        expect(objects_page.increase_decrease_unit_in_grpop_pop(count)).to_have_count(int(count) + 1)


# Перейти на наступну/попередню сторінку об'єктів в вікні створення групи об'єктів
@mark.objects
@mark.unit
@mark.testomatio('@Ttttt1569')
def test_display_the_next_and_previous_page_units_in_group(admin_user: Page):
    objects_page = ObjectsPage(admin_user)

    objects_page.page_tab_buttons["groups"].click()
    objects_page.head_menu_group_locators["add_group"].click()
    
    expect(objects_page.check_pagelist_unit_in_group("next_page")).to_contain_text("11-20")
    admin_user.wait_for_timeout(1000)
    expect(objects_page.check_pagelist_unit_in_group("previous_page")).to_contain_text("1-10")


# # Search-------------------------------------------------------------------------------------------------------------------------------------

class TestSearchObjectByFilters:

# Filter Пошук об'єкта за Ім'ям з повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Tttttt377')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_377(self, user_page, test_data, full_unit_create_and_remove_by_api):
        """ ||Tttttt377|| Пошук об'єкта за фільтрами """
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("DEVICE_NAME", test_data["device_name"][0])

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][0])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][0])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["phone"][0])


# Filter Пошук об'єкта за Ім'ям з частковою валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T7b7eb3cb')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_T7b7eb3cb(self, user_page, test_data, full_unit_create_and_remove_by_api):
        """ ||@T7b7eb3cb|| Пошук об'єкта за фільтрами """
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("DEVICE_NAME", test_data["device_name"][1].replace("Test ", ""))

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["phone"][1])


# Filter Пошук об'єкта за Ім'ям з не валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T0a7858f3')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_T0a7858f3(self, user_page, test_data, full_unit_create_and_remove_by_api):
        """ ||@T0a7858f3|| Пошук об'єкта за фільтрами """
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("DEVICE_NAME", "qwerty123")

        expect(objects_page.unit_table["body_row"]).to_have_count(0)


# Filter Пошук об'єкта за Унікальним ID з повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1939')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1939(self, user_page, test_data, full_unit_create_and_remove_by_api):
        """ ||@Ttttt1939|| Пошук об'єкта за фільтрами """
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("UNIQUE_ID", test_data["uniqueId"][0])

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][0])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][0])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["phone"][0])


# Filter Пошук об'єкта за Унікальним ID з часковою валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T48506b7a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T48506b7a(self, user_page, test_data, full_unit_create_and_remove_by_api):
        """ ||@T48506b7a|| Пошук об'єкта за фільтрами """
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("UNIQUE_ID", str(test_data["uniqueId"][1])[:5])

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["phone"][1])


# Filter Пошук об'єкта за унікальним ID з не валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1867')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1867(self, user_page, test_data, full_unit_create_and_remove_by_api):
        """ ||@Ttttt1867|| Пошук об'єкта за фільтрами """
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("UNIQUE_ID", "qwerty123")

        expect(objects_page.unit_table["body_row"]).to_have_count(0)


# Filter Пошук об'єкта за параметром "Номер телефону" з валідною назвою сім 1
    @mark.objects
    @mark.unit
    @mark.testomatio('@T09500e2a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T09500e2a(self, user_page, test_data, full_unit_create_and_remove_by_api):
        """ ||@T09500e2a|| Пошук об'єкта за фільтрами """
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("PHONE_1", test_data["phone"][0])

        expect(objects_page.unit_table["body_row"]).to_have_count(2)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][0])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][0])
        expect(objects_page.unit_table["body_row"].nth(1)).to_contain_text(test_data["device_name"][2])
        expect(objects_page.unit_table["body_row"].nth(1)).to_contain_text(test_data["uniqueId"][2])


# Filter Пошук об'єкта за параметром "Номер телефону" з валідною назвою сім 2
    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1942')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1942(self, user_page, test_data, full_unit_create_and_remove_by_api):
        """ ||@Ttttt1942|| Пошук об'єкта за фільтрами """
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("PHONE_1", test_data["phone2"][1])

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][1])


# Filter Пошук об'єкта за параметром "Номер телефону" з часковою валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T2ba28e23')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T2ba28e23(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("PHONE_1", str(test_data["phone2"][1])[:5])

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][1])


# Filter Пошук об'єкта за параметром "Номер телефону" з невалідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T883e1170')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T883e1170(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("PHONE_1", "qwerty123")

        expect(objects_page.unit_table["body_row"]).to_have_count(0)


# Filter Пошук за параметром "Обліковий запис" з повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1946')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1946(self, user_page, test_data, full_unit_create_and_remove_by_api):
        user_email = os.getenv("SELFREG_USER_EMAIL")  # ⬅️ отримуємо email з .env

        objects_page = ObjectsPage(user_page)
        objects_page.search_object("ACCOUNT", user_email)

        expect(objects_page.unit_table["body_row"]).to_have_count(3)


# Filter Пошук за параметром "Обліковий запис" з НЕ повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T2f97bc09')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T2f97bc09(self, user_page, test_data, full_unit_create_and_remove_by_api):
        user_email = os.getenv("SELFREG_USER_EMAIL")  # ⬅️ отримуємо email з .env
        username = user_email.split("@")[0]  # або домен — [1]

        objects_page = ObjectsPage(user_page)
        objects_page.search_object("ACCOUNT", username)

        expect(objects_page.unit_table["body_row"]).to_have_count(3)


# Filter Пошук за параметром "Обліковий запис" з не валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1951')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1951(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("ACCOUNT", "qwerty123")

        expect(objects_page.unit_table["body_row"]).to_have_count(0)


# Filter Пошук за параметром "Модель трекеру" з повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T0954169c')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T0954169c(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("MODEL_TRECKER", test_data["model"][1])

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][1])


# Filter Пошук за параметром "Модель трекеру" з НЕ повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Tc1ab5e20')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Tc1ab5e20(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("MODEL_TRECKER", str(test_data["model"][0])[:5])

        expect(objects_page.unit_table["body_row"]).to_have_count(2)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][0])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][0])   
        expect(objects_page.unit_table["body_row"].nth(1)).to_contain_text(test_data["device_name"][2])
        expect(objects_page.unit_table["body_row"].nth(1)).to_contain_text(test_data["uniqueId"][2])    


# Filter Пошук за параметром "Модель трекеру" з не валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Tfb936487')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Tfb936487(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("MODEL_TRECKER", "qawerty123")

        expect(objects_page.unit_table["body_row"]).to_have_count(0)

    
# Filter Пошук за параметром "Адміністративні поля" Повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Tfb936487')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Tfb936487(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("ADMIN_FIELDS", "value 123")

        expect(objects_page.unit_table["body_row"]).to_have_count(2)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][0])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][0])
        expect(objects_page.unit_table["body_row"].nth(1)).to_contain_text(test_data["device_name"][2])
        expect(objects_page.unit_table["body_row"].nth(1)).to_contain_text(test_data["uniqueId"][2])


# Filter Пошук за параметром "Адміністративні поля" НЕ Повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T06840ffd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T06840ffd(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("ADMIN_FIELDS", "admin")

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][1])


# Filter Пошук за параметром "Адміністративні поля" з не валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T1cd32951')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T1cd32951(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("ADMIN_FIELDS", "qwerty 123")

        expect(objects_page.unit_table["body_row"]).to_have_count(0)


# Filter Пошук за параметром "Довільні поля" з Повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T4bca3ad1')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T4bca3ad1(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("CUSTOM_FIELDS", "custom Field value")

        expect(objects_page.unit_table["body_row"]).to_have_count(2)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][0])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][0])
        expect(objects_page.unit_table["body_row"].nth(1)).to_contain_text(test_data["device_name"][2])
        expect(objects_page.unit_table["body_row"].nth(1)).to_contain_text(test_data["uniqueId"][2])


# Filter Пошук за параметром "Довільні поля" НЕ Повною валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@Ta4686336')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ta4686336(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("CUSTOM_FIELDS", "123")

        expect(objects_page.unit_table["body_row"]).to_have_count(1)
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["device_name"][1])
        expect(objects_page.unit_table["body_row"].nth(0)).to_contain_text(test_data["uniqueId"][1])


# Filter Пошук за параметром "Довільні поля" з не валідною назвою
    @mark.objects
    @mark.unit
    @mark.testomatio('@T9f1dd8d8')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T9f1dd8d8(self, user_page, test_data, full_unit_create_and_remove_by_api):
        objects_page = ObjectsPage(user_page)
        objects_page.search_object("CUSTOM_FIELDS", "qwerty 123")

        expect(objects_page.unit_table["body_row"]).to_have_count(0)


# Здійснити експорт списку об'єктів в форматі CSV / XLS
    @mark.objects
    @mark.unit
    @mark.testomatio('@Ttttt1957')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    @pytest.mark.parametrize("chose_item, expected_format", [("second", ".csv"), ("first", ".xls")], ids=["CSV", "XLS"])
    def test_export_objects_in_file_m2m_Ttttt1957(self, user_page, chose_item: str, expected_format: str, full_unit_create_and_remove_by_api):
        """ ||M2M-1957|| Здійснити експорт списку об'єктів в форматі CSV """
        
        base_page = BasePage(user_page)
        objects_page = ObjectsPage(user_page)

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



# Вікно  "Трансфер об'єктів"----------------------------------------------------------------------------------------------------------------------------


# # Здійснити трансфер об'єкта на обліковий запис, в якого досягнуто ліміт дозволених об'єктів
# @mark.testomatio('@Ttttt1571')
# def test_transfer_the_object_m2m_1571(admin_user: Page):
#     objects_page = ObjectsPage(admin_user)
#     objects_page.head_menu_unit_locators["transfer"].click()


#     objects_page.transfer_popap_func("input_search_account", "m2m.test.auto+freebill@gmail.com")
#     objects_page.transfer_popap["list_of_accounts"].nth(0).click()

#     objects_page.transfer_popap_func("input_search_unit", "Test unit")
#     objects_page.transfer_popap["list_of_units"].nth(0).click()

#     objects_page.transfer_popap["ok"].click()

#     expect(objects_page.transfer_popap["err_msg"]).to_contain_text("Неможливо здійснити переміщення")


# # Здійснити пошук облікового запису та об'єктів у вікні "Трансфер об'єктів" за допомогою валідних даних
# @mark.testomatio('@Ttttt1188')
# def test_valid_search_for_account_and_objects_in_transfer_m2m_1188(admin_user: Page):
#     objects_page = ObjectsPage(admin_user)
#     objects_page.head_menu_unit_locators["transfer"].click()

#     objects_page.transfer_popap_func("input_search_account", "m2m.test.auto+freebill@gmail.com")
#     expect(objects_page.transfer_popap["list_of_accounts"]).to_have_count(1)

#     objects_page.transfer_popap["list_of_accounts"].nth(0).click() # обераемо аккаунт тому що список обʼєктів не зявляється не обравши аккаунт
#     objects_page.transfer_popap_func("input_search_unit", "Test name unit")
#     expect(objects_page.transfer_popap["list_of_units"]).to_have_count(2) 


# # Здійснити пошук облікового запису та об'єктів у вікні "Трансфер об'єктів" за допомогою не валідних даних
# @mark.testomatio('@Ttttt1189')
# def test_invalid_search_for_account_and_objects_in_transfer_m2m_1189(admin_user: Page):
#     objects_page = ObjectsPage(admin_user)
#     objects_page.head_menu_unit_locators["transfer"].click()

#     objects_page.transfer_popap_func("input_search_account", "qwerty!@#")
#     expect(objects_page.transfer_popap["list_of_accounts"]).to_have_count(0)

#     # Oбераемо аккаунт тому що список обʼєктів не зявляється не обравши аккаунт
#     objects_page.transfer_popap_func("input_search_account", "m2m.test.auto+freebill@gmail.com")
#     objects_page.transfer_popap["list_of_accounts"].nth(0).click()

#     objects_page.transfer_popap_func("input_search_unit", "qwerty!@#")
#     expect(objects_page.transfer_popap["list_of_units"]).to_have_count(1) # дівайдеp як елемнт списку обʼєктів. тому 1 а не 0


# # Збільшити/зменшити кількість рядків на сторінці в розділах "Облікові записи" та "Об'єкти"
# @mark.testomatio('@Ttttt1190')
# def test_increase_decrease_account_and_object_rows_m2m_1190(admin_user: Page):
#     objects_page = ObjectsPage(admin_user)
#     objects_page.head_menu_unit_locators["transfer"].click()

#     for count in ["25", "50", "100", "10"]:
#         expect(objects_page.increase_decrease_the_number_transfer("dd_account", count, "list_of_accounts")).to_have_count(int(count))

#     # Oбераемо аккаунт тому що список обʼєктів не зявляється не обравши аккаунт
#     objects_page.transfer_popap_func("input_search_account", "m2m.test.auto+freebill@gmail.com")
#     objects_page.transfer_popap["list_of_accounts"].nth(0).click()

#     for count in ["25", "50", "100", "10"]:
#         expect(objects_page.increase_decrease_the_number_transfer("dd_unit", count, "list_of_units")).to_have_count(int(count) + 1) # дівайдеp як елемнт списку обʼєктів. тому + 1


# # Перейти на наступну/попередню сторінку в розділах "Облікові записи" та "Об'єкти"
# @mark.testomatio('@Ttttt1191')
# def test_display_the_next_and_previous_page_transfer_account_m2m_1191(admin_user: Page):
#     objects_page = ObjectsPage(admin_user)
#     objects_page.head_menu_unit_locators["transfer"].click()

#     expect(objects_page.check_pagelist_transfer("next_btn", 0, 1)).to_contain_text("11-20")
#     expect(objects_page.check_pagelist_transfer("prev_btn", 0, 1)).to_contain_text("1-10")

# def test_display_the_next_and_previous_page_transfer_unit_m2m_1191(admin_user: Page):
#     objects_page = ObjectsPage(admin_user)
#     objects_page.head_menu_unit_locators["transfer"].click()

#     # Oбераемо аккаунт тому що список обʼєктів не зявляється не обравши аккаунт
#     objects_page.transfer_popap_func("input_search_account", "m2m.test.auto+freebill@gmail.com")
#     objects_page.transfer_popap["list_of_accounts"].nth(0).click()

#     expect(objects_page.check_pagelist_transfer("next_btn", 1, 3)).to_contain_text("11-20")
#     expect(objects_page.check_pagelist_transfer("prev_btn", 1, 3)).to_contain_text("1-10")