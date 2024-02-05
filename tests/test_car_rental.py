from final_project.steps.car_rental_step import CarRentalStep
from final_project.data.car_rental_data import CarRentalData
from assertpy import assert_that, soft_assertions


class TestCarRental:
    def test_car_rental_with_drop_off_different_location(self, driver):
        car_rental_step = CarRentalStep(driver)
        car_rental_step.open_page("https://www.booking.com")
        with soft_assertions():
            assert_that(car_rental_step.driver.current_url).contains("https://www.booking.com/index")
        car_rental_step.close_dialog_modal()
        car_rental_step.change_currency()
        with soft_assertions():
            assert_that(car_rental_step.current_currency()).is_equal_to("USD")

        car_rental_data = CarRentalData()
        car_rental_step.open_rental_page()
        with soft_assertions():
            assert_that(car_rental_step.driver.current_url).contains("https://www.booking.com/cars/index")
            assert_that(car_rental_step.search_form_is_visible()).is_true()

        car_rental_step.check_drop_car_different_location()
        with soft_assertions():
            assert_that(car_rental_step.is_checked_drop_car()).is_true()

        car_rental_step.uncheck_driver_age_between()
        with soft_assertions():
            assert_that(car_rental_step.is_checked_age_between()).is_false()
            assert_that(car_rental_step.age_input_is_visible()).is_true()

        car_rental_step.enter_driver_age(car_rental_data.age)
        with soft_assertions():
            assert_that(car_rental_data.age).is_equal_to(car_rental_step.age_value())

        car_rental_step.enter_pic_up_location(car_rental_data.pic_up_location)
        with soft_assertions():
            assert_that(car_rental_step.pic_up_location_value()).contains(car_rental_data.pic_up_location)

        car_rental_step.enter_drop_off_location(car_rental_data.drop_off_location)
        with soft_assertions():
            assert_that(car_rental_step.drop_off_location_value()).contains(car_rental_data.drop_off_location)

        car_rental_step.select_date_and_time(car_rental_data.pick_up_date,
                                             car_rental_data.pick_up_time, "pick_up")
        with soft_assertions():
            assert_that(car_rental_step.selected_pick_up_date()).is_in(car_rental_data.pick_up_date)
            assert_that(car_rental_data.pick_up_time).contains(car_rental_step.selected_pick_up_time())

        car_rental_step.select_date_and_time(car_rental_data.drop_off_date,
                                             car_rental_data.drop_off_time, "drop_off")
        with soft_assertions():
            assert_that(car_rental_step.selected_drop_off_date()).is_in(car_rental_data.drop_off_date)
            assert_that(car_rental_step.selected_drop_off_time()).is_equal_to(car_rental_data.drop_off_time)

        car_rental_step.click_search_button()
        with soft_assertions():
            assert_that(car_rental_step.driver.current_url).contains("https://cars.booking.com/search-results")
