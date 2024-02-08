from final_project.steps.SignInSteps import SignInSteps
from final_project.data.stays_data import StaysData
from final_project.steps.stays_step import StaysStep
from final_project.utils import stays_utils as su
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions
from API.GSpread.allure_report_texts import Table as report_text_sheet
import allure
import pytest
import time


class TestStays:
    @pytest.mark.parametrize('expected_stay_destination', StaysData.get_stay_destinations())
    @allure.title('Test Stay destination: {expected_stay_destination}.')
    @allure.description(report_text_sheet.get_value('test_stay_description'))
    def test_stay_destinations(self, driver, expected_stay_destination):
        ss = StaysStep(driver)
        sd = StaysData()

        ss.open_home_page(Urls.HOME_URL)
        ss.refresh_page()
        ss.clean_destination()
        ss.enter_destination(expected_stay_destination)
        ss.click_check_in_date_button()
        ss.select_current_date_in_calendar(su.get_current_date())
        ss.select_stay_duration(sd.get_stay_duration())
        ss.click_search_button()

        for stay_address in ss.get_found_stay_options_addresses():
            with soft_assertions():
                assert_that(stay_address.text).contains(expected_stay_destination)

    @pytest.mark.parametrize('expected_stay_destination, email, password',
                             [(StaysData.get_stay_destination(), 'sherlock@gmail.com', 'Sherlock@2000')])
    @allure.title('Test Saving stay destination: {expected_stay_destination}.')
    @allure.description(report_text_sheet.get_value('test_save_stay_description'))
    def test_saving_stay_destination(self, driver_undetected, expected_stay_destination, email, password):
        rs = SignInSteps(driver_undetected)
        ss = StaysStep(driver_undetected)
        sd = StaysData()

        # precondition
        rs.open_page(Urls.HOME_URL)
        time.sleep(5)
        rs.driver.refresh()
        time.sleep(1)
        rs.open_sign_in()
        rs.fill_email(email)
        rs.submit_email()
        rs.fill_password(password)
        rs.submit_password()

        # test
        ss.clean_destination()
        ss.enter_destination(expected_stay_destination)
        ss.click_check_in_date_button()
        ss.select_current_date_in_calendar(su.get_current_date())
        ss.select_stay_duration(sd.get_stay_duration())
        ss.click_search_button()
        ss.save_stay()
        expected_saved_stay = ss.get_stay_option_title()
        ss.open_account_profile()
        ss.open_saved_page()
        assert_that(ss.is_stay_saved(expected_saved_stay)).is_true()

        # post-conditions
        ss.remove_stay()
