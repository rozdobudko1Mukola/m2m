from playwright.sync_api import sync_playwright, Page


def get_token_from_email(page: Page):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            slow_mo=2000,
            args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"],
            ignore_default_args=['--disable-component-extensions-with-background-pages']
        )
        context = browser.new_context()

        # Створюємо нову сторінку в контексті
        page = context.new_page()

        # Відвідуємо google accounts
        page.goto("https://workspace.google.com/intl/uk/gmail/")

        page.locator("a.button:nth-of-type(2)").click()

        # Вводимо адресу електронної пошти
        email_input = page.locator("input[type='email']")
        email_input.fill("m2m.test.auto@gmail.com")

        try:
            button_next = page.get_by_role("button", name="Далі")
            button_next.click()
        except Exception:
            button_next = page.get_by_role("button", name="Next")
            button_next.click()

        # Вводимо пароль
        password_input = page.locator("input[type='password']")
        password_input.fill("daIgK4tsyhPuLh5")

        try:
            button_next = page.get_by_role("button", name="Далі")
            button_next.click()
        except Exception:
            button_next = page.get_by_role("button", name="Next")
            button_next.click()

        # Відвідуємо gmail
        page.goto("https://gmail.com")

        # Перевірка нових листів
        emails = page.locator("div.UI table tr").first
        emails.click()

        button = page.get_by_role("link", name="Підтвердити зміну/відновлення паролю").last
        btn_attribut = button.get_attribute("href")

        browser.close()

        return btn_attribut
