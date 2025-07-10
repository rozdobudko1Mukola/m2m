from playwright.sync_api import Page, expect
from os import getenv


class FilterSearch:

    def __init__(self, page: Page):
        self.page = page

        self.head_menu_unit_locators = {
            "filter": self.page.locator("label + div div[role='combobox']"),
            "unit_search_input": self.page.locator("input[type='text']").first,
            "table result": self.page.locator("tbody tr"),
        }

        self.filter_list = {
            "name": self.page.locator("ul[role='listbox'] > li[data-value='DEVICE_NAME']"),
            "device_id": self.page.locator("ul[role='listbox'] > li[data-value='UNIQUE_ID']"),
            "phone": self.page.locator("ul[role='listbox'] > li[data-value='PHONE']"),
            "account": self.page.locator("ul[role='listbox'] > li[data-value='ACCOUNT']"),
            "model": self.page.locator("ul[role='listbox'] > li[data-value='MODEL']"),
            "custom_field": self.page.locator("ul[role='listbox'] > li[data-value='CUSTOM_FIELDS']"),
            "admin_field": self.page.locator("ul[role='listbox'] > li[data-value='ADMIN_FIELDS']"),
        }

    def search_object(self, filter_itm: str, query: str):
        """
        filter_list:
        - name
        - device_id
        - phone
        - account
        - model
        - custom_field
        - admin_field
        """
        self.head_menu_unit_locators["filter"].click()
        text_filter_name = self.filter_list[filter_itm].inner_text()
        self.filter_list[filter_itm].click()

        expect(self.head_menu_unit_locators["filter"]).to_have_text(text_filter_name)

        self.head_menu_unit_locators["unit_search_input"].fill(query)

        return self.head_menu_unit_locators["table result"]


class BaseTestSearchObjectByFilters:

    def search_by_name_full(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("name", test_data["device_name"][0])).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][0])

    def search_by_name_partial(self, page, test_data, _):
        filter_search = FilterSearch(page)
        value = test_data["device_name"][1].replace("Test ", "")
        expect(filter_search.search_object("name", value)).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][1])

    def search_by_name_invalid(self, page, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("name", "qwerty123")).to_have_count(0)

    def search_by_device_id_full(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("device_id", test_data["uniqueId"][0])).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][0])

    def search_by_device_id_partial(self, page, test_data, _):
        filter_search = FilterSearch(page)
        partial_id = str(test_data["uniqueId"][1])[:4]
        expect(filter_search.search_object("device_id", partial_id)).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][1])

    def search_by_device_id_invalid(self, page, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("device_id", "qwerty123")).to_have_count(0)

    def search_by_phone_full(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("phone", test_data["phone"][0])).to_have_count(2)
        for idx in (0, 1):
            row = filter_search.head_menu_unit_locators["table result"].nth(idx)
            device_index = idx if idx == 0 else 2
            expect(row).to_contain_text(test_data["device_name"][device_index])

    def search_by_phone_sim2(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("phone", test_data["phone2"][1])).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][1])

    def search_by_phone_partial(self, page, test_data, _):
        filter_search = FilterSearch(page)
        partial = test_data["phone2"][1][:5]
        expect(filter_search.search_object("phone", partial)).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][1])

    def search_by_phone_invalid(self, page, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("phone", "qwerty123")).to_have_count(0)

    def search_by_account_full(self, page, test_data, _):
        user_email = getenv("SELFREG_USER_EMAIL")
        assert user_email is not None, "SELFREG_USER_EMAIL not set in environment"
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("account", user_email)).to_have_count(3)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][0])

    def search_by_account_partial(self, page, test_data, _):
        user_email = getenv("SELFREG_USER_EMAIL")
        assert user_email is not None, "SELFREG_USER_EMAIL not set in environment"
        username = user_email.split("@")[0]
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("account", username)).to_have_count(3)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][0])

    def search_by_account_invalid(self, page, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("account", "qwerty123")).to_have_count(0)

    def search_by_model_full(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("model", test_data["model"][1])).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][1])

    def search_by_model_partial(self, page, test_data, _):
        filter_search = FilterSearch(page)
        partial = str(test_data["model"][0])[:5]
        expect(filter_search.search_object("model", partial)).to_have_count(2)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][0])

    def search_by_model_invalid(self, page, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("model", "qawerty123")).to_have_count(0)

    def search_by_admin_field_full(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("admin_field", "value 123")).to_have_count(2)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][0])

    def search_by_admin_field_partial(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("admin_field", "admin")).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][1])

    def search_by_admin_field_invalid(self, page, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("admin_field", "qwerty 123")).to_have_count(0)

    def search_by_custom_field_full(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("custom_field", "custom Field value")).to_have_count(2)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][0])

    def search_by_custom_field_partial(self, page, test_data, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("custom_field", "123")).to_have_count(1)
        row = filter_search.head_menu_unit_locators["table result"].nth(0)
        expect(row).to_contain_text(test_data["device_name"][1])

    def search_by_custom_field_invalid(self, page, _):
        filter_search = FilterSearch(page)
        expect(filter_search.search_object("custom_field", "qwerty 123")).to_have_count(0)
