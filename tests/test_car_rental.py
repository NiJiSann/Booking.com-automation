from final_project.steps.car_rental_step import CarRentalStep
from final_project.steps.car_rental_search_result_step import CarRentalSearchResultStep
from final_project.data.car_rental_data import CarRentalData


class TestCarRental:
    def test_car_rental_with_drop_off_different_location(self, driver):
        car_rental_step = CarRentalStep(driver)
        car_rental_step.open_page("https://www.booking.com")
        car_rental_step.close_dialog_modal()
        car_rental_step.change_currency()

        car_rental_data = CarRentalData()
        car_rental_step.open_rental_page()
        car_rental_step.check_drop_car_different_location()
        car_rental_step.uncheck_driver_age_between()
        car_rental_step.enter_driver_age(car_rental_data.age)
        car_rental_step.enter_pic_up_location(car_rental_data.pic_up_location)
        car_rental_step.enter_drop_off_location(car_rental_data.drop_off_location)
        car_rental_step.select_date_and_time(car_rental_data.pick_up_date, car_rental_data.pick_up_time, "pick_up")
        car_rental_step.select_date_and_time(car_rental_data.drop_off_date, car_rental_data.drop_off_time, "drop_off")
        car_rental_step.click_search_button()

        car_rental_result_step = CarRentalSearchResultStep(driver)
        car_rental_result_step.wait_current_url("https://cars.booking.com/search-results")
