# from playwright.sync_api import Page


# class LoginPage:
#     def __init__(self, page):
#         self.page = page
#         self.page.goto("https://staging.m2m.eu/login")

#         self.email_input = self.page.get_by_label("Email")
#         self.password_input = self.page.locator("input[name='password']")

#         self.login_btn = self.page.locator("button[type='submit']")


#     def login(self, user_email, password):
#         self.email_input.fill(user_email)
#         self.password_input.fill(password)

#         self.login_btn.click() 