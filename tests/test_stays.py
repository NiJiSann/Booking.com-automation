from final_project.data.stays_data import StaysData
from final_project.steps.stays_step import StaysStep
from final_project.utils import stays_utils as su
from assertpy import assert_that, soft_assertions


class TestStays:
    def test_stay_destinations(self, driver):
        ss = StaysStep(driver)
        sd = StaysData()
        expected_stay_destination = sd.get_stay_destination()

        ss.open_home_page('https://www.booking.com/')
        ss.close_sign_in_info_window()
        ss.enter_destination(expected_stay_destination)
        ss.click_check_in_date_button()
        ss.click_current_date_in_calendar(su.get_current_date())
        ss.click_stay_duration(sd.get_stay_duration())
        ss.click_search_button()

        for stay_address in ss.get_found_stay_options_addresses():
            with soft_assertions():
                assert_that(stay_address.text).contains(expected_stay_destination)

