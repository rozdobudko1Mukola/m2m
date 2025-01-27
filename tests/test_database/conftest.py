import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from pages.login import LoginPage


STAGE_USER_FREE_BILL_PLAN = "m2m.test.auto+freebill@gmail.com"
LOCALE = 'uk-UA'
TIMEZONE_ID = 'Europe/Kiev'
TRACE_DIR = "reports/trace"


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

@pytest.fixture(scope="function")
def login_free_paln_user(browser: Browser, request, base_url):
    """Fixture for logging in a user."""
    context = browser.new_context(locale=LOCALE, timezone_id=TIMEZONE_ID, base_url=base_url)
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.login(STAGE_USER_FREE_BILL_PLAN, STAGE_USER_FREE_BILL_PLAN)
    login_page.accept_btn.click()
    page.wait_for_timeout(1000)

    trace_file_path = start_tracing(context, request.node.name)

    yield page

    stop_tracing(context, trace_file_path if request.node.rep_call.failed else None)

    page.close()
    context.close() 