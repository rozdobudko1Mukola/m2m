import pytest
from pytest import mark
from pages.e2e.search_using_filter import BaseTestSearchObjectByFilters


@mark.usefixtures("user_page")
class TestSearchOnUnits(BaseTestSearchObjectByFilters):

    @pytest.fixture(autouse=True)
    def open_units_page(self, user_page):
        user_page.goto("/units")

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Tttttt377')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_name_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_name_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T7b7eb3cb')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_name_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_name_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T0a7858f3')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_name_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_name_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1939')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_device_id_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_device_id_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T48506b7a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_device_id_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_device_id_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1867')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_device_id_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_device_id_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T09500e2a')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_phone_sim1(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_phone_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1942')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_phone_sim2(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_phone_sim2(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T2ba28e23')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_phone_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_phone_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T883e1170')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_phone_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_phone_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1946')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_account_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T2f97bc09')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_account_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ttttt1951')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_account_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T0954169c')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_model_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_model_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Tc1ab5e20')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_model_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_model_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Tfb936487')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_model_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_model_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T0a3bed46')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_admin_field_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_admin_field_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T06840ffd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_admin_field_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_admin_field_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T1cd32951')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_admin_field_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_admin_field_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T4bca3ad1')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_custom_field_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_custom_field_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Ta4686336')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_custom_field_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_custom_field_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T9f1dd8d8')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_custom_field_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_custom_field_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Tc70a0d71')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_sensors_full_name(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_sensors_full_name(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@T4e2c7214')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_sensors_name_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_sensors_partial_name(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.search_unit
    @mark.testomatio('@Tff8d2fa5')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_sensors_name_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_sensors_invalid_name(user_page, full_unit_create_and_remove_by_api)


@mark.usefixtures("user_page")
class TestSearchOnMonitoring(BaseTestSearchObjectByFilters):

    @pytest.fixture(autouse=True)
    def open_monitoring_page(self, user_page):
        user_page.goto("/monitoring")

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@Te794ccc2')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_377(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_name_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T7768f270')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_object_using_filters_name_T7b7eb3cb(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_name_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@Tee85d85c')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_T0a7858f3(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_name_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@Te15c99d5')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1939(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_device_id_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T27bbc415')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T48506b7a(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_device_id_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T32464abd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1867(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_device_id_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T86673fdd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T09500e2a(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_phone_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T302ec44f')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1942(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_phone_sim2(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T37eea97e')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T2ba28e23(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_phone_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@Tf03e78d5')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T883e1170(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_phone_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T8649f0f4')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_account_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T1c7711fd')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_account_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T45e8883b')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_account_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T227af8df')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_model_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_model_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T6fa72b1b')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_model_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_model_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T88b6bf4b')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_model_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_model_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@Tb73c49a8')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_admin_field_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_admin_field_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T7c6e6318')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_admin_field_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_admin_field_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T653ad405')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_admin_field_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_admin_field_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T1d2fb9c1')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_custom_field_full(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_custom_field_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T53078243')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_custom_field_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_custom_field_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T6606d437')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_custom_field_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_custom_field_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T948123a0')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_sensors_full_name(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_sensors_full_name(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T214065d4')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_sensors_name_partial(self, user_page, class_test_data, full_unit_create_and_remove_by_api):
        self.search_by_sensors_partial_name(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.monitoring
    @mark.search_unit
    @mark.testomatio('@T0e0a36a1')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_sensors_name_invalid(self, user_page, full_unit_create_and_remove_by_api):
        self.search_by_sensors_invalid_name(user_page, full_unit_create_and_remove_by_api)


@mark.usefixtures("user_page")
class TestSearchOnPause(BaseTestSearchObjectByFilters):

    @pytest.fixture(autouse=True)
    def open_on_pause_page(self, user_page):
        user_page.goto("/on-pause")

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1987')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_Ttttt1987(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_name_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1991')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_object_using_filters_name_Ttttt1991(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_name_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1992')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_Ttttt1992(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_name_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1990')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1990_on_pause(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_device_id_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1996')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1996(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_device_id_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1986')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1986(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_device_id_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1993')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1993(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_phone_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1994')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1994(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_phone_sim2(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1995')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Ttttt1995(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_phone_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Tb78c4077')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Tb78c4077(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_phone_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1997')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_full_Ttttt1997(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_account_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1988')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_partial_Ttttt1988(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_account_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.on_pause
    @mark.search_unit
    @mark.testomatio('@Ttttt1989')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_invalid_Ttttt1989(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_pause
    ):
        self.search_by_account_invalid(user_page, full_unit_create_and_remove_by_api)


@mark.usefixtures("user_page")
class TestSearchOnWastebin(BaseTestSearchObjectByFilters):

    @pytest.fixture(autouse=True)
    def open_monitoring_page(self, user_page):
        user_page.goto("/recycle-bin")

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@T71baaac6')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_T71baaac6(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_name_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@Tad16f89b')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_object_using_filters_name_Tad16f89b(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_name_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@Tf82873a3')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_name_Tf82873a3(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_name_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@T8c292698')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T8c292698(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_device_id_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@T6c903870')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T6c903870(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_device_id_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@T341ac93f')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T341ac93f(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_device_id_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@Td1473e3e')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Td1473e3e(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_phone_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@Tf2535bc3')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_Tf2535bc3(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_phone_sim2(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@T587f7b08')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T587f7b08(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_phone_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@T34552b0e')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_search_for_an_object_using_filters_T34552b0e(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_phone_invalid(user_page, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@T2b5c83d5')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_full_T2b5c83d5(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_account_full(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@Tdc852363')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_partial_Tdc852363(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_account_partial(user_page, class_test_data, full_unit_create_and_remove_by_api)

    @mark.objects
    @mark.wastebin
    @mark.search_unit
    @mark.testomatio('@T4d675d0c')
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [3], indirect=True)
    def test_account_invalid_T4d675d0c(
        self,
        user_page,
        class_test_data,
        full_unit_create_and_remove_by_api,
        move_created_devices_to_wastebin
    ):
        self.search_by_account_invalid(user_page, full_unit_create_and_remove_by_api)
