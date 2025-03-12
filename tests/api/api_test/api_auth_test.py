import pytest
import os
from pytest import mark
from pages.api.auth_api import AuthAPI
from playwright.sync_api import expect
from faker import Faker


# Fixtures ---------------------------------------------------------------------

@pytest.fixture(scope="function")
def precondition_login(api_context, test_data):
    """Фікстура для отримання токена."""
    auth_api = AuthAPI(api_context, None)
    response = auth_api.sign_in(
        email="m2m.test.auto+test_auth@gmail.com",
        password="m2m.test.auto+test_auth@gmail.com"
    )
    expect(response).to_be_ok()
    test_data['refreshToken'] = response.json()["refreshToken"]
    test_data['token'] = response.json().get("token")
    
    yield


@pytest.fixture(scope="function")
def precondition_sign_up(api_context, test_data):
    """Тест на реєстрацію."""
    auth_api = AuthAPI(api_context, token=None)
    fake = Faker()
    test_data["user_email"] = fake.email()
    response = auth_api.sign_up(
        email=test_data["user_email"],
        password="123456",
        language="UKRAINIAN"
    )
    expect(response).to_be_ok()
    
    yield


@pytest.fixture(scope="function")
def token_auth(api_context):
    """Отримує токен авторизації для API."""
    user_email = "m2m.test.auto+test_auth@gmail.com"
    user_password = "m2m.test.auto+test_auth@gmail.com"

    response = api_context.post("/api/login", data={"email": user_email, "password": user_password})
    expect(response).to_be_ok()
    
    json_data = response.json()
    return json_data.get("token")

# Tests ------------------------------------------------------------------------


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt481')
def test_get_profile(api_context, token_auth):
    """Тест на отримання профілю користувача."""
    auth_api = AuthAPI(api_context, token_auth)
    response = auth_api.get_profile()
    expect(response).to_be_ok()
    assert response.json()["email"] == "m2m.test.auto+test_auth@gmail.com"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt482')
def test_update_profile(api_context, token_auth):
    """Тест на оновлення профілю користувача."""
    auth_api = AuthAPI(api_context, token_auth)
    response = auth_api.update_profile(
        firstName="Test"
    )
    expect(response).to_be_ok()
    assert response.json()["firstName"] == "Test"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt811')
def test_login_as_child_user(api_context, token, test_data, create_and_del_user_by_accaunt):
    """Тест на вхід як дитина."""
    auth_api = AuthAPI(api_context, token)
    response = auth_api.login_as_child_user(
        user_id=test_data["user_id"],
    )
    expect(response).to_be_ok()
    assert response.json()['user']['email'] == test_data["user_email"]


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt812')
def test_verify_access_token(api_context, token_auth):
    """Тест на перевірку доступу."""
    auth_api = AuthAPI(api_context, token_auth)
    response = auth_api.verify_access_token()
    expect(response).to_be_ok()
    assert response.json()["message"] == "Token valid"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt813')
def test_refresh_access_token(api_context, test_data, precondition_login):
    """Тест на оновлення доступу."""
    auth_api = AuthAPI(api_context, token=None)
    response = auth_api.refresh_access_token(
        refreshToken=test_data["refreshToken"]
    )
    expect(response).to_be_ok()
    assert response.json()["token"] != ''


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt814')
def test_send_an_email_to_reset_password(api_context):
    """Тест на відправлення листа для скидання пароля."""
    auth_api = AuthAPI(api_context, token=None)
    response = auth_api.send_an_email_to_reset_password(
        resetEmail="m2m.test.auto+test_auth@gmail.com"
    )
    expect(response).to_be_ok()
    assert response.json()["message"] == "email.sent"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt815')
@mark.skip("Токен приходить на пошту, потрібно доробити тест із доступом до пошти ")
def test_password_reset_confirmation(api_context, test_data, precondition_login):
    """Тест на підтвердження скидання пароля."""
    auth_api = AuthAPI(api_context, token=None)
    response = auth_api.password_reset_confirmation(
        token=test_data["token"],
        newPassword=os.getenv("SELFREG_USER_PASSWORD")
    )
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt816')
def test_sign_up(api_context):
    """Тест на реєстрацію."""
    auth_api = AuthAPI(api_context, token=None)
    fake = Faker()
    response = auth_api.sign_up(
        email=fake.email(),
        password="123456",
        language="UKRAINIAN"
    )
    expect(response).to_be_ok()
    assert response.json()["message"] == "email.sent"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1719')
@mark.skip("Токен приходить на пошту, потрібно доробити тест із доступом до пошти ")
def test_activate_user_after_registration(api_context, test_data):
    """Тест на активацію користувача після реєстрації."""
    auth_api = AuthAPI(api_context, token=None)
    response = auth_api.activate_user_after_registration(
        token=test_data["token"]
    )
    expect(response).to_be_ok()
    assert response.json()["message"] == "user.activated"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt817')
def test_refresh_confirmation_link(api_context, test_data, precondition_sign_up):
    """Тест на оновлення посилання підтвердження."""
    auth_api = AuthAPI(api_context, token=None)
    response = auth_api.refresh_confirmation_link(
        email=test_data["user_email"]
    )
    expect(response).to_be_ok()
    assert response.json()["message"] == "email.sent"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt818')
def test_change_password(api_context, token_auth):
    """Тест на зміну пароля."""
    auth_api = AuthAPI(api_context, token_auth)
    response = auth_api.change_password(
        oldPassword="m2m.test.auto+test_auth@gmail.com",
        newPassword="m2m.test.auto+test_auth@gmail.com"
    )
    expect(response).to_be_ok()
    

@mark.api
@mark.smoke
@mark.testomatio('@Tttttt810')
def test_send_email_to_change_email_address(api_context, token_auth):
    """Тест на відправлення листа для зміни адреси електронної пошти."""
    auth_api = AuthAPI(api_context, token_auth)
    response = auth_api.send_email_to_change_email_address(
        newEmail="m2m.test.auto+test_auth@gmail.com"
    )
    expect(response).to_be_ok()
    print(response.json())
    assert response.json()["message"] == "email.sent"


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1721')
@mark.skip("Токен приходить на пошту, потрібно доробити тест із доступом до пошти ")
def test_confirmation_of_change_email(api_context, token_auth):
    """Тест на підтвердження зміни адреси електронної пошти."""
    auth_api = AuthAPI(api_context, token_auth)
    response = auth_api.confirmation_of_change_email(
        token="token"
    )
    expect(response).to_be_ok()
    assert response.json()["message"] == "email.changed"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt819')
def test_sign_in(api_context):
    """Тест на вхід."""
    auth_api = AuthAPI(api_context, token=None)
    response = auth_api.sign_in(
        email="m2m.test.auto+test_auth@gmail.com",
        password="m2m.test.auto+test_auth@gmail.com"
    )
    expect(response).to_be_ok()
    assert response.json()['user']["email"] == "m2m.test.auto+test_auth@gmail.com"
