from playwright.sync_api import Page

class LoginPage:
    LOGIN_URL = "https://staging.m2m.eu/login"
    EMAIL_SELECTOR = "label:has-text('Email')"
    PASSWORD_SELECTOR = "input[name='password']"
    LOGIN_BUTTON_SELECTOR = "button[type='submit']"

    def __init__(self, page: Page):
        self.page = page
        self.page.goto(self.LOGIN_URL)

        self.email_input = self.page.locator(self.EMAIL_SELECTOR)
        self.password_input = self.page.locator(self.PASSWORD_SELECTOR)
        self.login_btn = self.page.locator(self.LOGIN_BUTTON_SELECTOR)

    def login(self, user_email: str, password: str):
        self.email_input.fill(user_email)
        self.password_input.fill(password)
        self.login_btn.click()