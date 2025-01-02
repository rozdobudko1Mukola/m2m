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
        self.avatar_btn = self.page.locator("header button").nth(3)
        self.bg_color_switcher = self.page.locator("header input")
        self.open_notifications_btn = self.page.locator("header button").nth(1)
        self.close_notifications_btn = self.page.locator("ul div svg")
        self.current_time = self.page.locator("header p")

        # Налаштування бокового меню
        self.customize_menu_btn = self.page.locator("header button").nth(2)
        self.customize_menu_list_checkbox = self.page.locator("ul li input")

        self.nav_sidebar = self.page.locator("nav")

        self.user_email = self.page.locator("ul div span").nth(1)

        # Помилки
        self.red_fild_color = self.page.locator("fieldset")  # Червоний колір полів
        self.mandatory_fields_msg = self.page.locator("form p") # Повідомлення про обов'язкові поля

