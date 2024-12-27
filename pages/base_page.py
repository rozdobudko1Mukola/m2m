from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
        # Елементи меню
        self.support_menu_btn = self.page.get_by_role("link", name="Підтримка")
        self.doc_menu_btn = self.page.get_by_role("link", name="Документація")
        self.profile_menu_btn = self.page.get_by_role("link", name="Профіль користувача")
        self.exit_menu_btn = self.page.get_by_role("button", name="Вихід")

        # Шапка сайту
        self.avatar_btn = self.page.locator("header button").nth(4)

        self.user_email = self.page.locator("ul div span").nth(1)

        # Помилки
        self.red_fild_color = self.page.locator("fieldset")  # Червоний колір полів
        self.mandatory_fields_msg = self.page.locator("form p") # Повідомлення про обов'язкові поля


#     def login(self, user_email, password):
#         self.email_input.fill(user_email)
#         self.password_input.fill(password)

#         self.login_btn.click() 