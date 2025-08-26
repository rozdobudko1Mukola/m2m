import pytest
from pytest import mark
from playwright.sync_api import expect, APIRequestContext
from pages.e2e.database.on_pause import OnPausePage

from pages.api.wastebin_api import WastebinAPI
from pages.api.devices_api import DeviceAPI


@pytest.fixture(scope="function")
def create_devices_only(api_context: APIRequestContext, token: str, test_data, request):
    """Фікстура для створення та видалення пристроїв через API після кожного тесту.
    Кількість пристроїв визначається параметром request.param."""

    device_api = DeviceAPI(api_context, token)
    wastebin_api = WastebinAPI(api_context, token)

    # Визначаємо кількість пристроїв для створення (за замовчуванням 1)
    num_devices = request.param if hasattr(request, "param") else 1
    test_data["device_ids"] = []
    test_data["uniqueId"] = []
    test_data["device_name"] = []

    # Створюємо пристрої та зберігаємо їхні ID
    for i in range(1, num_devices + 1):

        response = device_api.create_new_device(
            name=f"Test device {i}",
            type="VEHICLE",
            uniqueId=device_api.unique_id(),
        )
        expect(response).to_be_ok()

        test_data["unit_id"] = response.json().get("id")

        test_data["device_ids"].append(response.json().get("id"))
        test_data["device_name"].append(response.json().get("name"))

        expect(response).to_be_ok()
        test_data["uniqueId"].append(response.json().get("uniqueId"))

    # Передаємо список створених ID у тест
    yield test_data

    # Отримуємо всі ID з усіх трьох джерел
    active_ids = {
        device["id"]
        for device in device_api.retrieve_list_of_devices_with_pagination(page=1, per_page=50).json().get("items", [])
    }

    paused_ids = {
        device["id"]
        for device in wastebin_api.retrieve_a_list_of_paused_devices_with_pagination(
            page=1, per_page=50
        ).json().get("items", [])
    }

    deleted_ids = {
        device["id"]
        for device in wastebin_api.retrieve_list_of_deleted_devices_with_pagination
        (page=1, per_page=50).json().get("items", [])
    }

    # Переміщаємо все, що ще не в кошику
    for device_id in active_ids.union(paused_ids):
        move_response = wastebin_api.move_device_to_wastebin(device_id)
        expect(move_response).to_be_ok()

    # Видаляємо усе, що в кошику
    for device_id in deleted_ids.union(active_ids).union(paused_ids):
        delete_response = wastebin_api.device_permanent_delete(device_id)
        expect(delete_response).to_be_ok()

    # Очищення test_data
    test_data.pop("device_ids", None)


@pytest.fixture(scope="function")
def move_created_devices_to_pause(api_context, token, test_data):
    device_api = DeviceAPI(api_context, token)
    for device_id in test_data["device_ids"]:
        response = device_api.move_device_to_pause(device_id)
        expect(response).to_be_ok()


@pytest.fixture(scope="function")
def move_created_devices_to_wastebin(api_context, token, test_data):
    wastebin_api = WastebinAPI(api_context, token)
    for device_id in test_data["device_ids"]:
        response = wastebin_api.move_device_to_wastebin(device_id)
        expect(response).to_be_ok()


@mark.usefixtures("user_page")
class TestOnPausePage:

    @pytest.fixture(autouse=True)
    def open_units_page(self, user_page, create_devices_only, move_created_devices_to_pause):
        """Спочатку створюємо об’єкти, ставимо їх на паузу, а потім відкриваємо сторінку"""
        user_page.goto("/on-pause")
        self.page_object = OnPausePage(user_page)

    @mark.objects
    @mark.on_pause
    @mark.testomatio("@Tttttt445")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_restore_one_confirm(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.restore_one(0, "confirm")
        expect(self.page_object.page.locator("tbody tr")).to_have_count(2)

    @mark.objects
    @mark.on_pause
    @mark.testomatio("@Tttttt446")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_remove_one_confirm(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.remove_one(0, "confirm")
        expect(self.page_object.page.locator("tbody tr")).to_have_count(2)

    @mark.objects
    @mark.on_pause
    @mark.testomatio("@Ttttt1378")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_restore_all_confirm(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.restore_all("confirm")
        expect(self.page_object.page.locator("tbody tr")).not_to_be_visible()

    @mark.objects
    @mark.on_pause
    @mark.testomatio("@Ttttt1379")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_remove_all_confirm(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.remove_all("confirm")
        expect(self.page_object.page.locator("tbody tr")).not_to_be_visible()

    @mark.objects
    @mark.on_pause
    @mark.testomatio("@Tttttt447")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_remove_one_reject(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.remove_one(0, "reject")
        expect(self.page_object.page.locator("tbody tr")).to_have_count(3)

    @mark.objects
    @mark.on_pause
    @mark.testomatio("@Ttttt1380")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_remove_all_reject(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.remove_all("reject")
        expect(self.page_object.page.locator("tbody tr")).to_have_count(3)


@mark.usefixtures("user_page")
class TestWastebinPage:

    @pytest.fixture(autouse=True)
    def open_units_page(self, user_page, create_devices_only, move_created_devices_to_wastebin):
        """Спочатку створюємо об’єкти, ставимо d rjibr, а потім відкриваємо сторінку"""
        user_page.goto("/recycle-bin")
        self.page_object = OnPausePage(user_page)

    @mark.objects
    @mark.wastebin
    @mark.testomatio("@Ttttt1980")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_restore_one_confirm(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.restore_one(0, "confirm")
        expect(self.page_object.page.locator("tbody tr")).to_have_count(2)

    @mark.objects
    @mark.wastebin
    @mark.testomatio("@Ttttt1981")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_restore_all_confirm(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.restore_all("confirm")
        expect(self.page_object.page.locator("tbody tr")).not_to_be_visible()

    @mark.objects
    @mark.wastebin
    @mark.testomatio("@Tb826d687")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_restore_one_reject(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.restore_one(0, "reject")
        expect(self.page_object.page.locator("tbody tr")).to_have_count(3)

    @mark.objects
    @mark.wastebin
    @mark.testomatio("@Ttttt1983")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_remove_one_confirm(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.remove_one(0, "confirm")
        expect(self.page_object.page.locator("tbody tr")).to_have_count(2)

    @mark.objects
    @mark.wastebin
    @mark.testomatio("@T9b5b3484")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_remove_all_confirm(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.remove_all("confirm")
        expect(self.page_object.page.locator("tbody tr")).not_to_be_visible()

    @mark.objects
    @mark.wastebin
    @mark.testomatio("@Ttttt1982")
    @pytest.mark.parametrize("user_page", ["SELFREG"], indirect=True)
    @pytest.mark.parametrize("create_devices_only", [3], indirect=True)
    def test_remove_one_reject(
        self, user_page, create_devices_only, test_data
    ):
        self.page_object.remove_one(0, "reject")
        expect(self.page_object.page.locator("tbody tr")).to_have_count(3)
