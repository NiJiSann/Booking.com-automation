from final_project.steps.airport_taxi_step import AirportTaxiStep
from final_project.steps.airport_taxi_details_step import AirportTaxiDetailsStep
from final_project.steps.airport_taxi_checkout_step import AirportTaxiCheckoutStep
from final_project.data.airport_taxi_data import AirportTaxiDate, AirportTaxiDetailsDate, UserData, PaymentData
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions
import allure
from API.GSpread.allure_report_texts import Table as report_text_sheet


@allure.feature(report_text_sheet.get_value("airport_taxi"))
class TestAirportTaxi:
    @allure.title(report_text_sheet.get_value("airport_taxi_title"))
    @allure.description(report_text_sheet.get_value("airport_taxi_desc"))
    @allure.tag("E2E")
    @allure.tag("UI")
    def test_end_to_end_airport_taxi_one_way(self, driver_undetected):
        airport_taxi = AirportTaxiStep(driver_undetected)
        airport_taxi_data = AirportTaxiDate()
        airport_taxi_details = AirportTaxiDetailsStep(driver_undetected)
        airport_taxi_details_data = AirportTaxiDetailsDate()
        airport_taxi_checkout = AirportTaxiCheckoutStep(driver_undetected)
        user_data = UserData()
        payment_data = PaymentData()

        with allure.step("Preconditions"):
            with allure.step(f"Open the Home page of '{Urls.HOME_URL}'."):
                airport_taxi.open_page(Urls.HOME_URL)
                with soft_assertions():
                    assert_that(airport_taxi.main_page_is_opened()).is_true()
                airport_taxi.close_dialog_modal()
            airport_taxi.change_currency()
            with allure.step("Change currency to usd"):
                airport_taxi.close_dialog_modal()
                with soft_assertions():
                    assert_that(airport_taxi.current_currency()).is_equal_to("USD")


        # Steps in airport taxi interface
        with allure.step("Open Airport Taxi Interface"):
            airport_taxi.open_airport_taxi_page()
            airport_taxi.change_language_to_en()
            with soft_assertions():
                assert_that(airport_taxi.airport_taxi_page_is_opened()).is_true()
                assert_that(airport_taxi.search_form_is_visible()).is_true()

        with allure.step("Enter Pick-up location"):
            airport_taxi.enter_pick_up_location(airport_taxi_data.pic_up_location)
            with soft_assertions():
                assert_that(airport_taxi.pic_up_location_value()).contains(airport_taxi_data.pic_up_location)

        with allure.step("Enter Destination"):
            airport_taxi.enter_destination_location(airport_taxi_data.destination_location)
            with soft_assertions():
                assert_that(airport_taxi.destination_value()).contains(airport_taxi_data.destination_location)

        with allure.step("Enter Pick-up date"):
            airport_taxi.enter_date(airport_taxi_data.pick_up_date)
            with soft_assertions():
                assert_that(airport_taxi_data.pick_up_date).contains(airport_taxi.selected_pick_up_date())

        with allure.step("Enter Pick-up time"):
            airport_taxi.select_time(airport_taxi_data.pick_up_time)
            with soft_assertions():
                assert_that(airport_taxi.selected_pick_up_time()).is_equal_to(airport_taxi_data.pick_up_time)

        with allure.step("Enter Passengers"):
            airport_taxi.select_passengers(airport_taxi_data.passenger_count)
            with soft_assertions():
                assert_that(airport_taxi_data.passenger_count).is_equal_to(airport_taxi.selected_passenger())

        with allure.step("Submit airport taxi search"):
            airport_taxi.click_search_button()
            with soft_assertions():
                assert_that(airport_taxi_details.airport_taxi_details_page_is_opened()).is_true()


        # Steps in airport taxi details page
        airport_taxi_details.select_car_type()
        with allure.step("Add request child car seat"):
            airport_taxi_details.add_request_child_seat()
            with soft_assertions():
                assert_that(airport_taxi_details.child_car_seat()).is_true()

        with allure.step("Add a comment for driver"):
            airport_taxi_details.add_comment_for_driver(airport_taxi_details_data.comment)
            with soft_assertions():
                assert_that(airport_taxi_details_data.comment).is_equal_to(airport_taxi_details.comment_value())

        with allure.step("Continue to checkout"):
            airport_taxi_details.click_continue_button()
            with soft_assertions():
                assert_that(airport_taxi_checkout.taxi_checkout_page_is_opened()).is_true()


        # Steps in airport taxi checkout
        with allure.step("Enter first name"):
            airport_taxi_checkout.enter_first_name(user_data.first_name)
            with soft_assertions():
                assert_that(user_data.first_name).is_equal_to(airport_taxi_checkout.get_first_name_value())

        with allure.step("Enter last name"):
            airport_taxi_checkout.enter_last_name(user_data.last_name)
            with soft_assertions():
                assert_that(user_data.last_name).is_equal_to(airport_taxi_checkout.get_last_name_value())

        with allure.step("Enter email"):
            airport_taxi_checkout.enter_email(user_data.email)
            with soft_assertions():
                assert_that(user_data.email).is_equal_to(airport_taxi_checkout.get_email_value())

        with allure.step("Select phone code"):
            airport_taxi_checkout.select_phone_code(user_data.phone_code)
            with soft_assertions():
                assert_that(user_data.phone_code).contains(airport_taxi_checkout.get_phone_code_value())

        with allure.step("Enter phone number"):
            airport_taxi_checkout.enter_phone_number(user_data.phone_number)
            with soft_assertions():
                assert_that(user_data.phone_number).is_equal_to(airport_taxi_checkout.get_phone_number_value())

        with allure.step("Enter card holder's name"):
            airport_taxi_checkout.enter_name(payment_data.first_name)
            with soft_assertions():
                assert_that(payment_data.first_name).is_equal_to(airport_taxi_checkout.get_name_value())

        with allure.step("Enter card number"):
            airport_taxi_checkout.enter_card_number(payment_data.card_number)
            with soft_assertions():
                assert_that(payment_data.card_number).is_equal_to(airport_taxi_checkout.get_card_number_value())

        with allure.step("Select card type"):
            try:
                airport_taxi_checkout.select_card_type(payment_data.card_type)
            except:
                pass
            with soft_assertions():
                assert_that(payment_data.card_type).is_equal_to(airport_taxi_checkout.get_card_type_value())

        with allure.step("Enter expiration date"):
            airport_taxi_checkout.enter_expiration_date(payment_data.expiration_date)
            with soft_assertions():
                assert_that(payment_data.expiration_date).is_equal_to(airport_taxi_checkout.get_expiration_date_value())

        with allure.step("Enter cvc"):
            airport_taxi_checkout.enter_cvc_number(payment_data.cvc)
            with soft_assertions():
                assert_that(payment_data.cvc).is_equal_to(airport_taxi_checkout.get_cvc_number_value())

        with soft_assertions():
            assert_that(airport_taxi_checkout.book_and_pay_btn_is_clickable()).is_true()
