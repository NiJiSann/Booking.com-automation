import time

from final_project.steps.airport_taxi_step import AirportTaxiStep
from final_project.steps.airport_taxi_details_step import AirportTaxiDetailsStep
from final_project.data.airport_taxi_data import AirportTaxiDate, AirportTaxiDetailsDate
from assertpy import assert_that, soft_assertions


class TestAirportTaxi:
    def test_airport_taxi_one_way(self, driver_undetected):
        airport_taxi = AirportTaxiStep(driver_undetected)
        airport_taxi.open_page("https://www.booking.com")
        with soft_assertions():
            assert_that(airport_taxi.driver.current_url).contains("https://www.booking.com/index")
        airport_taxi.close_dialog_modal()
        airport_taxi.change_currency()
        airport_taxi.close_dialog_modal()
        with soft_assertions():
            assert_that(airport_taxi.current_currency()).is_equal_to("USD")

        airport_taxi_data = AirportTaxiDate()
        airport_taxi.open_airport_taxi_page()
        airport_taxi.change_language_to_en()
        with soft_assertions():
            assert_that(airport_taxi.driver.current_url).contains("https://www.booking.com/taxi")
            assert_that(airport_taxi.search_form_is_visible()).is_true()

        airport_taxi.check_one_way()
        with soft_assertions():
            assert_that(airport_taxi.is_checked_one_way()).is_true()

        airport_taxi.enter_pick_up_location(airport_taxi_data.pic_up_location)
        with soft_assertions():
            assert_that(airport_taxi.pic_up_location_value()).contains(airport_taxi_data.pic_up_location)

        airport_taxi.enter_destination_location(airport_taxi_data.destination_location)
        with soft_assertions():
            assert_that(airport_taxi.destination_value()).contains(airport_taxi_data.destination_location)

        airport_taxi.enter_date(airport_taxi_data.pick_up_date)
        with soft_assertions():
            assert_that(airport_taxi_data.pick_up_date).contains(airport_taxi.selected_pick_up_date())

        airport_taxi.select_time(airport_taxi_data.pick_up_time)
        with soft_assertions():
            assert_that(airport_taxi.selected_pick_up_time()).is_equal_to(airport_taxi_data.pick_up_time)

        airport_taxi.select_passengers(airport_taxi_data.passenger_count)
        with soft_assertions():
            assert_that(airport_taxi_data.passenger_count).is_equal_to(airport_taxi.selected_passenger())

        airport_taxi.click_search_button()
        with soft_assertions():
            assert_that(airport_taxi.driver.current_url).contains("https://taxis.booking.com/search")

        airport_taxi_details_data = AirportTaxiDetailsDate()
        airport_taxi_details = AirportTaxiDetailsStep(driver_undetected)
        airport_taxi_details.select_car_type()
        airport_taxi_details.add_request_child_seat()
        with soft_assertions():
            assert_that(airport_taxi_details.child_car_seat()).is_true()

        airport_taxi_details.add_comment_for_driver(airport_taxi_details_data.comment)
        with soft_assertions():
            assert_that(airport_taxi_details_data.comment).is_equal_to(airport_taxi_details.comment_value())

        airport_taxi_details.click_continue_button()
        with soft_assertions():
            assert_that(airport_taxi_details.driver.current_url).contains("https://taxis.booking.com/checkout")
