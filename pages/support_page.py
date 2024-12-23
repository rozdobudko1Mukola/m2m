from playwright.sync_api import Page

class SupportPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://staging.m2m.eu")

        # Лінки на форум і документацію
        self.forum_link = self.page.get_by_text("forum.m2m.eu")
        self.docs_link = self.page.get_by_role("link", name="docs.m2m.eu")

        # Локатор для даних
        self.data_list = self.page.locator("main div p")

        self.support_menu_btn = self.page.get_by_role("link", name="Підтримка")
        self.doc_menu_btn = self.page.get_by_role("link", name="Документація")
 
        self.profile_menu_btn = self.page.get_by_role("link", name="Профіль користувача")
        self.exit_menu_btn = self.page.get_by_role("button", name="Вихід")

    
    def click_exit_button(self):
        self.exit_menu_btn.click()
    

    def open_profile_page(self):
        self.profile_menu_btn.click()


    def open_doc_page(self):
        self.doc_menu_btn.click()


    def open_forum_link(self):
        # """Відкриває форум в новій вкладці"""
        self.page.goto("https://staging.m2m.eu/support")
        self.forum_link.click()


    def open_docs_link(self):
        # """Відкриває документацію в новій вкладці"""
        self.page.goto("https://staging.m2m.eu/support")
        self.docs_link.click()


    def get_contact_info(self):
        self.support_menu_btn.click()

        # """Повертає словник контактної інформації"""
        paragraphs = self.data_list.all_inner_texts()

        data_dict = {}
        for item in paragraphs:
            parts = item.split('\n')  # Розбиваємо за новим рядком
            if len(parts) == 2:  # Перевірка, що є два елементи
                key, value = parts
                data_dict[key] = value
            else:
                data_dict[parts[0]] = ""  # Якщо немає другого елемента, присвоюємо порожнє значення

        return data_dict