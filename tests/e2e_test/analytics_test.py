# need to rewrite this file to use the new AnalyticsPage class
# This file contains tests for the Analytics page functionality in a web application.


# import pytest
# from pytest import mark
# from pages.e2e.analytics_page import AnalyticsPage
# from playwright.sync_api import Page, expect


# # M2M-347 Open the Analytics page
# @mark.testomatio('@Tttttt347')
# def test_check_analytics_text_m2m_347(client_user: Page):
#     analytics_page = AnalyticsPage(client_user)
#     actual_text = analytics_page.check_analytics_text()
#     expected_text = (
#         "Сьогодні Вчора Тиждень Стан підключення Дані онлайн "
#         "Графік за часом зупинок Графік за пробігом Графік за максимальною швидкістю"
#     )
#     assert actual_text == expected_text


# # M2M-348 View data on objects for Today/Yesterday/Week
# @mark.testomatio('@Tttttt348')
# def test_view_data_on_objects_m2m_348(client_user: Page):
#     analytics_page = AnalyticsPage(client_user)
#     for tab in [analytics_page.today_tab, analytics_page.yesterday_tab, analytics_page.week_tab]:
#         tab.click()
#         expect(tab).to_have_css("color", "rgb(38, 180, 254)")


# @pytest.mark.skip("This test is not implemented")
# # M2M-789 View the connection status on the diagram
# def test_view_connection_status_m2m_789(client_user: Page):
#     pass


# # M2M-773 Create a custom list of objects by stop time
# @mark.testomatio('@Tttttt773')
# def test_list_of_objects_by_stop_m2m_773(client_user: Page, grafic=0):
#     analytics_page = AnalyticsPage(client_user)
#     expected_result = analytics_page.add_device_to_diagram(grafic)
#     client_user.wait_for_timeout(1000)
#     actual_result = analytics_page.get_device_from_diagram()
#     assert actual_result == expected_result


# # M2M-1597 Change the objects that appear in the diagram by stop time
# @pytest.mark.skip("This test is not implemented")
# def test_change_objects_in_diagram_by_stop_time_m2m_1597(client_user: Page):
#     pass


# # M2M-774 Create a custom list of objects by mileage
# @mark.testomatio('@Tttttt774')
# def test_list_of_objects_by_mileage_m2m_774(client_user, grafic=1):
#     analytics_page = AnalyticsPage(client_user)
#     expected_result = analytics_page.add_device_to_diagram(grafic)
#     client_user.wait_for_timeout(1000)
#     actual_result = analytics_page.get_device_from_diagram()
#     assert actual_result == expected_result


# # M2M-1599 Change the objects that appear in the diagram by maximum speed
# @pytest.mark.skip("This test is not implemented")
# def test_change_objects_in_diagram_by_max_speed_m2m_1599(client_user: Page):
#     pass


# # M2M-775 Generate a custom diagram of objects by maximum speed
# @mark.testomatio('@Tttttt775')
# def test_list_of_objects_by_speed_m2m_775(client_user, grafic=2):
#     analytics_page = AnalyticsPage(client_user)
#     expected_result = analytics_page.add_device_to_diagram(grafic)
#     client_user.wait_for_timeout(1000)
#     actual_result = analytics_page.get_device_from_diagram()
#     assert actual_result == expected_result


# # M2M-776 Search for an object in the "Select up to 10 objects to display..." window.
# @mark.testomatio('@Tttttt776')
# def test_valid_search_object_m2m_776(client_user: Page, search_text="peugeot"):
#     analytics_page = AnalyticsPage(client_user)
#     analytics_page.popup_input_search(search_text)
#     actual_result = ' '.join(analytics_page.unit_list.all_text_contents()).lower()
#     assert search_text in actual_result


# # M2M-777 Search for an object in the "Select up to 10 objects to display..." window using an invalid name
# @mark.testomatio('@Tttttt777')
# def test_invalid_search_object_m2m_777(client_user: Page, search_text="non-existent"):
#     analytics_page = AnalyticsPage(client_user)
#     analytics_page.popup_input_search(search_text)
#     expect(analytics_page.unit_list).not_to_be_attached()


# # M2M-778 Increase/decrease the number in the "Select up to 10 objects..." window.
# @mark.testomatio('@Tttttt778')
# @pytest.mark.parametrize("number", [25, 50, 100, 10]) # test all possible values
# def test_increase_decrease_number_of_objects_m2m_778(client_user: Page, number):
#     analytics_page = AnalyticsPage(client_user)
#     assert len(analytics_page.change_device_list(number)) == number, f"Expected {number} devices, but got {len(analytics_page.unit_list)}"
#     assert analytics_page.row_per_page_dd.inner_text() == str(number)


# # M2M-779 Go to the next/previous page of the list in the "Select up to 10 objects" window
# @mark.testomatio('@Tttttt779')
# def test_next_previous_page_of_list_m2m_779(client_user: Page):
#     analytics_page = AnalyticsPage(client_user)
#     assert analytics_page.next_page() is True, f"Expected to go to the next page, but got {analytics_page.next_page()}"
#     expect(analytics_page.device_of_devices_text.last).to_contain_text("11-20")
#     analytics_page.previos_page_btn.click(delay=500)
#     expect(analytics_page.device_of_devices_text.last).to_contain_text("1-10")






