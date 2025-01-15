import pytest
from pages.analytics_page import AnalyticsPage
from playwright.sync_api import Page, expect


# M2M-347 Open the Analytics page
def test_check_analytics_text_m2m_347(authenticated_page: Page):
    analytics_page = AnalyticsPage(authenticated_page)
    actual_text = analytics_page.check_analytics_text()
    expected_text = (
        "Сьогодні Вчора Тиждень Стан підключення Дані онлайн "
        "Графік за часом зупинок Графік за пробігом Графік за максимальною швидкістю"
    )
    assert actual_text == expected_text


# M2M-348 View data on objects for Today/Yesterday/Week
def test_view_data_on_objects_m2m_348(authenticated_page: Page):
    analytics_page = AnalyticsPage(authenticated_page)
    analytics_page.today_tab.click()
    expect(analytics_page.today_tab).to_have_css("color", "rgb(38, 180, 254)")
    analytics_page.yesterday_tab.click()
    expect(analytics_page.yesterday_tab).to_have_css("color", "rgb(38, 180, 254)")
    analytics_page.week_tab.click()
    expect(analytics_page.week_tab).to_have_css("color", "rgb(38, 180, 254)")


@pytest.mark.skip("This test is not implemented")
# M2M-789 View the connection status on the diagram
def test_view_connection_status_m2m_789(authenticated_page: Page):
    pass


# M2M-773 Create a custom list of objects by stop time
def test_list_of_objects_by_stop_m2m_773(authenticated_page: Page):
    analytics_page = AnalyticsPage(authenticated_page)
    expected_result = analytics_page.add_device_to_diagram()
    authenticated_page.wait_for_timeout(1000)
    actual_result = analytics_page.get_device_from_diagram()
    assert actual_result == expected_result
