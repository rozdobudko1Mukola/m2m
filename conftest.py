import pytest
from pathlib import Path
from playwright.sync_api import Browser
from pages.login import LoginPage


@pytest.fixture(scope="function")
def page(browser: Browser):
    """Фікстура для чистої сесії."""
    context = browser.new_context()
    page = context.new_page()

    yield page

    page.close()
    context.close()


@pytest.fixture(scope="function")
def authenticated_page(browser: Browser):
    """Фікстура для сесії із збереженим станом автентифікації."""
    storage_state_path = Path("utils/.auth/storage_state.json")

    # Якщо файл стану не існує, створюємо його
    if not storage_state_path.exists():
        context = browser.new_context()
        page = context.new_page()

        user_email = "dkononenko1994@ukr.net"
        password = "123456"

        login_page = LoginPage(page)
        login_page.login(user_email, password)

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