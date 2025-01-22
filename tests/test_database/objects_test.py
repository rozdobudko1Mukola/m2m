import pytest
from playwright.sync_api import Page, expect
from pages.database.objects import ObjectsPage


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


@pytest.mark.skip("This test is not implemented")
# M2M-380 Прибрати додаткові колонки на панелі відображення об'єктів
def test_remove_additional_columns_m2m_380(auth_new_test_user: Page):
    """||M2M-380|| Прибрати додаткові колонки на панелі відображення об'єктів"""
    pass


@pytest.mark.skip("This test is not implemented")
# M2M-381 Додати додаткові колонки на панелі відображення об'єктів
def test_add_additional_columns_m2m_381(auth_new_test_user: Page):
    """||M2M-381|| Додати додаткові колонки на панелі відображення об'єктів"""
    pass


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
def test_create_new_object_when_the_device_limit_is_exhausted_m2m_1540(login_user: Page):
    """ ||M2M-1540|| Створити новий об'єкт при умові, що ліміт кількості пристроїв вичерпаний """

    objects_page = ObjectsPage(login_user)

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
    expect(objects_page.ob_tablet_body).not_to_be_visible()




