from final_project.steps.car_rental_step import CarRentalStep
from final_project.steps.car_rental_result_search_step import CarRentalSearchResultStep
from final_project.data.car_rental_data import CarRentalData
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions
import allure
from API.GSpread.allure_report_texts import Table as report_text_sheet


@allure.feature(report_text_sheet.get_value("car_rental"))
class TestCarRental:
    @allure.title(report_text_sheet.get_value("car_rental_title"))
    @allure.description(report_text_sheet.get_value("car_rental_desc"))
    @allure.tag("E2E")
    @allure.tag("UI")
    def test_end_to_end_car_rental_with_drop_off_different_location(self, driver_undetected):
        car_rental_step = CarRentalStep(driver_undetected)
        car_rental_data = CarRentalData()
        car_rental_search_result = CarRentalSearchResultStep(driver_undetected)

        with allure.step("Preconditions"):
            with allure.step(f"Open the Home page of '{Urls.HOME_URL}'."):
                car_rental_step.open_page(Urls.HOME_URL)
                car_rental_step.close_dialog_modal()
                with soft_assertions():
                    assert_that(car_rental_step.main_page_is_opened()).is_true()
            with allure.step("Change currency to usd"):
                car_rental_step.change_currency()
                with soft_assertions():
                    assert_that(car_rental_step.current_currency()).is_equal_to("USD")

        # Steps in car rental interface
        with allure.step("Open Car Rental Interface"):
            car_rental_step.open_rental_page()
            car_rental_step.change_language_to_en()
            with soft_assertions():
                assert_that(car_rental_step.car_rental_is_opened()).is_true()
                assert_that(car_rental_step.search_form_is_visible()).is_true()

        with allure.step("Check checkbox drop off at different location"):
            car_rental_step.check_drop_car_different_location()
            with soft_assertions():
                assert_that(car_rental_step.is_checked_drop_car()).is_true()

        with allure.step("Default Age checkbox is uncheck"):
            car_rental_step.uncheck_driver_age_between()
            with soft_assertions():
                assert_that(car_rental_step.is_checked_age_between()).is_false()
                assert_that(car_rental_step.age_input_is_visible()).is_true()

        with allure.step("Enter driver's age"):
            car_rental_step.enter_driver_age(car_rental_data.age)
            with soft_assertions():
                assert_that(car_rental_data.age).is_equal_to(car_rental_step.age_value())

        with allure.step("Enter Pick-up location"):
            car_rental_step.enter_pic_up_location(car_rental_data.pic_up_location)
            with soft_assertions():
                assert_that(car_rental_step.pic_up_location_value()).contains(car_rental_data.pic_up_location)

        with allure.step("Enter Drop-off location"):
            car_rental_step.enter_drop_off_location(car_rental_data.drop_off_location)
            with soft_assertions():
                assert_that(car_rental_step.drop_off_location_value()).contains(car_rental_data.drop_off_location)

        with allure.step("Enter Pick-up date and time"):
            car_rental_step.select_date_and_time(car_rental_data.pick_up_date,
                                                 car_rental_data.pick_up_time, "pick_up")
            with soft_assertions():
                assert_that(car_rental_step.selected_pick_up_date()).is_in(car_rental_data.pick_up_date)
                assert_that(car_rental_data.pick_up_time).contains(car_rental_step.selected_pick_up_time())

        with allure.step("Enter Drop-off date and time"):
            car_rental_step.select_date_and_time(car_rental_data.drop_off_date,
                                                 car_rental_data.drop_off_time, "drop_off")
            with soft_assertions():
                assert_that(car_rental_step.selected_drop_off_date()).is_in(car_rental_data.drop_off_date)
                assert_that(car_rental_data.drop_off_time).contains(car_rental_step.selected_drop_off_time())

        with allure.step("Submit car rental search"):
            car_rental_step.click_search_button()
            with soft_assertions():
                assert_that(car_rental_search_result.car_rental_result_search_is_opened()).is_true()


        # Steps in car rental search result page
        with allure.step("Select premium car type"):
            car_rental_search_result.select_car_type()
            with soft_assertions():
                assert_that(car_rental_search_result.is_selected_car_type()).is_true()

        with allure.step("View deal"):
            car_rental_search_result.select_first_car()
            with soft_assertions():
                assert_that(car_rental_search_result.car_deal_page_is_opened()).is_true()

