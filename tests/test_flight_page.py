import time
import allure
from final_project.data.flightBooking import FlightTown
from final_project.steps.flightSteps import FlightSteps
import pytest
from final_project.data.CommonData import Urls
from assertpy import assert_that

@allure.epic("Main Epic")
class TestBookingFlight:
    @allure.title('opening main url')
    @allure.description('step opens main page and shows details of page')
    def test_precondition(self, driver):
        Flight_steps = FlightSteps(driver)
        Flight_steps.open_page(Urls.HOME_URL)
        Flight_steps.driver.refresh()

    @allure.title('booking Flight')
    @allure.description('step opens Flight page to order a flight to chosen country')
    @pytest.mark.parametrize('city, expected', [(FlightTown.flight_tokio, 'Success')])
    def test_search(self, driver, city, expected):
        fs = FlightSteps(driver)
        fs.open_flight_page()
        fs.click_country()
        fs.fill_country(city)
        assert_that(fs.submit_country()).contains(expected)
        fs.searchBtn()


    @allure.title('check given variants')
    @allure.description('function clicks nav bar steps to check various recommendations of web-interface')
    @pytest.mark.parametrize('expected', ['Best', 'Cheapest', 'Quickest'])
    def test_check_bars(self, driver, expected):
        chb = FlightSteps(driver)
        if expected == 'Best':
            chb.check_best()
        elif expected == 'Cheapest':
            chb.check_cheapest()
        elif expected == 'Quickest':
            chb.check_quickest()
        time.sleep(2)
