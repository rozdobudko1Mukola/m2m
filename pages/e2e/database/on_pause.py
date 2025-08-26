from playwright.sync_api import Page, Locator


class OnPausePage:
    def __init__(self, page: Page):
        self.page = page

        # Popup buttons
        self.popup_btn = {
            "confirm": self.page.get_by_role("presentation").locator("button").nth(0),
            "reject": self.page.get_by_role("presentation").locator("button").nth(1),
        }

        # Thead buttons
        self.thead_btns = {
            "on_pause_all": self.page.locator("thead").get_by_test_id("restore"),
            "delete_all": self.page.locator("thead").get_by_test_id("remove"),
            "checkbox_all": self.page.locator("thead input"),
        }

    def role_btn_tbody(self, row: int, btn_role: str) -> Locator:
        """row - номер рядка в таблиці, починаючи з 0
        btn_role - remove або restore
        """
        return self.page.locator("tbody").get_by_test_id(btn_role).nth(row)

    def checkbox_tbody(self, row: int) -> Locator:
        """row - номер рядка в таблиці, починаючи з 0"""
        return self.page.locator("tbody input").nth(row)

    def restore_one(self, row: int, popup_btn: str):
        """row - номер рядка в таблиці
        popup_btn - confirm або reject
        """
        self.role_btn_tbody(row, "restore").click()
        self.popup_btn[popup_btn].click()

    def remove_one(self, row: int, popup_btn: str):
        self.role_btn_tbody(row, "remove").click()
        self.popup_btn[popup_btn].click()

    def restore_all(self, popup_btn: str):
        self.thead_btns["checkbox_all"].click()
        self.thead_btns["on_pause_all"].click()
        self.popup_btn[popup_btn].click()
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(1000)

    def remove_all(self, popup_btn: str):
        self.thead_btns["checkbox_all"].click()
        self.thead_btns["delete_all"].click()
        self.popup_btn[popup_btn].click()
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(1000)
