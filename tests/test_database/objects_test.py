import pytest
from playwright.sync_api import Page, expect
from pages.database.objects import ObjectsPage
import random


VEHICLE_DEVICE = {
    "name": "Test",
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
@pytest.mark.parametrize("device_type, expected_text", [
    ("VEHICLE", "Транспортний засіб"),
    ("FUEL_VEHICLE", "Транспортний засіб з контролем пального"),
    ("PERSONAL_TRACKER", "Персональний трекер"),
    ("BEACON", "Маяк")],
    ids = [
    "Транспортний засіб ||M2M-382||", 
    "Транспортний засіб з контролем пального ||M2M-383||", 
    "Персональний трекер ||M2M-384||", 
    "Маяк ||M2M-385||"
    ]
)
def test_create_new_object_m2m_382(auth_new_test_user: Page, device_type, expected_text):
    """ Створити новий об'єкт типу """

    unique_id = ''.join(random.choices('0123456789', k=random.randint(5, 20)))

    objects_page = ObjectsPage(auth_new_test_user)
    objects_page.add_new_object(
        f"{VEHICLE_DEVICE['name']} {device_type}",
        unique_id,
        VEHICLE_DEVICE["phone_1"],
        VEHICLE_DEVICE["phone_2"],
        VEHICLE_DEVICE['model'],
        VEHICLE_DEVICE['device_type'][device_type]
    )
    # Check if the object was created
    expect(objects_page.ob_tablet_body.nth(0)).to_contain_text(expected_text)

    # Delete all objects on pause after test
    objects_page.pause_all_object()
