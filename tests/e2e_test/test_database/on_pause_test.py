import pytest
from pytest import mark
from playwright.sync_api import expect
from pages.e2e.base_page import IncreaseDecrease
from pages.e2e.database.on_pause import onPausePage


@mark.usefixtures("user_page")
class TestOnPause:

    @pytest.fixture(autouse=True)
    def open_units_page(self, user_page):
        user_page.goto("/on-pause")

    @mark.on_pause
    @mark.objects
    @mark.testomatio('@Tttttt443')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [25], indirect=True)
    def test_next_previous_page_Tttttt443(
            self,
            user_page,
            full_unit_create_and_remove_by_api,
            move_created_devices_to_pause
            ):
        """
        ||@Tttttt443|| Відобразити наступну та попередню сторінку зі списку об'єктів на паузі'.
        """
        inc_dec = IncreaseDecrease(user_page)

        # Перевірка переходу на наступну сторінку
        expect(inc_dec.next_previous("next")).to_have_count(10)
        expect(inc_dec.next_previous("next")).to_have_count(5)

        # Перевірка переходу на попередню сторінку
        expect(inc_dec.next_previous("previous")).to_have_count(10)

    @mark.on_pause
    @mark.objects
    @mark.testomatio('@Tttttt444')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [25], indirect=True)
    def test_increase_decrease_number_of_objects_Tttttt444(
            self,
            user_page,
            full_unit_create_and_remove_by_api,
            move_created_devices_to_pause
            ):
        """
        ||@Tttttt444|| Збільшити/зменшити кількість об'єктів, які відображаються на сторінці.
        """
        inc_dec = IncreaseDecrease(user_page)

        # Перевірка збільшення кількості рядків на сторінці
        expect(inc_dec.increase_decrease_element("25")).to_have_count(25)

        # Перевірка зменшення кількості рядків на сторінці
        expect(inc_dec.increase_decrease_element("10")).to_have_count(10)
