from playwright.sync_api import Page
import random


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://staging.m2m.eu/login")

        self.email_input = self.page.locator("label:has-text('Email')")
        self.password_input = self.page.locator("input[name='password']")

        self.acsept_btn = self.page.locator("button[type='submit']")

        self.restore_password_link = self.page.get_by_role("link", name="Відновити пароль")
        self.login_as_btn = self.page.get_by_text("Увійти як").first
        self.sign_up_btn = self.page.get_by_role("link", name="Створити")
        self.user_agriment_btn = self.page.get_by_text("Користувацька угода") 
        self.terms_of_use_btn = self.page.get_by_text("Умови користування") 
        self.show_password_btn = self.page.get_by_label("toggle password visibility")
        self.go_back_btn = self.page.get_by_role("link", name="Повернутись")


        self.repeat_password_input = self.page.locator("input[name='repeatPassword']")
        self.language_select = self.page.get_by_role("combobox")
        self.i_agree_checkbox = self.page.get_by_role("checkbox")

        self.login_btn = self.page.get_by_role("link", name="Увійти")

        self.error_block = self.page.get_by_text("Невірні логін або пароль")

        self.user_is_exist_msg = self.page.get_by_text("Такий користувач вже існує")

        self.term_popup = self.page.get_by_role("dialog")
        self.login_as_list = self.page.locator("ul")
        self.login_as_input = self.page.locator("input#outlined-basic")
        self.close_login_as_popap = self.page.locator("h2 div")

        self.user_email_profile_input = self.page.get_by_label("Логін/email")


    def language(self, language_code: str):
        language_dict = {
            "ua": "Українська",
            "ru": "Русский",
            "en": "English"
        }
        
        self.language_name = language_dict[language_code]
        self.language_option = self.page.get_by_role("option", name=self.language_name)

        return self.language_option.click()


    def login(self, user_email: str, password: str):
        self.email_input.fill(user_email)
        self.password_input.fill(password)


    def login_as(self, user_email: str, password: str, user_type: str):
        self.email_input.fill(user_email)
        self.password_input.fill(password)
        self.login_as_btn.click()
        self.page.get_by_text(user_type).click()


    def sign_up(self, user_email: str, password: str, repeat_password: str, language_code: str):
        self.email_input.fill(user_email)
        self.password_input.fill(password)
        self.repeat_password_input.fill(repeat_password)
        self.language_select.click()
        self.language(language_code)

    
    def is_logged_in(self) -> bool:
        """Перевіряє, чи користувач залогінений на основі заголовка сторінки."""
        try:
            # Отримуємо текст заголовка
            header_text = self.page.locator("header h1").first.text_content()
            return header_text == "Моніторинг" or header_text == "Monitoring"
        except:
            # Якщо заголовок не знайдено або виникла помилка, користувач вважається вилогіненим
            return False


    