import time

import allure
from final_project.data.flightBooking import FlightTown
from final_project.steps.flightSteps import FlightSteps
import pytest
from final_project.data.CommonData import Urls

@allure.epic("Main Epic")  # Replace "Main Epic" with the correct epic title or a dynamic value
class TestBookingFlight:
    def test_precondition(self, driver):
        attraction_steps = FlightSteps(driver)
        attraction_steps.open_page(Urls.HOME_URL)
        attraction_steps.driver.refresh()

    @pytest.mark.parametrize('city', FlightTown.flight_tokio)  # Ensure this is a list
    def test_search(self, driver, city):
        fs = FlightSteps(driver)
        fs.open_flight_page()
        fs.click_country()
        time.sleep(2)
        fs.fill_country(city)

    def select_plan(self, driver):
        sp = FlightSteps(driver)
        sp.open_plan_dropdown()
        sp.select_plan_dropdown()
        time.sleep(5)
