from final_project.data.stays_data import StaysData
from final_project.steps.stays_step import StaysStep
from final_project.utils import stays_utils as su
from assertpy import assert_that, soft_assertions
import allure
import pytest


class TestStays:
    @pytest.mark.parametrize('expected_stay_destination', StaysData.get_stay_destinations())
    @allure.title('Test Stay destination: {expected_stay_destination}.')
    @allure.description('The test verifies that the correct stay destinations are found for the expected search destination.')
    def test_stay_destinations(self, driver, expected_stay_destination):
        ss = StaysStep(driver)
        sd = StaysData()

        ss.open_home_page('https://www.booking.com/')
        ss.refresh_page()
        ss.enter_destination(expected_stay_destination)
        ss.click_check_in_date_button()
        ss.select_current_date_in_calendar(su.get_current_date())
        ss.select_stay_duration(sd.get_stay_duration())
        ss.click_search_button()

        for stay_address in ss.get_found_stay_options_addresses():
            with soft_assertions():
                assert_that(stay_address.text).contains(expected_stay_destination)

