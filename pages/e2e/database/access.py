from playwright.sync_api import Page, expect


class AccessModule:

    def __init__(self, page: Page):
        self.page = page

        self.unit_permissions = {
            "VIEW_ELEMENT": self.page.locator("#VIEW_ELEMENT").get_by_role("checkbox"),
            "CHANGE_ELEMENT_ACCESS": self.page.locator("#CHANGE_ELEMENT_ACCESS").get_by_role("checkbox"),
            "DELETE_ELEMENT": self.page.locator("#DELETE_ELEMENT").get_by_role("checkbox"),
            "RENAME_ELEMENT": self.page.locator("#RENAME_ELEMENT").get_by_role("checkbox"),
            "CUSTOM_FIELDS_VIEW": self.page.locator("#CUSTOM_FIELDS_VIEW").get_by_role("checkbox"),
            "CUSTOM_FIELDS_EDIT": self.page.locator("#CUSTOM_FIELDS_EDIT").get_by_role("checkbox"),
            "ADMIN_FIELDS_VIEW": self.page.locator("#ADMIN_FIELDS_VIEW").get_by_role("checkbox"),
            "ADMIN_FIELDS_EDIT": self.page.locator("#ADMIN_FIELDS_EDIT").get_by_role("checkbox"),
            "CONNECTION_PARAMETERS_VIEW": self.page.locator("#CONNECTION_PARAMETERS_VIEW").get_by_role("checkbox"),
            "CONNECTION_PARAMETERS_EDIT": self.page.locator("#CONNECTION_PARAMETERS_EDIT").get_by_role("checkbox"),
            "SENSORS_MANAGEMENT": self.page.locator("#SENSORS_MANAGEMENT").get_by_role("checkbox"),
            "EXECUTE_COMMANDS": self.page.locator("#EXECUTE_COMMANDS").get_by_role("checkbox"),
            "GET_POSITIONS": self.page.locator("#GET_POSITIONS").get_by_role("checkbox"),
            "GET_REPORT_DATA": self.page.locator("#GET_REPORT_DATA").get_by_role("checkbox"),
            "DELETE_POSITIONS": self.page.locator("#DELETE_POSITIONS").get_by_role("checkbox"),
            "VIEW_DEVICE_TYPE": self.page.locator("#VIEW_DEVICE_TYPE").get_by_role("checkbox"),
            "CHANGE_DEVICE_TYPE": self.page.locator("#CHANGE_DEVICE_TYPE").get_by_role("checkbox"),
            "VIEW_SENSORS": self.page.locator("#VIEW_SENSORS").get_by_role("checkbox"),
            "DELETE_SENSORS": self.page.locator("#DELETE_SENSORS").get_by_role("checkbox"),
            "CREATE_CUSTOM_FIELDS": self.page.locator("#CREATE_CUSTOM_FIELDS").get_by_role("checkbox"),
            "CREATE_ADMIN_FIELDS": self.page.locator("#CREATE_ADMIN_FIELDS").get_by_role("checkbox"),
            "DELETE_CUSTOM_FIELDS": self.page.locator("#DELETE_CUSTOM_FIELDS").get_by_role("checkbox"),
            "DELETE_ADMIN_FIELDS": self.page.locator("#DELETE_ADMIN_FIELDS").get_by_role("checkbox"),
            "VIEW_CHARACTERISTICS": self.page.locator("#VIEW_CHARACTERISTICS").get_by_role("checkbox"),
            "EDIT_CHARACTERISTICS": self.page.locator("#EDIT_CHARACTERISTICS").get_by_role("checkbox"),
            "VIEW_COMMANDS": self.page.locator("#VIEW_COMMANDS").get_by_role("checkbox"),
            "CREATE_COMMANDS": self.page.locator("#CREATE_COMMANDS").get_by_role("checkbox"),
            "EDIT_COMMANDS": self.page.locator("#EDIT_COMMANDS").get_by_role("checkbox"),
            "DELETE_COMMANDS": self.page.locator("#DELETE_COMMANDS").get_by_role("checkbox"),
            "VIEW_TRIPDETECTOR": self.page.locator("#VIEW_TRIPDETECTOR").get_by_role("checkbox"),
            "EDIT_TRIPDETECTOR": self.page.locator("#EDIT_TRIPDETECTOR").get_by_role("checkbox"),
            "COPY_DEVICE": self.page.locator("#COPY_DEVICE").get_by_role("checkbox"),
            "IMPORT_SETTINGS": self.page.locator("#IMPORT_SETTINGS").get_by_role("checkbox"),
            "EXPORT_SETTINGS": self.page.locator("#EXPORT_SETTINGS").get_by_role("checkbox"),
        }

    def expect_permissions_state(self, expected_active: list[str]):
        """Перевіряє, що саме ці права активні, а інші — ні"""
        for key, locator in self.unit_permissions.items():
            self.page.wait_for_load_state("networkidle")
            if key in expected_active:
                expect(locator).to_be_checked()
            else:
                expect(locator).not_to_be_checked()

    def click_on_permission(self, permissions_el: str):
        """Клік по чекбоксу з доступом"""
        self.unit_permissions[permissions_el].click()
        self.page.wait_for_load_state("networkidle")
