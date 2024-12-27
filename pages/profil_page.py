from playwright.sync_api import Page

class ProfilePage:
    def __init__(self, page: Page):
        self.page = page

        self.first_name_input = self.page.locator("input[name='firstName']")
        self.last_name_input = self.page.locator("input[name='lastName']")
        self.email_input = self.page.locator("input[name='email']")
        self.phone_input = self.page.locator("input[name='phone']")
        self.company_input = self.page.locator("input[name='company']")
        self.position_input = self.page.locator("input[name='position']")
        self.save_btn = self.page.locator("button[type='submit']")
        self.cancel_btn = self.page.locator("button[type='button']")

    def fill_form(self, first_name, last_name, email, phone, company, position):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.company_input.fill(company)
        self.position_input.fill(position)