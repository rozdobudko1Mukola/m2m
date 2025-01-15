from playwright.sync_api import Page
from pages.base_page import BasePage


class AnalyticsPage:

    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page) 
        self.page.goto("/dashboard")

        # Локатори для табів
        self.today_tab = self.page.locator("button#simple-tab-0")
        self.yesterday_tab = self.page.locator("button#simple-tab-1")
        self.week_tab = self.page.locator("button#simple-tab-2")

        self.dashbords = self.page.locator("//div[@id='simple-tabpanel-0']/div/div/div/div/div/div/span")

        self.settings_btn = self.page.locator("//div[@id='simple-tabpanel-0']/div/div/div/div/div/div/span/following-sibling::div")

        #popup locators
        self.search_input = self.page.locator("input#outlined-basic")
        self.unit_list = self.page.locator("//div[@role='list']/div")
        self.submit_btn = self.page.locator("//button[@type='submit']")

        self.device_in_diagram = self.page.locator("g.apexcharts-yaxis.apexcharts-xaxis-inversed g title")


    def add_device_to_diagram(self):
        list = []
        self.settings_btn.nth(1).click()
        for i in range(10):
            self.unit_list.nth(i).click()
            list.append(self.unit_list.nth(i).text_content())
        self.submit_btn.click()
        list.sort()
        return list


    def get_device_from_diagram(self):
        list = []
        for i in range(10):
            list.append(self.device_in_diagram.nth(i).text_content())
        list.sort()
        return list
        

    def check_analytics_text(self) -> str:
        texts = [
            self.today_tab.inner_text(),
            self.yesterday_tab.inner_text(),
            self.week_tab.inner_text()
        ]
        texts.extend(self.dashbords.all_inner_texts())
        return " ".join(filter(None, texts))