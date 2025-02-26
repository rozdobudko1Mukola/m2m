import pytest
from pytest import mark
from pages.api.users_api import UsersAPI
from playwright.sync_api import expect
from faker import Faker


# Fixtures for the test UsersAPI
@pytest.fixture(scope="function")
def test_data():
    """Фікстура для збереження даних між тестами."""
    return {}


@pytest.fixture(scope="function")
def del_user_postcondition(api_context, token, test_data):
    """Фікстура видалення після тесту."""

    yield
    user_api = UsersAPI(api_context, token)

    response = user_api.remove_child_user(test_data["user_id"])
    expect(response).to_be_ok()


@pytest.fixture(scope="function")
def create_user_precondition(api_context, token, test_data):
    """Фікстура для створення користувача перед тестом."""
    fake = Faker()
    user_api = UsersAPI(api_context, token)

    response = user_api.create_new_user(
        email=fake.email(),
        password="123456",
        language="UKRAINIAN"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["user_id"] = json_data.get("id")

    yield


@pytest.fixture(scope="function")
def create_and_del_managed_id(api_context, token, test_data):
    """Фікстура для створення користувача перед тестом та видалення після тесту."""
    fake = Faker()
    user_api = UsersAPI(api_context, token)

    response = user_api.create_new_user(
        email=fake.email(),
        password="123456",
        language="UKRAINIAN"
    )
    expect(response).to_be_ok()

    json_data = response.json()
    test_data["managed_id"] = json_data.get("id")

    yield

    response = user_api.remove_child_user(test_data["managed_id"])
    expect(response).to_be_ok()
    test_data.pop("managed_id", None)


# Tests for the API Users  
@mark.smoke
@mark.api
@mark.testomatio('')
def test_get_child_user_by_id(api_context, token, test_data, create_and_del_user_by_accaunt):
    """Тестуємо отримання дитячого користувача по id"""
    user_api = UsersAPI(api_context, token)
    response = user_api.get_child_user_by_id(test_data["user_id"])
    expect(response).to_be_ok()
    assert response.json()["id"] == test_data["user_id"]


@mark.smoke
@mark.api
@mark.testomatio('')
def test_update_child_user(api_context, token, test_data, create_and_del_user_by_accaunt):
    """Тестуємо оновлення дитячого користувача"""
    user_api = UsersAPI(api_context, token)
    response = user_api.update_child_user(test_data["user_id"], firstName="test")
    expect(response).to_be_ok()
    assert response.json()["firstName"] == "test"


@mark.smoke
@mark.api
@mark.testomatio('')
def test_remove_child_user(api_context, token, test_data, create_user_precondition):
    """Тестуємо видалення дитячого користувача"""
    user_api = UsersAPI(api_context, token)
    response = user_api.remove_child_user(test_data["user_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('')
def test_retrieve_list_of_child_users_without_pagination(api_context, token, test_data, create_and_del_user_by_accaunt):
    """Тестуємо отримання списку дитячих користувачів без пагінації"""
    user_api = UsersAPI(api_context, token)
    response = user_api.retrieve_list_of_child_users_without_pagination()
    expect(response).to_be_ok()
    assert response.json()[0]["id"] == test_data["user_id"]


@mark.smoke
@mark.api
@mark.testomatio('')
def test_create_new_user(api_context, token, test_data, del_user_postcondition):
    """Тестуємо створення нового користувача"""
    fake = Faker()
    user_api = UsersAPI(api_context, token)

    response = user_api.create_new_user(
        email=fake.email(),
        password="123456",
        language="UKRAINIAN"
    )
    expect(response).to_be_ok()
    json_data = response.json()
    test_data["user_id"] = json_data.get("id")


@mark.smoke
@mark.api
@mark.testomatio('')
def test_change_the_child_user_password(api_context, token, test_data, create_and_del_user_by_accaunt):
    """Тестуємо зміну пароля дитячого користувача"""
    user_api = UsersAPI(api_context, token)
    response = user_api.change_the_child_user_password(test_data["user_id"], password="123123")
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('')
def test_send_invite(api_context, token, test_data, create_and_del_user_by_accaunt):
    """Тестуємо відправлення запрошення користувачу"""
    user_api = UsersAPI(api_context, token)
    response = user_api.send_invite(test_data["user_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('')
def test_change_email(api_context, token, test_data, create_and_del_user_by_accaunt):
    """Тестуємо зміну email користувача"""
    user_api = UsersAPI(api_context, token)
    response = user_api.change_email(test_data["user_id"], email="test@test.com")
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('')
def test_get_child_user_permissions_for_another_child(api_context, token, test_data, create_and_del_user_by_accaunt, create_and_del_managed_id):
    """Тестуємо отримання дитячого користувача по id"""
    user_api = UsersAPI(api_context, token)
    response = user_api.get_child_user_permissions_for_another_child(test_data["user_id"], managed_id=test_data["managed_id"])
    expect(response).to_be_ok()


@mark.smoke
@mark.api
@mark.testomatio('')
def test_grant_permissions_to_child_user_for_another_child(api_context, token, test_data, create_and_del_user_by_accaunt, create_and_del_managed_id):
    """Тестуємо надання прав дитячому користувачу для іншого дитячого користувача"""
    user_api = UsersAPI(api_context, token)
    response = user_api.grant_permissions_to_child_user_for_another_child(test_data["user_id"], managed_id=test_data["managed_id"], permission="VIEW_ELEMENT", state="true")
    expect(response).to_be_ok()
    assert response.json().get("VIEW_ELEMENT") is True


@mark.smoke
@mark.api
@mark.testomatio('')
def test_retrieve_list_of_child_users_with_pagination(api_context, token, test_data, create_and_del_user_by_accaunt):
    """Тестуємо отримання списку дитячих користувачів з пагінацією"""
    user_api = UsersAPI(api_context, token)
    response = user_api.retrieve_list_of_child_users_with_pagination(page=1, per_page=10)
    expect(response).to_be_ok()
    assert response.json()["items"][0]["id"] == test_data["user_id"]