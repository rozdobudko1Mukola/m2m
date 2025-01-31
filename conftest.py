import pytest
import os
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser, Page
from pages.login import LoginPage

LOCALE = 'uk-UA'
TIMEZONE_ID = 'Europe/Kiev'
TRACE_DIR = "reports/trace"


def get_auth_storage_path(base_url, user_type):
    """Отримати шлях до файлу збереження сесії для кожного типу користувача."""
    if "staging" in base_url:
        return Path(f"utils/.auth/storage_state_staging_{user_type}.json")
    elif "my.m2m" in base_url:
        return Path(f"utils/.auth/storage_state_prod_{user_type}.json")
    elif "dev" in base_url:
        return Path(f"utils/.auth/storage_state_dev_{user_type}.json")
    else:
        raise ValueError("Unknown environment")


def start_tracing(context, test_name=None):
    """Start tracing for the context."""
    context.tracing.start(screenshots=True, snapshots=True)
    if test_name:
        short_test_name = test_name.split("[")[0]
        return f"{TRACE_DIR}/{short_test_name}_trace.zip"
    return None


def stop_tracing(context, trace_file_path=None):
    """Stop tracing and save if trace_file_path is provided."""
    if trace_file_path:
        context.tracing.stop(path=trace_file_path)
    else:
        context.tracing.stop()


def close_context(context, page):
    """Закрити сторінку та контекст."""
    page.close()
    context.close()


def load_env(env):
    """Завантаження `.env` файлу для вибраного середовища."""
    env_file = f".env.{env}"
    if not Path(env_file).exists():
        raise FileNotFoundError(f"Environment file '{env_file}' not found")
    load_dotenv(env_file)


@pytest.fixture(scope="session", autouse=True)
def setup_env(pytestconfig):
    """Завантаження конфігурації середовища перед запуском тестів."""
    env = pytestconfig.getoption("--env") or "staging"
    load_env(env)
 
# Environment setup fixture
@pytest.fixture()
def client_user(browser: Browser, request):
    """Використовується для створення авторизації для конкретного типу користувача."""
    user_type = "CLIENT"
    base_url = os.getenv("BASE_URL")
    user_email = os.getenv(f"{user_type}_USER_EMAIL")
    user_password = os.getenv(f"{user_type}_USER_PASSWORD")

    auth_storage_path = get_auth_storage_path(base_url, user_type.lower())

    # Якщо сесія не існує, створити її
    if not auth_storage_path.exists():
        context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
        page = context.new_page()

        # Авторизація
        login_page = LoginPage(page)
        if login_page.sucsefull_login(user_email, user_password):
            context.storage_state(path=str(auth_storage_path))
        else:
            raise Exception(f"Авторизація {user_type} не виконана. Сесія не збережена.")

        page.close()
        context.close()

    # Використання існуючої сесії
    context = browser.new_context(
        storage_state=str(auth_storage_path),
        locale=LOCALE,
        timezone_id=TIMEZONE_ID,
        base_url=base_url,
    )
    page = context.new_page()
    trace_file_path = start_tracing(context, request.node.name)

    yield page  # Повертаємо об'єкт Page

    # Зупиняємо трасування та закриваємо контекст
    if request.node.rep_call.failed:
        stop_tracing(context, trace_file_path)
    else:
        stop_tracing(context)

    page.close()
    context.close()


@pytest.fixture()
def admin_user(browser: Browser, request):
    """Використовується для створення авторизації для конкретного типу користувача."""
    user_type = "ADMIN"
    base_url = os.getenv("BASE_URL")
    user_email = os.getenv(f"{user_type}_USER_EMAIL")
    user_password = os.getenv(f"{user_type}_USER_PASSWORD")

    auth_storage_path = get_auth_storage_path(base_url, user_type.lower())

    # Якщо сесія не існує, створити її
    if not auth_storage_path.exists():
        context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
        page = context.new_page()

        # Авторизація
        login_page = LoginPage(page)
        if login_page.sucsefull_login(user_email, user_password):
            context.storage_state(path=str(auth_storage_path))
        else:
            raise Exception(f"Авторизація {user_type} не виконана. Сесія не збережена.")

        page.close()
        context.close()

    # Використання існуючої сесії
    context = browser.new_context(
        storage_state=str(auth_storage_path),
        locale=LOCALE,
        timezone_id=TIMEZONE_ID,
        base_url=base_url,
    )
    page = context.new_page()
    trace_file_path = start_tracing(context, request.node.name)

    yield page  # Повертаємо об'єкт Page

    # Зупиняємо трасування та закриваємо контекст
    if request.node.rep_call.failed:
        stop_tracing(context, trace_file_path)
    else:
        stop_tracing(context)

    page.close()
    context.close()


