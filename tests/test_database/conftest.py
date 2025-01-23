import pytest
from playwright.sync_api import sync_playwright
from pages.login import LoginPage

STAGE_USER_FREE_BILL_PLAN = "x1pt4sqawm@vvatxiy.com"
LOCALE = 'uk-UA'
TIMEZONE_ID = 'Europe/Kiev'

@pytest.fixture(scope="function")
def login_free_paln_user(base_url):
    """Fixture for logging in a user with browser initialization."""
    with sync_playwright() as p:
        # Запускаємо браузер із slow_mo
        browser = p.chromium.launch(slow_mo=500)
        context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
        page = context.new_page()
        
        # Логін користувача
        login_page = LoginPage(page)
        login_page.login(STAGE_USER_FREE_BILL_PLAN, STAGE_USER_FREE_BILL_PLAN)
        login_page.accept_btn.click()

        yield page

        # Закриваємо сторінку, контекст та браузер
        page.close()
        context.close()
        browser.close()
