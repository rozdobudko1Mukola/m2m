from playwright.sync_api import Page
from pages.database.objects import ObjectsPage


class onPausePage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("/on-pause")


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


    def all_unit_move_to_trash(self):
        """Переміщає об'єкт в корзину."""
        self.page.wait_for_timeout(1000) 
        while self.ob_tablet_body.count() > 0:
            self.ob_tablet_head.first.click()
            self.ob_tablet_head.last.click()
            self.popap_btn["confirm_del"].click()
            self.page.wait_for_timeout(1000)

        
