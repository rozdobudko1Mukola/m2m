import os
import pytest
from pytest import mark
from playwright.sync_api import expect

from pages.e2e.search_using_filter import FilterSearch


@pytest.mark.usefixtures("user_page")
class TestSearchObjectByFilters:

    @pytest.fixture(autouse=True)
    def open_units_page(self, user_page):
        """Відкрити сторінку перед кожним тестом у класі"""
        user_page.goto("/units")

    #  Filter Пошук об'єкта за Ім'ям з повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Tttttt377')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_377(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        """ ||Tttttt377|| Пошук об'єкта за фільтрами """
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("name", class_test_data["device_name"][0])).to_have_count(1)

        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["device_name"][0])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["uniqueId"][0])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["phone"][0])

    # Filter Пошук об'єкта за Ім'ям з частковою валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T7b7eb3cb')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_object_using_filters_name_T7b7eb3cb(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        """ ||@T7b7eb3cb|| Пошук об'єкта за фільтрами """
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("name", class_test_data["device_name"][1].replace("Test ", ""))).to_have_count(1)

        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["device_name"][1])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["uniqueId"][1])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["phone"][1])

    # Filter Пошук об'єкта за Ім'ям з не валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T0a7858f3')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_T0a7858f3(self, user_page, full_unit_create_and_remove_by_api):
        """ ||@T0a7858f3|| Пошук об'єкта за фільтрами """
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("name", "qwerty123")).to_have_count(0)

    # Filter Пошук об'єкта за Унікальним ID з повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1939')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1939(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        """ ||@Ttttt1939|| Пошук об'єкта за фільтрами """
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("device_id", class_test_data["uniqueId"][0])).to_have_count(1)

        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["device_name"][0])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["uniqueId"][0])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["phone"][0])

    # Filter Пошук об'єкта за Унікальним ID з часковою валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T48506b7a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T48506b7a(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        """ ||@T48506b7a|| Пошук об'єкта за фільтрами """
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("device_id", str(class_test_data["uniqueId"][1])[:4])).to_have_count(1)

        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["device_name"][1])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["uniqueId"][1])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["phone"][1])

    # Filter Пошук об'єкта за унікальним ID з не валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1867')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1867(self, user_page, full_unit_create_and_remove_by_api):
        """ ||@Ttttt1867|| Пошук об'єкта за фільтрами """
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("device_id", "qwerty123")).to_have_count(0)

    # Filter Пошук об'єкта за параметром "Номер телефону" з валідною назвою сім 1
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T09500e2a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T09500e2a(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        """ ||@T09500e2a|| Пошук об'єкта за фільтрами """
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("phone", class_test_data["phone"][0])).to_have_count(2)

        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["device_name"][0])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["uniqueId"][0])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["phone"][0])
        expect(filter_search.head_menu_unit_locators["table result"].nth(1)).to_contain_text(class_test_data["device_name"][2])
        expect(filter_search.head_menu_unit_locators["table result"].nth(1)).to_contain_text(class_test_data["uniqueId"][2])
        expect(filter_search.head_menu_unit_locators["table result"].nth(1)).to_contain_text(class_test_data["phone"][0])

    # Filter Пошук об'єкта за параметром "Номер телефону" з валідною назвою сім 2
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1942')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1942(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        """ ||@Ttttt1942|| Пошук об'єкта за фільтрами """
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("phone", class_test_data["phone2"][1])).to_have_count(1)

        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["device_name"][1])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["uniqueId"][1])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["phone2"][1])

    # Filter Пошук об'єкта за параметром "Номер телефону" з часковою валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T2ba28e23')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T2ba28e23(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("phone", class_test_data["phone2"][1][:5])).to_have_count(1)

        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["device_name"][1])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["uniqueId"][1])
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(class_test_data["phone2"][1])

# Filter Пошук об'єкта за параметром "Номер телефону" з невалідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T883e1170')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T883e1170(self, user_page, full_unit_create_and_remove_by_api):
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("phone", "qwerty123")).to_have_count(0)

    # ---------- ACCOUNT ----------------------------------------------------

    # Filter Пошук за параметром "Обліковий запис" з повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1946')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_account_full_value_Ttttt1946(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
    ):
        """||@Ttttt1946|| Пошук за параметром «Обліковий запис» (повна назва)"""
        user_email = os.getenv("SELFREG_USER_EMAIL")
        assert user_email is not None, "SELFREG_USER_EMAIL not set in environment"

        filter_search = FilterSearch(user_page)
        expect(filter_search.search_object("account", user_email)).to_have_count(3)

    # Filter Пошук за параметром "Обліковий запис" з НЕ повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T2f97bc09')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_account_partial_value_T2f97bc09(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
    ):
        """||@T2f97bc09|| Пошук за параметром «Обліковий запис» (часткова назва)"""
        user_email = os.getenv("SELFREG_USER_EMAIL")
        assert user_email is not None, "SELFREG_USER_EMAIL not set in environment"
        username = user_email.split("@")[0]

        filter_search = FilterSearch(user_page)
        expect(filter_search.search_object("account", username)).to_have_count(3)

    # Filter Пошук за параметром "Обліковий запис" з невалідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1951')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_account_invalid_value_Ttttt1951(
        self,
        user_page,
        full_unit_create_and_remove_by_api,
    ):
        """||@Ttttt1951|| Пошук за параметром «Обліковий запис» (невалідна назва)"""
        filter_search = FilterSearch(user_page)
        expect(filter_search.search_object("account", "qwerty123")).to_have_count(0)

    # ---------- MODEL ------------------------------------------------------

    # Filter Пошук за параметром "Модель трекеру" з повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T0954169c')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_model_full_value_T0954169c(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
    ):
        """||@T0954169c|| Пошук за параметром «Модель трекеру» (повна назва)"""
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("model", class_test_data["model"][1])).to_have_count(1)
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(
            class_test_data["device_name"][1]
        )
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(
            class_test_data["uniqueId"][1]
        )

    # Filter Пошук за параметром "Модель трекеру" з НЕ повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Tc1ab5e20')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_model_partial_value_Tc1ab5e20(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
    ):
        """||@Tc1ab5e20|| Пошук за параметром «Модель трекеру» (часткова назва)"""
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("model", str(class_test_data["model"][0])[:5])).to_have_count(2)
        # Перевіряємо два рядки
        for idx in (0, 1):
            expect(filter_search.head_menu_unit_locators["table result"].nth(idx)).to_contain_text(
                class_test_data["device_name"][idx if idx == 0 else 2]
            )

    # Filter Пошук за параметром "Модель трекеру" з невалідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Tfb936487')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_model_invalid_value_Tfb936487(
        self,
        user_page,
        full_unit_create_and_remove_by_api,
    ):
        """||@Tfb936487|| Пошук за параметром «Модель трекеру» (невалідна назва)"""
        filter_search = FilterSearch(user_page)
        expect(filter_search.search_object("model", "qawerty123")).to_have_count(0)

# ---------- ADMIN FIELDS ----------------------------------------------
    # Filter Пошук за «Адміністративними полями» з повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T0a3bed46')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_admin_fields_full_value_T0a3bed46(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
    ):
        """||@T0a3bed46|| Пошук за «Адміністративними полями» (повна назва)"""
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("admin_field", "value 123")).to_have_count(2)
        # Перевіряємо два рядки
        for idx in (0, 1):
            expect(filter_search.head_menu_unit_locators["table result"].nth(idx)).to_contain_text(
                class_test_data["uniqueId"][idx if idx == 0 else 2]
            )

    # Filter Пошук за «Адміністративними полями» з НЕ повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T06840ffd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_admin_fields_partial_value_T06840ffd(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
    ):
        """||@T06840ffd|| Пошук за «Адміністративними полями» (часткова назва)"""
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("admin_field", "admin")).to_have_count(1)
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(
            class_test_data["uniqueId"][1]
        )

    # Filter Пошук за «Адміністративними полями» з невалідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T1cd32951')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_admin_fields_invalid_value_T1cd32951(
        self,
        user_page,
        full_unit_create_and_remove_by_api,
    ):
        """||@T1cd32951|| Пошук за «Адміністративними полями» (невалідна назва)"""
        filter_search = FilterSearch(user_page)
        expect(filter_search.search_object("admin_field", "qwerty 123")).to_have_count(0)

    # ---------- CUSTOM FIELDS ---------------------------------------------
    # Filter Пошук за «Довільними полями» з повною валідною назвою
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T4bca3ad1')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_custom_fields_full_value_T4bca3ad1(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
    ):
        """||@T4bca3ad1|| Пошук за «Довільними полями» (повна назва)"""
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("custom_field", "custom Field value")).to_have_count(2)
        for idx in (0, 1):
            expect(filter_search.head_menu_unit_locators["table result"].nth(idx)).to_contain_text(
                class_test_data["uniqueId"][idx if idx == 0 else 2]
            )

    # Filter Пошук за «Довільними полями» (часткова назва)
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ta4686336')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_custom_fields_partial_value_Ta4686336(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
    ):
        """||@Ta4686336|| Пошук за «Довільними полями» (часткова назва)"""
        filter_search = FilterSearch(user_page)

        expect(filter_search.search_object("custom_field", "123")).to_have_count(1)
        expect(filter_search.head_menu_unit_locators["table result"].nth(0)).to_contain_text(
            class_test_data["uniqueId"][1]
        )

    # Filter Пошук за «Довільними полями» (невалідна назва)
    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T9f1dd8d8')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_custom_fields_invalid_value_T9f1dd8d8(
        self,
        user_page,
        full_unit_create_and_remove_by_api,
    ):
        """||@T9f1dd8d8|| Пошук за «Довільними полями» (невалідна назва)"""
        filter_search = FilterSearch(user_page)
        expect(filter_search.search_object("custom_field", "qwerty 123")).to_have_count(0)
