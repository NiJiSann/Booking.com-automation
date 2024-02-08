import time

import allure
from final_project.data.flightBooking import FlightTown
from final_project.steps.flightSteps import FlightSteps
import pytest
from final_project.data.CommonData import Urls

@allure.epic("Main Epic")
class TestBookingFlight:
    @allure.title('opening main url')
    @allure.description('step opens main page and shows details of page')
    def test_precondition(self, driver):
        Flight_steps = FlightSteps(driver)
        Flight_steps.open_page(Urls.HOME_URL)
        Flight_steps.driver.refresh()

    @allure.title('booking Flight')
    @allure.description('step opens Flight page to order an flight to choosen country')
    @pytest.mark.parametrize('city', FlightTown.flight_tokio)  # Ensure this is a list
    def test_search(self, driver, city):
        fs = FlightSteps(driver)
        fs.open_flight_page()
        fs.click_country()
        fs.fill_country(city)
        time.sleep(4)
        fs.searchBtn()

    @allure.title('check given varaints')
    @allure.description('function clicks nav bar steps to check various recommendation of web-intreface')
    def checkBars(self, driver):
        chb = FlightSteps(driver)
        chb.check_best()
        time.sleep(2)
        chb.check_cheapest()
        time.sleep(2)
        chb.check_quickest()
        time.sleep(2)