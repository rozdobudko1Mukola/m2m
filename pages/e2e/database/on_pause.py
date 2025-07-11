from playwright.sync_api import Page
from pages.e2e.base_page import BasePage, DelRestorePopup


class onPausePage:

    def __init__(self, page: Page):
        self.page = page

    # Objects lable locators
        self.ob_tablet_head = self.page.locator("table thead tr th")
        self.ob_tablet_body = self.page.locator("table tbody tr")

    # Edit objectd popap locators
        self.popap_btn = {
            "cancel": self.page.locator("form button[tabindex='0']").nth(0),
            "ok": self.page.locator("form button[tabindex='0']").nth(1),
            "confirm_del": self.page.locator("div[role='dialog'] button").nth(0),
            "cancel_del": self.page.locator("div[role='dialog'] button").nth(1)
        }

