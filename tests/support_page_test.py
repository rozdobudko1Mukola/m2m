import pytest
from pytest import mark
from pages.support_page import SupportPage
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


login_page_url = "/login"
profile_url = "/user"
support_url = "/support"
docs_url = "https://docs.m2m.eu/uk/"
forum_url = "https://forum.m2m.eu/"

# """Перевірка контактної інформації на сторінці підтримки."""
expected_dict = {
    'Форум': 'forum.m2m.eu',
    'Документація': 'docs.m2m.eu',
    'Email:': 'support@m2m.eu',
    'Телефон 1': '+380 (44) 323-22-44',
    'Телефон 2': '+380 (68) 323-22-44',
    'Телефон 3': '+380 (95) 323-22-44',
    'Телефон 4': '+380 (63) 323-22-44',
    'Для зв\'язку з технічною підтримкою натисніть, будь ласка "9"': ''
}

@mark.testomatio('@Ttttt1578')
def test_open_profile_page(client_user: Page):
    """||M2M-1582|| Перейти на сторінку 'Профіль користувача"""
    support_page = SupportPage(client_user)

    support_page.open_profile_page()
    expect(client_user).to_have_url(profile_url)


@mark.testomatio('@Ttttt1581')
def test_open_doc_page(client_user: Page):
    """||M2M-1581|| Переглянути документацію системи"""
    support_page = SupportPage(client_user)

    with client_user.expect_popup() as popup_info:
        support_page.open_docs_link()
    docs_tab = popup_info.value
    expect(docs_tab).to_have_url(docs_url)
    docs_tab.close()  # Закриваємо вкладку документації


@mark.testomatio('@Ttttt1579')
def test_useful_links(client_user: Page):
    """||M2M-1579|| Перевірка переходу за посиланнями в розділі 'Користні посилання'"""
    support_page = SupportPage(client_user)

    # Відслідковуємо нову вкладку для форуму
    with client_user.expect_popup() as popup_info:
        support_page.open_forum_link()
    forum_tab = popup_info.value
    expect(forum_tab).to_have_url(forum_url)
    forum_tab.close()  # Закриваємо вкладку форуму

    # Відслідковуємо нову вкладку для документації
    with client_user.expect_popup() as popup_info:
        support_page.open_docs_link()
    docs_tab = popup_info.value
    expect(docs_tab).to_have_url(docs_url)
    docs_tab.close()  # Закриваємо вкладку документації


@mark.testomatio('@Ttttt1580')
def test_contact_info(client_user: Page):
    """ ||M2M-1578|| / ||M2M-1580|| Переглянути сторінку підтримки / Переглянути контантну інформацію"""
    support_page = SupportPage(client_user)

    # Отримуємо контактну інформацію
    contact_info = support_page.get_contact_info()

    # Перевіряємо, чи дані з contact_info відповідають expected_dict
    for key, expected_value in expected_dict.items():
        actual_value = contact_info.get(key, "")
        assert actual_value == expected_value, f"Невірне значення для '{key}': очікувалось '{expected_value}', але отримано '{actual_value}'"


@mark.testomatio('@Ttttt1583')
def test_click_exit_button(client_user: Page):
    """||M2M-1583|| Натиснути на кнопку 'Вихід' в бічному меню"""
    support_page = SupportPage(client_user)
    support_page.click_exit_button()

    expect(client_user).to_have_url(login_page_url)