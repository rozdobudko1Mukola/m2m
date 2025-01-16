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
        self.row_per_page_dd = self.page.locator("//div[@role='combobox']")
        self.previos_page_btn = self.page.get_by_title("Go to previous page")
        self.next_page_btn = self.page.get_by_title("Go to next page")
        self.device_of_devices_text = self.page.locator("form p")


        self.device_in_diagram = self.page.locator("g.apexcharts-yaxis.apexcharts-xaxis-inversed g title")


# Add 10 devices to one diagram
    def add_device_to_diagram(self, grafic) -> list:

        """  
        grafic variable is the setting btn with the name of the diagram

        0 - Graph of stop duration
        1 - Graph of mileage
        2 - Graph of maximum speed """

        device_list = []
        self.settings_btn.nth(grafic).click()
        for i in range(10):
            self.unit_list.nth(i).click()
            device_list.append(self.unit_list.nth(i).text_content())
        self.submit_btn.click()
        device_list.sort()
        return device_list


# get vertical device list from diagram(grafic)
    def get_device_from_diagram(self):
        list = self.device_in_diagram.all_text_contents()
        list.sort()
        return list

        # list = []
        # for i in range(10):
        #     list.append(self.device_in_diagram.nth(i).text_content())
        # list.sort()
        # return list
        

# Get text from tabs and header dashbords
    def check_analytics_text(self) -> str:
        texts = [
            self.today_tab.inner_text(),
            self.yesterday_tab.inner_text(),
            self.week_tab.inner_text()
        ]
        texts.extend(self.dashbords.all_inner_texts())
        return " ".join(filter(None, texts))


# Search for a device in the list of devices
    def popup_input_search(self, search_text: str) -> str:
        self.settings_btn.nth(2).click()
        self.search_input.fill(search_text)
        self.page.wait_for_timeout(1000)


# Increase/decrease the number device list in popup
    def change_device_list(self, number: int) -> int:

        """  
        numer variable is the number of devices in the list

        10 - 10 devices (by default)
        25 - 25 devices
        50 - 50 devices
        100 - 100 devices
        """
        device_list = []
        self.settings_btn.nth(2).click()
        self.row_per_page_dd.click()
        self.page.locator(f"//*[@data-value='{number}']").click()
        self.page.wait_for_timeout(1000)

        for i in range(number):
            self.unit_list.nth(i)
            device_list.append(self.unit_list.nth(i).text_content())

        return device_list

    
# Go to the next/previous page of the list in the "Select up to 10 objects" window
    def next_page(self):
        self.settings_btn.nth(0).click()
        first_page_devices_list = self.page.locator("//div[@role='list']").all_text_contents()
        self.next_page_btn.click()
        self.page.wait_for_timeout(1000)
        second_page_devices_list = self.page.locator("//div[@role='list']").all_text_contents()
        return first_page_devices_list != second_page_devices_list
