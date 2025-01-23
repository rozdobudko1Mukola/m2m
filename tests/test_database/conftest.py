import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from pages.login import LoginPage

STAGE_USER_FREE_BILL_PLAN = "x1pt4sqawm@vvatxiy.com"
LOCALE = 'uk-UA'
TIMEZONE_ID = 'Europe/Kiev'


@pytest.fixture(scope="function")
def login_free_paln_user(browser: Browser, base_url):
    """Fixture for logging in a user."""
    context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.login(STAGE_USER_FREE_BILL_PLAN, STAGE_USER_FREE_BILL_PLAN)
    login_page.accept_btn.click()
    page.wait_for_timeout(1000)

    yield page

    page.close()
    context.close() 