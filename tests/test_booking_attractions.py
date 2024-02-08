import allure
from API.GSpread.allure_report_texts import Table as report_text_sheet

from final_project.steps.BookAttractionSteps import AttractionSteps
from final_project.data.AttractionData import AttractionData
import pytest
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions


@allure.epic(report_text_sheet.get_value('main'))
class TestBookingAttraction:
    @allure.title(report_text_sheet.get_value('book_attraction_preconditions_title'))
    @allure.description(report_text_sheet.get_value('book_attraction_preconditions_desc'))
    def test_precondition(self, driver):
        attraction_steps = AttractionSteps(driver)
        with allure.step(report_text_sheet.get_value('open_home')):
            attraction_steps.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('refresh')):
            attraction_steps.driver.refresh()

    @pytest.mark.parametrize('location, attraction, expected', AttractionData.attractions_list)
    @allure.title(report_text_sheet.get_value('find_attraction_title') + ': {location} x {attraction}')
    @allure.description(report_text_sheet.get_value('find_attraction_desc'))
    def test_find_attraction(self, driver, location, attraction,  expected):
        attraction_steps = AttractionSteps(driver)
        with allure.step(report_text_sheet.get_value('open_attractions')):
            attraction_steps.open_attractions_page()
        with allure.step(report_text_sheet.get_value('enter_city_country')):
            attraction_steps.enter_city_country(location)
        with allure.step(report_text_sheet.get_value('search_attraction')):
            attraction_steps.search_attractions()
        with allure.step(report_text_sheet.get_value('show_all_attractions')):
            attraction_steps.show_all_attractions()
        with soft_assertions(), allure.step(report_text_sheet.get_value('check_if_attraction_exist')):
            assert_that(attraction_steps.find_attraction(attraction)).contains_ignoring_case(expected)
