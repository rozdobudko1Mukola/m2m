from playwright.sync_api import Page, expect


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
