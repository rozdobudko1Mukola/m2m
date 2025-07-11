from playwright.sync_api import Page, Download, expect


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

        self.user_dd_window = self.page.locator("ul div span")

        # Помилки
        self.red_fild_color = self.page.locator("fieldset")  # Червоний колір полів
        self.mandatory_fields_msg = self.page.locator("form p")  # Повідомлення про обов'язкові поля

        self.color_of_red = "rgb(211, 47, 47)"  # Червоний колір

        self.export_links = {
            "first": self.page.locator("li[role='menuitem']").nth(1),
            "second": self.page.locator("li[role='menuitem']").nth(2),
        }

    def trigger_download(self, locator: str) -> Download:
        """Клікає по елементу та очікує завантаження файлу."""
        with self.page.expect_download() as download_info:
            self.export_links[locator].click()
        return download_info.value


class IncreaseDecrease():

    def __init__(self, page: Page):
        self.page = page

        self.row_on_page = {
            "first_dd_button": self.page.locator("p + div div[role='combobox']").first,
            "last_dd_button": self.page.locator("p + div div[role='combobox']").last,
            "10": self.page.locator("li[data-value='10']"),
            "25": self.page.locator("li[data-value='25']"),
            "50": self.page.locator("li[data-value='50']"),
            "100": self.page.locator("li[data-value='100']")
        }

        self.nxt_prv_btn = {
            "next": self.page.get_by_role("button", name="Go to next page"),
            "previous": self.page.get_by_role("button", name="Go to previous page")
        }

        self.table = {
            "head": self.page.locator("table thead tr th"),
            "body": self.page.locator("table tbody tr")
        }

    def increase_decrease_element(self, locator: str):
        """Змінює кількість рядків на сторінці.
        locator: "10", "25", "50", "100"
        """
        self.row_on_page["first_dd_button"].click()
        self.row_on_page[locator].click()
        expect(self.row_on_page["first_dd_button"]).to_have_text(locator)
        return self.table["body"]

    def next_previous(self, locator: str):
        """Переходить на наступну або попередню сторінку.
        locator: "next" or "previous"
        """
        self.nxt_prv_btn[locator].click()
        return self.table["body"]


class DelRestorePopup():

    def __init__(self, page: Page):
        self.page = page

        self.popap_btn = {
            "confirm_pop_btn": self.page.locator("div[role='dialog'] button").nth(0),
            "cancel_pop_btn": self.page.locator("div[role='dialog'] button").nth(1)
        }

        self.page_btn = {
            "head_btn": self.page.locator("div[class='table-title'] button"),
            "first_tr_body_btn": self.page.locator("table tbody tr:first-child button")
        }