@pytest.fixture()
def selfreg_user(browser: Browser, request):
    """Використовується для створення авторизації для конкретного типу користувача."""
    user_type = "SELFREG"
    base_url = os.getenv("BASE_URL")
    user_email = os.getenv(f"{user_type}_USER_EMAIL")
    user_password = os.getenv(f"{user_type}_USER_PASSWORD")

    auth_storage_path = get_auth_storage_path(base_url, user_type.lower())

    # Якщо сесія не існує, створити її
    if not auth_storage_path.exists():
        context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
        page = context.new_page()

        # Авторизація
        login_page = LoginPage(page)
        if login_page.sucsefull_login(user_email, user_password):
            context.storage_state(path=str(auth_storage_path))
        else:
            raise Exception(f"Авторизація {user_type} не виконана. Сесія не збережена.")

        page.close()
        context.close()

    # Використання існуючої сесії
    context = browser.new_context(
        storage_state=str(auth_storage_path),
        locale=LOCALE,
        timezone_id=TIMEZONE_ID,
        base_url=base_url,
    )
    page = context.new_page()
    trace_file_path = start_tracing(context, request.node.name)

    yield page  # Повертаємо об'єкт Page

    # Зупиняємо трасування та закриваємо контекст
    if request.node.rep_call.failed:
        stop_tracing(context, trace_file_path)
    else:
        stop_tracing(context)

    page.close()
    context.close()



@pytest.fixture()
def freebill_user(browser: Browser, request):
    """Використовується для створення авторизації для конкретного типу користувача."""
    user_type = "FREEBILL"
    base_url = os.getenv("BASE_URL")
    user_email = os.getenv(f"{user_type}_USER_EMAIL")
    user_password = os.getenv(f"{user_type}_USER_PASSWORD")

    auth_storage_path = get_auth_storage_path(base_url, user_type.lower())

    # Якщо сесія не існує, створити її
    if not auth_storage_path.exists():
        context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
        page = context.new_page()

        # Авторизація
        login_page = LoginPage(page)
        if login_page.sucsefull_login(user_email, user_password):
            context.storage_state(path=str(auth_storage_path))
        else:
            raise Exception(f"Авторизація {user_type} не виконана. Сесія не збережена.")

        page.close()
        context.close()

    # Використання існуючої сесії
    context = browser.new_context(
        storage_state=str(auth_storage_path),
        locale=LOCALE,
        timezone_id=TIMEZONE_ID,
        base_url=base_url,
    )
    page = context.new_page()
    trace_file_path = start_tracing(context, request.node.name)

    yield page  # Повертаємо об'єкт Page

    # Зупиняємо трасування та закриваємо контекст
    if request.node.rep_call.failed:
        stop_tracing(context, trace_file_path)
    else:
        stop_tracing(context)

    page.close()
    context.close()


@pytest.fixture()
def page(browser: Browser, request):
    """Fixture for a clean session."""
    base_url = os.getenv("BASE_URL")
    context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
    page = context.new_page()
    trace_file_path = start_tracing(context, request.node.name)

    yield page  # Повертаємо об'єкт Page

    # Зупиняємо трасування та закриваємо контекст
    if request.node.rep_call.failed:
        stop_tracing(context, trace_file_path)
    else:
        stop_tracing(context)

    page.close()
    context.close()


def pytest_addoption(parser):
    """Додавання параметра --env для вибору середовища."""
    parser.addoption(
        "--env",
        action="store",
        default="staging",
        help="Вибір середовища для тестів (prod, staging, dev)",
    )