import pytest
from pathlib import Path
from playwright.sync_api import Browser, Page
from pages.login import LoginPage


user_email = "dkononenko1994@ukr.net"
password = "123456"


@pytest.fixture(scope="function")
def page(browser: Browser):
    """Фікстура для чистої сесії."""
    context = browser.new_context()
    page = context.new_page()

    yield page

    page.close()
    context.close()


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



@pytest.fixture(scope="session")
def authenticated_page(browser: Browser):
    """Фікстура для сесії із збереженим станом автентифікації."""
    storage_state_path = Path("utils/.auth/storage_state.json")

    # Якщо файл стану не існує, створюємо його
    if not storage_state_path.exists():
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.login(user_email, password)
        login_page.acsept_btn.click(timeout=500)

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
    login_page.login(user_email, password)
    login_page.acsept_btn.click()

    yield page

    page.close()
    context.close()