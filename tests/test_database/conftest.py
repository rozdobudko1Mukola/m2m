import pytest
from playwright.async_api import Browser, Page
from pages.login import LoginPage
from playwright.async_api import async_playwright


STAGE_USER_FREE_BILL_PLAN = "x1pt4sqawm@vvatxiy.com"
LOCALE = 'uk-UA'
TIMEZONE_ID = 'Europe/Kiev'

@pytest.fixture(scope="function")
async def login_user(base_url):
    """Fixture for logging in a user with browser initialization."""
    async with async_playwright() as p:
        # Запускаємо браузер із slow_mo
        browser = await p.chromium.launch(slow_mo=500)
        context = await browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
        page = await context.new_page()
        
        # Логін користувача
        login_page = LoginPage(page)
        await login_page.login(STAGE_USER_FREE_BILL_PLAN, STAGE_USER_FREE_BILL_PLAN)
        await login_page.accept_btn.click()

        yield page

        # Закриваємо сторінку, контекст та браузер
        await page.close()
        await context.close()
        await browser.close()