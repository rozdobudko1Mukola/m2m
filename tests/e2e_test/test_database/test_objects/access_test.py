import pytest
from pytest import mark

from playwright.sync_api import expect, APIRequestContext

from pages.e2e.database.access import AccessModule
from pages.e2e.database.objects import ObjectsPage

from pages.api.users_api import UsersAPI
from pages.api.devices_api import DeviceAPI


@pytest.fixture(scope="class")
def create_del_child_user(api_context: APIRequestContext, token: str, class_test_data, request):
    """Фікстура для створення та видалення дитячого користувача через API один раз на клас тестів."""
    users_api = UsersAPI(api_context, token)

    # Визначаємо кількість дочірніх користувачів для створення (за замовчуванням 1)
    num_users = request.param if hasattr(request, "param") else 1
    class_test_data["child_user_ids"] = []

    # Створюємо користувачів та зберігаємо їхні ID
    for i in range(1, num_users + 1):
        response = users_api.create_new_user(
            email=f"test_user_{i}@gmail.com",
            password="123123",
            language="UKRAINIAN",
            )
        expect(response).to_be_ok()

        class_test_data["child_user_ids"].append(response.json().get("id"))

    yield class_test_data

    # Видаляємо створених користувачів
    for user_id in class_test_data["child_user_ids"]:
        delete_response = users_api.remove_child_user(user_id)
        expect(delete_response).to_be_ok()

    # Очищення class_test_data
    class_test_data.pop("child_user_ids", None)


@pytest.fixture(autouse=True)
def unCheck_all_permissions(user_page, class_test_data, token: str, api_context: APIRequestContext):

    yield

    """Фікстура, яка знімає всі чекбокси прав доступу перед кожним тестом в класі."""
    device_api = DeviceAPI(api_context, token)

    response = device_api.switch_all_device_permissions_for_child_user(
        user_id=class_test_data["child_user_ids"][0],
        device_id=class_test_data["device_ids"][0],
        state="false"
    )

    expect(response).to_be_ok()


