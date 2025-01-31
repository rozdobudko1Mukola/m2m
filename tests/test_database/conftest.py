import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from pages.database.objects import ObjectsPage
from pages.database.on_pause import onPausePage



# Group Fixtures ------------------------------------------------------------

@pytest.fixture
def create_and_remove_one_group(freebill_user: Page):
    objects_page = ObjectsPage(freebill_user)

    # Create group
    objects_page.head_menu_buttons["groups"].click()
    objects_page.add_new_group("Test_group", 3)
    objects_page.group_popap["ok"].click()
    freebill_user.wait_for_selector("#display-tabpanel-1 table")

    yield

    # Remove group
    freebill_user.wait_for_timeout(1000)
    while objects_page.group_tablet_body.count() > 0:
        objects_page.remove_group()
        freebill_user.wait_for_timeout(500)


@pytest.fixture()
def create_and_remove_12_group(freebill_user: Page, index=12):
    objects_page = ObjectsPage(freebill_user)
    objects_page.head_menu_buttons["groups"].click()

    # Create group
    for i in range(1, index + 1):
        objects_page.add_new_group(f"Test group {i}", 3)
        objects_page.group_popap["ok"].click()

    yield

    # Remove group
    freebill_user.wait_for_timeout(1000)
    while objects_page.group_tablet_body.count() > 0:
        objects_page.remove_group()
        freebill_user.wait_for_timeout(500)


@pytest.fixture()
def create_and_remove_3_groups(freebill_user: Page, index=3):
    objects_page = ObjectsPage(freebill_user)
    objects_page.head_menu_buttons["groups"].click()

    # Create group
    for i in range(index):
        objects_page.add_new_group(f"Test group {i}", 3)
        objects_page.group_popap["ok"].click()

    yield

    # Remove group
    if objects_page.head_menu_gruop_buttons["search_input"].input_value() != "":
        objects_page.head_menu_gruop_buttons["search_input"].fill("")
        freebill_user.wait_for_timeout(1000)

        while objects_page.group_tablet_body.count() > 0:
            objects_page.remove_group()
            freebill_user.wait_for_timeout(500)


@pytest.fixture
def create_and_remove_25_group(freebill_user: Page, index=26):
    objects_page = ObjectsPage(freebill_user)
    objects_page.head_menu_buttons["groups"].click()

    # Create group
    for i in range(1, index):
        objects_page.add_new_group(f"Test_group {i}", 3)
        objects_page.group_popap["ok"].click()
    freebill_user.wait_for_timeout(500)

    yield

    # Remove group
    freebill_user.wait_for_timeout(1000)
    while objects_page.group_tablet_body.count() > 0:
        objects_page.remove_group()
        freebill_user.wait_for_timeout(500)


@pytest.fixture
def just_remove_groups(freebill_user: Page):
    objects_page = ObjectsPage(freebill_user)

    yield 
    # Remove group
    freebill_user.wait_for_timeout(1000)
    while objects_page.group_tablet_body.count() > 0:
        objects_page.remove_group()
        freebill_user.wait_for_timeout(500)


# Units Fixtures --------------------------------------------------------------

@pytest.fixture
def create_and_remove_one_units(selfreg_user: Page):
    objects_page = ObjectsPage(selfreg_user)

    # Preconditions add object
    objects_page.precondition_add_multiple_objects(1, "Auto_Test", "180455679224", "180455679224", "Teltonika FMB965", "VEHICLE")
    objects_page.unit_table["body_row"].is_visible()
    yield  # Provide the data to the test

    # Delete all objects from pause to trash after test
    selfreg_user.wait_for_timeout(1000)
    while objects_page.unit_table["body_row"].count() > 0:
        objects_page.move_to_trash_all_object()
        selfreg_user.wait_for_timeout(500)


@pytest.fixture
def just_remove_units(selfreg_user: Page):
    objects_page = ObjectsPage(selfreg_user)

    yield  # Provide the data to the test

    # Delete all objects from pause to trash after test
    selfreg_user.wait_for_timeout(1000)
    while objects_page.unit_table["body_row"].count() > 0:
        objects_page.move_to_trash_all_object()
        selfreg_user.wait_for_timeout(500)

@pytest.fixture
def move_unnit_to_trash(selfreg_user: Page):
    objects_page = ObjectsPage(selfreg_user)

    yield  # Provide the data to the test

    on_pause_page = onPausePage(selfreg_user)
    on_pause_page.all_unit_move_to_trash()

# @pytest.fixture
# def just_remove_units(selfreg_user: Page):
#     print("\nTearing down resources...")
#     objects_page = ObjectsPage(selfreg_user)

#     yield  # Provide the data to the test
#     # Teardown: Clean up resources (if any) after the test
#     print("\nTearing down resources...")
#     objects_page.pause_all_object()
#     # Delete all objects from pause to trash after test
#     on_pause_page = onPausePage(selfreg_user)
#     on_pause_page.all_unit_move_to_trash()