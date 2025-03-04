import pytest
import os
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import APIRequestContext, Playwright, expect
from pages.api.devices_api import DeviceAPI


# Завантаження змінних середовища
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

@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext:
    """Створює Playwright API контекст з базовим URL."""
    base_url = os.getenv("BASE_URL")
    request_context = playwright.request.new_context(base_url=base_url)
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def token(api_context: APIRequestContext):
    """Отримує токен авторизації для API."""
    user_email = os.getenv("SELFREG_USER_EMAIL")
    user_password = os.getenv("SELFREG_USER_PASSWORD")

    response = api_context.post("/api/login", data={"email": user_email, "password": user_password})
    expect(response).to_be_ok()
    
    json_data = response.json()
    return json_data.get("token")


@pytest.fixture(scope="session")
def admin_token(api_context: APIRequestContext):
    """Отримує токен адміна для авторизації для API."""
    user_email = os.getenv("ADMIN_USER_EMAIL")
    user_password = os.getenv("ADMIN_USER_PASSWORD")

    response = api_context.post("/api/login", data={"email": user_email, "password": user_password})
    expect(response).to_be_ok()
    
    json_data = response.json()
    return json_data.get("token")

# @pytest.fixture(scope="session")
# def device_api(api_context, token):
#     """Повертає об'єкт DeviceAPI із залогіненим користувачем."""
#     return DeviceAPI(api_context, token)