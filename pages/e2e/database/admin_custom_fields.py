from playwright.sync_api import Page


class CustomAdminFieldsPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("/units")


        self.save_btn = self.page.locator("button[type='submit']")
        self.del_btn = self.page.locator("form button[type='button']")
        
        self.empty_fields = self.page.locator("form input[value='']") # nth(0) - first empty name field nth(1) - second empty value field

        self.error = {
            "msg": self.page.locator("form p"),
            "input_border": self.page.locator("form fieldset"),
            "form_err_msg": self.page.locator("form > span")
        }

        self.modal_window = {
            "modal_title": self.page.locator("h2[id='alert-dialog-title']"),
            "cancl_btn": self.page.locator("div[role='dialog']").nth(1).locator("button").nth(0),
            "save_btn": self.page.locator("div[role='dialog']").nth(1).locator("button").nth(1),
        }

    def get_field(self, field_type, index):
        return self.page.locator(f"form input[name='pairs.{index}.{field_type}']")
    
    def fill_field(self, field_type: str, value: str):
        self.page.locator(f"form input[name='{field_type}']").fill(value)

    def click_button(self, name: str):
        self.buttons[name].click()