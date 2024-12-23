import pytest
from pages.support_page import SupportPage
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


login_page_url = "https://staging.m2m.eu/login"
profile_url = "https://staging.m2m.eu/user"
support_url = "https://staging.m2m.eu/support"
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


# M2M-1583 Натиснути на кнопку "Вихід" в бічному меню.
def test_click_exit_button(authenticated_page: Page):
    support_page = SupportPage(authenticated_page)
    support_page.click_exit_button()

    expect(authenticated_page).to_have_url(login_page_url)


# M2M-1582 Перейти на сторінку "Профіль користувача"
def test_open_profile_page(authenticated_page: Page):
    support_page = SupportPage(authenticated_page)

    support_page.open_profile_page()
    expect(authenticated_page).to_have_url(profile_url)


#M2M-1581 Переглянути документацію системи
def test_open_doc_page(authenticated_page: Page):
    support_page = SupportPage(authenticated_page)

    with authenticated_page.expect_popup() as popup_info:
        support_page.open_docs_link()
    docs_tab = popup_info.value
    expect(docs_tab).to_have_url(docs_url)
    docs_tab.close()  # Закриваємо вкладку документації


# M2M-1579 Перейти за посиланнями в розділі "Користні посилання"
def test_useful_links(authenticated_page: Page):
    support_page = SupportPage(authenticated_page)

    # Відслідковуємо нову вкладку для форуму
    with authenticated_page.expect_popup() as popup_info:
        support_page.open_forum_link()
    forum_tab = popup_info.value
    expect(forum_tab).to_have_url(forum_url)
    forum_tab.close()  # Закриваємо вкладку форуму

    # Відслідковуємо нову вкладку для документації
    with authenticated_page.expect_popup() as popup_info:
        support_page.open_docs_link()
    docs_tab = popup_info.value
    expect(docs_tab).to_have_url(docs_url)
    docs_tab.close()  # Закриваємо вкладку документації


# M2M-1578 Переглянути сторінку підтримки
# M2M-1580 Переглянути контантну інформацію
def test_contact_info(authenticated_page: Page):
    support_page = SupportPage(authenticated_page)

    # Отримуємо контактну інформацію
    contact_info = support_page.get_contact_info()

    # Перевіряємо, чи дані з contact_info відповідають expected_dict
    for key, expected_value in expected_dict.items():
        actual_value = contact_info.get(key, "")
        assert actual_value == expected_value, f"Невірне значення для '{key}': очікувалось '{expected_value}', але отримано '{actual_value}'"