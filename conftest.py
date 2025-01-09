import pytest
from pathlib import Path
from playwright.sync_api import Browser, Page
from pages.login import LoginPage

# Constants
STAGE_USER_EMAIL = "dkononenko1994@ukr.net"
STAGE_USER_PASSWORD = "123456"
STAGE_TEST_USER_EMAIL_PASS = "m2m.test.auto@gmail.com"
LOCALE = 'uk-UA'
TIMEZONE_ID = 'Europe/Kiev'
TRACE_DIR = "reports/trace"
AUTH_STORAGE_PATH = Path("utils/.auth/storage_state.json")
NEW_TEST_USER_STAGE_PATH = Path("utils/.auth/new_test_user_stage.json")


def start_tracing(context, test_name=None):
    """Start tracing for the context."""
    context.tracing.start(screenshots=True, snapshots=True)
    if test_name:
        return f"{TRACE_DIR}/{test_name}_trace.zip"
    return None


def stop_tracing(context, trace_file_path=None):
    """Stop tracing and save if trace_file_path is provided."""
    if trace_file_path:
        context.tracing.stop(path=trace_file_path)
    else:
        context.tracing.stop()


def close_context(context, page):
    """Close the page and context."""
    page.close()
    context.close()


@pytest.fixture(scope="function")
def page(browser: Browser, request):
    """Fixture for a clean session."""
    context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID)
    page = context.new_page()
    trace_file_path = start_tracing(context, request.node.name)

    yield page

    if request.node.rep_call.failed:
        stop_tracing(context, trace_file_path)
    else:
        stop_tracing(context)

    close_context(context, page)


@pytest.fixture(scope="function")
def gmail(browser: Browser):
    """Fixture for a clean Gmail session."""
    context = browser.new_context(
        slow_mo=2000,
        args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"],
        ignore_default_args=['--disable-component-extensions-with-background-pages']
    )
    page = context.new_page()

    yield page

    close_context(context, page)


@pytest.fixture(scope="function")
def authenticated_page(browser: Browser, request):
    """Fixture for a session with saved authentication state."""
    if not AUTH_STORAGE_PATH.exists():
        context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID)
        page = context.new_page()
        login_page = LoginPage(page)
        login_page.login(STAGE_USER_EMAIL, STAGE_USER_PASSWORD)
        login_page.acsept_btn.click()

        if login_page.is_logged_in():
            context.storage_state(path=str(AUTH_STORAGE_PATH))
        else:
            print("Authorization failed. State will not be saved.")

        close_context(context, page)

    context = browser.new_context(storage_state=str(AUTH_STORAGE_PATH), locale=LOCALE, timezone_id=TIMEZONE_ID)
    page = context.new_page()
    trace_file_path = start_tracing(context, request.node.name)

    yield page

    if request.node.rep_call.failed:
        stop_tracing(context, trace_file_path)
    else:
        stop_tracing(context)

    close_context(context, page)


@pytest.fixture(scope="session")
def login_user(browser: Browser):
    """Fixture for logging in a user."""
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.login(STAGE_USER_EMAIL, STAGE_USER_PASSWORD)
    login_page.acsept_btn.click()

    yield page

    close_context(context, page)


@pytest.fixture(scope="function")
def auth_new_test_user(browser: Browser, request):
    """Fixture for a session with saved state for a new test user."""
    if not NEW_TEST_USER_STAGE_PATH.exists():
        context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID)
        page = context.new_page()
        login_page = LoginPage(page)
        login_page.login(STAGE_TEST_USER_EMAIL_PASS, STAGE_TEST_USER_EMAIL_PASS)
        login_page.acsept_btn.click()

        if login_page.is_logged_in():
            context.storage_state(path=str(NEW_TEST_USER_STAGE_PATH))
        else:
            print("Authorization failed. State will not be saved.")

        close_context(context, page)

    context = browser.new_context(storage_state=str(NEW_TEST_USER_STAGE_PATH), locale=LOCALE, timezone_id=TIMEZONE_ID)
    page = context.new_page()
    trace_file_path = start_tracing(context, request.node.name)

    yield page

    if request.node.rep_call.failed:
        stop_tracing(context, trace_file_path)
    else:
        stop_tracing(context)

    close_context(context, page)
