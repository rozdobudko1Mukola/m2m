from playwright.sync_api import Page
from pages.e2e.base_page import BasePage


class SupportPage:

    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page) 
        self.page.goto("/support")

        # Лінки на форум і документацію
        self.forum_link = self.page.get_by_text("forum.m2m.eu")
        self.docs_link = self.page.get_by_role("link", name="docs.m2m.eu")

        # Локатор для даних
        self.data_list = self.page.locator("main div p")


    def click_exit_button(self):
        self.base_page.exit_menu_btn.click()

    def open_profile_page(self):
        self.base_page.profile_menu_btn.click()

    def open_doc_page(self):
        self.base_page.doc_menu_btn.click()

    def open_forum_link(self):
        """Відкриває форум у новій вкладці."""
        self.forum_link.click()

    def open_docs_link(self):
        """Відкриває документацію у новій вкладці."""
        self.docs_link.click()

    def get_contact_info(self):
        """Повертає словник контактної інформації."""
        self.base_page.support_menu_btn.click()
        paragraphs = self.data_list.all_inner_texts()

        data_dict = {}
        for item in paragraphs:
            parts = item.split("\n")  # Розбиваємо за новим рядком
            if len(parts) == 2:  # Перевірка, що є два елементи
                key, value = parts
                data_dict[key.strip()] = value.strip()
            else:
                data_dict[parts[0].strip()] = ""  # Якщо немає другого елемента, присвоюємо порожнє значення

        return data_dict