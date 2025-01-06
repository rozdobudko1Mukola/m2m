import pytest
from pathlib import Path
from playwright.sync_api import Browser, Page
from pages.login import LoginPage


stage_user_email = "dkononenko1994@ukr.net"
stage_user_password = "123456"

stage_test_user_email_pass = "m2m.test.auto@gmail.com"


@pytest.fixture(scope="function")
def page(browser: Browser):
    """Фікстура для чистої сесії."""
    context = browser.new_context()
    page = context.new_page()

    yield page

    page.close()
    context.close()


# Authenticated gmail page fixture with saved state
@pytest.fixture(scope="function")
def gmail(browser: Browser):
    """Фікстура для чистої сесії."""
    context = browser.new_context(
            slow_mo=2000,
            args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"],
            ignore_default_args=['--disable-component-extensions-with-background-pages']
        )
    page = context.new_page()

    yield page

    page.close()
    context.close()


# Authenticated page fixture with saved state user
@pytest.fixture(scope="function")
def authenticated_page(browser: Browser):
    """Фікстура для сесії із збереженим станом автентифікації."""
    storage_state_path = Path("utils/.auth/storage_state.json")

    # Якщо файл стану не існує, створюємо його
    if not storage_state_path.exists():
        context = browser.new_context()

        page = context.new_page()

        login_page = LoginPage(page)
        login_page.login(stage_user_email, stage_user_password)
        login_page.acsept_btn.click()

        # Зберігаємо стан
        context.storage_state(path=str(storage_state_path))

        page.close()
        context.close()

    # Завантажуємо збережений стан
    context = browser.new_context(storage_state=str(storage_state_path))

    page = context.new_page()

    yield page

    page.close()
    context.close()


@pytest.fixture(scope="session")
def login_usere(browser: Browser):
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.login(stage_user_email, stage_user_password)
    login_page.acsept_btn.click()

    yield page

    page.close()
    context.close()


# Authenticated page fixture with saved state user m2m.test.auto@gmail.com
@pytest.fixture(scope="function")
def auth_new_test_user(browser: Browser):
    new_test_user_stage_path = Path("utils/.auth/new_test_user_stage.json")

    # Якщо файл стану не існує, створюємо його
    if not new_test_user_stage_path.exists():
        context = browser.new_context()

        page = context.new_page()

        login_page = LoginPage(page)
        login_page.login(stage_test_user_email_pass, stage_test_user_email_pass)
        login_page.acsept_btn.click()

        # Зберігаємо стан
        context.storage_state(path=str(new_test_user_stage_path))

        page.close()
        context.close()
    
    # Завантажуємо збережений стан
    context = browser.new_context(storage_state=str(new_test_user_stage_path))
    page = context.new_page()
    yield page
    page.close()
    context.close()