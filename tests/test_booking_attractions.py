import allure
from API.GSpread.allure_report_texts import Table as report_text_sheet

from final_project.steps.BookAttractionSteps import AttractionSteps
from final_project.data.AttractionData import AttractionData
import pytest
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions


@allure.epic(report_text_sheet.get_value('main'))
class TestBookingAttraction:
    @allure.title(report_text_sheet.get_value(''))
    @allure.description(report_text_sheet.get_value(''))
    def test_precondition(self, driver):
        attraction_steps = AttractionSteps(driver)
        with allure.step(report_text_sheet.get_value('')):
            attraction_steps.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            attraction_steps.driver.refresh()

    @pytest.mark.parametrize('location, attraction, expected', AttractionData.attractions_list)
    @allure.title(report_text_sheet.get_value('') + ': {location} x {attraction}')
    @allure.description(report_text_sheet.get_value(''))
    def test_find_attraction(self, driver, location, attraction,  expected):
        attraction_steps = AttractionSteps(driver)
        with allure.step(report_text_sheet.get_value('')):
            attraction_steps.open_attractions_page()
        with allure.step(report_text_sheet.get_value('')):
            attraction_steps.enter_city_country(location)
        with allure.step(report_text_sheet.get_value('')):
            attraction_steps.search_attractions()
        with allure.step(report_text_sheet.get_value('')):
            attraction_steps.show_all_attractions()
        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(attraction_steps.find_attraction(attraction)).contains_ignoring_case(expected)
