from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://staging.m2m.eu/login")

        self.email_input = self.page.locator("label:has-text('Email')")
        self.password_input = self.page.locator("input[name='password']")

        self.acsept_btn = self.page.locator("button[type='submit']")

        self.restore_password_link = self.page.get_by_role("link", name="Відновити пароль")
        self.login_as_btn = self.page.get_by_text("Увійти як")
        self.sign_up_btn = self.page.get_by_role("link", name="Створити")
        self.user_agriment_btn = self.page.get_by_text("Користувацька угода") 
        self.terms_of_use_btn = self.page.get_by_text("Умови користування") 
        self.show_password_btn = self.page.get_by_label("toggle password visibility")
        self.go_back_btn = self.page.get_by_role("link", name="Повернутись на сайт")

        self.mandatory_fields_msg = self.page.locator("form p")

        self.repeat_password_input = self.page.get_by_role("input", name="repeatPassword")
        self.language_select = self.page.get_by_test_id("demo-simple-select")
        self.i_agree_checkbox = self.page.get_by_role("checkbox")

        self.login_btn = self.page.get_by_role("link", name="Увійти")

        self.error_block = self.page.get_by_text("Невірні логін або пароль")

        self.term_popup = self.page.get_by_role("dialog")


    def login(self, user_email: str, password: str):
        self.email_input.fill(user_email)
        self.password_input.fill(password)

    