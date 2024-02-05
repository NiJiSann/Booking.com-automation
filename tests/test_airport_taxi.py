from final_project.steps.airport_taxi_step import AirportTaxiStep
from final_project.steps.airport_taxi_details_step import AirportTaxiDetailsStep
from final_project.data.airport_taxi_data import AirportTaxiDate, AirportTaxiDetailsDate


class TestAirportTaxi:
    def test_airport_taxi_one_way(self, driver):
        airport_taxi = AirportTaxiStep(driver)
        airport_taxi.open_page("https://www.booking.com")
        airport_taxi.close_dialog_modal()
        airport_taxi.change_currency()

        airport_taxi_data = AirportTaxiDate()
        airport_taxi.open_airport_taxi_page()
        airport_taxi.enter_pick_up_location(airport_taxi_data.pic_up_location)
        airport_taxi.enter_destination_location(airport_taxi_data.destination_location)
        airport_taxi.enter_date(airport_taxi_data.pick_up_date)
        airport_taxi.select_time(airport_taxi_data.pick_up_time)
        airport_taxi.select_passengers(airport_taxi_data.passenger_count)
        airport_taxi.click_search_button()

        airport_taxi_details_data = AirportTaxiDetailsDate()
        airport_taxi_details = AirportTaxiDetailsStep(driver)
        airport_taxi_details.select_car_type()
        airport_taxi_details.add_request_child_seat()
        airport_taxi_details.add_comment_for_driver(airport_taxi_details_data.comment)
        airport_taxi_details.click_continue_button()
        airport_taxi_details.wait_current_url("https://taxis.booking.com/checkout")