@mark.usefixtures("user_page")
class TestAccessModule:

    @pytest.fixture(autouse=True)
    def open_units_page(self, user_page, full_unit_create_and_remove_by_api, create_del_child_user):
        user_page.goto("/units")
        self.access = AccessModule(user_page)

        self.objects_page = ObjectsPage(user_page)
        self.objects_page.role_btn_tbody(0, "edit").click()
        expect(self.objects_page.object_main_popap_inputs["model"]).not_to_be_empty()
        self.objects_page.object_popap_tablist["access"].click()
        self.access.page.wait_for_load_state("networkidle")

    @mark.testomatio("@T8bbac1d8")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_copy_reports_permission(self):

        # Клікнути на чекбокс "Копіювання об’єкту"
        self.access.click_on_permission("COPY_DEVICE")

        # Очікувані активні права
        expected_active = [
            "ADMIN_FIELDS_VIEW",
            "CONNECTION_PARAMETERS_VIEW",
            "COPY_DEVICE",
            "CREATE_COMMANDS",
            "CUSTOM_FIELDS_VIEW",
            "SENSORS_MANAGEMENT",
            "VIEW_CHARACTERISTICS",
            "VIEW_COMMANDS",
            "VIEW_DEVICE_TYPE",
            "VIEW_ELEMENT",
            "VIEW_SENSORS",
            "VIEW_TRIPDETECTOR",
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2011")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_view_element_permission(self):

        # Клікнути на чекбокс "Перегляд елемента та основних властивостей"
        self.access.click_on_permission("VIEW_ELEMENT")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2012")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_get_position_permission(self):
        # Клікнути на чекбокс "Виконання треків та повідомлень"
        self.access.click_on_permission("GET_POSITIONS")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "GET_POSITIONS"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@T680274d5")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_export_settings_permission(self):
        # Клікнути на чекбокс "Експорт налаштувань"
        self.access.click_on_permission("EXPORT_SETTINGS")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "CUSTOM_FIELDS_VIEW",
            "ADMIN_FIELDS_VIEW",
            "CONNECTION_PARAMETERS_VIEW",
            "VIEW_DEVICE_TYPE",
            "VIEW_SENSORS",
            "VIEW_CHARACTERISTICS",
            "VIEW_COMMANDS",
            "VIEW_TRIPDETECTOR",
            "EXPORT_SETTINGS"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@T73cf49a9")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_import_settings_permission(self):
        # Клікнути на чекбокс "Імпорт налаштувань об’єкту"
        self.access.click_on_permission("IMPORT_SETTINGS")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "CUSTOM_FIELDS_VIEW",
            "CUSTOM_FIELDS_EDIT",
            "ADMIN_FIELDS_VIEW",
            "ADMIN_FIELDS_EDIT",
            "CONNECTION_PARAMETERS_VIEW",
            "CONNECTION_PARAMETERS_EDIT",
            "SENSORS_MANAGEMENT",
            "VIEW_DEVICE_TYPE",
            "CHANGE_DEVICE_TYPE",
            "VIEW_SENSORS",
            "VIEW_CHARACTERISTICS",
            "EDIT_CHARACTERISTICS",
            "VIEW_COMMANDS",
            "CREATE_COMMANDS",
            "VIEW_TRIPDETECTOR",
            "EDIT_TRIPDETECTOR",
            "IMPORT_SETTINGS"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2013")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_get_report_data_permission(self):
        # Клікнути на чекбокс "Виконання звітів"
        self.access.click_on_permission("GET_REPORT_DATA")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "GET_POSITIONS",
            "GET_REPORT_DATA",
            "VIEW_TRIPDETECTOR"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2014")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_del_element_permission(self):
        # Клікнути на чекбокс "Видалення об’єкту"
        self.access.click_on_permission("DELETE_ELEMENT")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "DELETE_ELEMENT"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2015")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_del_position_permission(self):
        # Клікнути на чекбокс "Видалення повідомлень"
        self.access.click_on_permission("DELETE_POSITIONS")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "GET_POSITIONS",
            "DELETE_POSITIONS"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2016")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_rename_elemen_permission(self):
        # Клікнути на чекбокс "Редагування імені об’єкту"
        self.access.click_on_permission("RENAME_ELEMENT")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "RENAME_ELEMENT"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2017")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_connection_par_view_permission(self):
        # Клікнути на чекбокс "Перегляд параметрів підключення"
        self.access.click_on_permission("CONNECTION_PARAMETERS_VIEW")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "CONNECTION_PARAMETERS_VIEW"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2018")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_conn_param_view_permission(self):
        # Клікнути на чекбокс "Редагування параметрів підключення"
        self.access.click_on_permission("CONNECTION_PARAMETERS_EDIT")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "CONNECTION_PARAMETERS_VIEW",
            "CONNECTION_PARAMETERS_EDIT"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2019")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_view_device_type_permission(self):
        # Клікнути на чекбокс "Перегляд типу об’єкту"
        self.access.click_on_permission("VIEW_DEVICE_TYPE")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "VIEW_DEVICE_TYPE"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2020")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_change_device_type_permission(self):
        # Клікнути на чекбокс "Зміна типу об’єкту"
        self.access.click_on_permission("CHANGE_DEVICE_TYPE")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "VIEW_DEVICE_TYPE",
            "CHANGE_DEVICE_TYPE",
            "VIEW_SENSORS",
            "DELETE_SENSORS"
        ]

        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)

    @mark.testomatio("@Ttttt2021")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("full_unit_create_and_remove_by_api", [1], indirect=True)
    def test_change_element_access_permission(self):
        # Клікнути на чекбокс "Управління доступом до об’єкту"
        self.access.click_on_permission("CHANGE_ELEMENT_ACCESS")

        # Очікувані активні права
        expected_active = [
            "VIEW_ELEMENT",
            "CHANGE_ELEMENT_ACCESS"
        ]
        # Виклик функції, що робить усі перевірки
        self.access.expect_permissions_state(expected_active)
