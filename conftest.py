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
# @pytest.fixture(scope="function")
# def auth_new_test_user(browser: Browser):
#     new_test_user_stage_path = Path("utils/.auth/new_test_user_stage.json")

#     # Якщо файл стану не існує, створюємо його
#     if not new_test_user_stage_path.exists():
#         context = browser.new_context()

#         page = context.new_page()

#         login_page = LoginPage(page)
#         login_page.login(stage_test_user_email_pass, stage_test_user_email_pass)
#         login_page.acsept_btn.click()

#         # Зберігаємо стан
#         context.storage_state(path=str(new_test_user_stage_path))

#         page.close()
#         context.close()
    
#     # Завантажуємо збережений стан
#     context = browser.new_context(storage_state=str(new_test_user_stage_path))
#     page = context.new_page()
#     yield page
#     page.close()
#     context.close()


@pytest.fixture(scope="function")
def auth_new_test_user(browser: Browser, request):
    # Шлях до файлу збереженого стану
    new_test_user_stage_path = Path("utils/.auth/new_test_user_stage.json")

    # Якщо файл стану не існує, створюємо його
    if not new_test_user_stage_path.exists():
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.login(stage_test_user_email_pass, stage_test_user_email_pass)  # Замініть на реальний пароль
        login_page.acsept_btn.click()

        # Перевіряємо, чи користувач авторизувався успішно
        if login_page.is_logged_in():
            # Зберігаємо стан у файл
            context.storage_state(path=str(new_test_user_stage_path))
        else:
            print("Авторизація не вдалася. Стан не буде збережено.")

        page.close()
        context.close()

    # Завантажуємо збережений стан
    context = browser.new_context(storage_state=str(new_test_user_stage_path))

    # Починаємо трасування
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()

    # Передаємо сторінку тестам
    yield page

    # Перевіряємо статус тесту після його виконання
    if request.node.rep_call.failed:
        # Якщо тест не пройшов, зберігаємо трасування
        test_name = request.node.name  # Отримуємо ім'я тесту
        trace_file_path = f"reports/trace/{test_name}_trace.zip"
        context.tracing.stop(path=trace_file_path)  # Зберігаємо трасування тільки для тестів, які не пройшли
    else:
        # Якщо тест пройшов успішно, зупиняємо трасування без збереження
        context.tracing.stop()

    # Закриваємо сторінку та контекст після виконання тесту
    page.close()
    context.close()


