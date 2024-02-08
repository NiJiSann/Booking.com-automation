import time
from selenium.webdriver import Keys
from final_project.steps.BookAttractionSteps import AttractionSteps
from final_project.pages.CommopPage import CommonPage as cp
from final_project.pages.ChangeCurrencyPage import ChangeCurrencyPage as ccp
from final_project.steps.my_common_actions import MyCommonActions as Common
from final_project.steps.airport_taxi_step import AirportTaxiStep
from final_project.steps.car_rental_step import CarRentalStep


class ChangeCurrencySteps(Common):
    def choose_currency(self, currency):
        self.close_dialog_modal()
        time.sleep(2)
        self.click(cp.CURRENCY_PICKER)
        self.click(ccp.get_currency_locator(currency))

    def get_stays_price_currency(self, match) -> str:
        time.sleep(1)
        self.click(ccp.DATES)
        self.click(ccp.FLEXIBLE)
        self.click(ccp.A_WEEKEND)
        self.click(ccp.MONTH)
        self.click(ccp.SELECT)
        try:
            input_loc = self.wait_for(ccp.STAY_LOCATION_INPUT)
            input_loc.click()
            input_loc.send_keys(Keys.CONTROL + 'A')
            input_loc.send_keys(Keys.DELETE)
            time.sleep(1)
            input_loc.clear()
            time.sleep(1)
            input_loc.send_keys('Japan')
            time.sleep(2)
            input_loc.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
        source = self.driver.page_source
        if source.count(match[0]) > 1 or source.count(match[1]) > 1:
            return 'Currencies are matching'
        return 'Currencies are not matching'

    def get_attraction_price_currency(self, match) -> str:
        attrs = AttractionSteps(self.driver)
        attrs.open_attractions_page()
        time.sleep(1)
        attrs.enter_city_country('Tokyo')
        attrs.search_attractions()
        source = self.driver.page_source
        if source.count(match[0]) > 1 or source.count(match[1]) > 1:
            return 'Currencies are matching'
        return 'Currencies are not matching'

    def get_car_rental_price_currency(self, match) -> str:
        crs = CarRentalStep(self.driver)
        crs.open_rental_page()
        input_loc = self.wait_for(crs.PIC_UP_LOCATION_INPUT)
        input_loc.send_keys(Keys.CONTROL + 'A')
        input_loc.send_keys(Keys.DELETE)
        time.sleep(1)
        crs.enter_pic_up_location('Florida')
        crs.click_search_button()
        source = self.driver.page_source
        if source.count(match[0]) > 1 or source.count(match[1]) > 1:
            return 'Currencies are matching'
        return 'Currencies are not matching'

    def get_taxi_price_currency(self, match) -> str:
        ats = AirportTaxiStep(self.driver)
        ats.open_airport_taxi_page()
        ats.enter_pick_up_location('Dubai')
        ats.enter_destination_location('Burj Khalifa')
        ats.enter_date('20 April')
        ats.click_search_button()
        source = self.driver.page_source
        if source.count(match[0]) > 0 or source.count(match[1]) > 0:
            return 'Currencies are matching'
        return 'Currencies are not matching'

    def get_flight_price_currency(self, match) -> str:
        time.sleep(1)
        self.click(cp.FLIGHTS)
        try:
            self.click(ccp.TO_HOLDER)
            input_loc = self.wait_for(ccp.TO_INPUT)
            input_loc.clear()
            input_loc.send_keys(Keys.CONTROL + 'A')
            input_loc.send_keys(Keys.DELETE)
            time.sleep(1)
            input_loc.send_keys('Tokyo')
            time.sleep(2)
            input_loc.send_keys(Keys.ENTER)
        except:
            pass

        self.click(ccp.SEARCH_FLIGHT)
        time.sleep(15)
        source = self.driver.page_source
        if source.count(match[0]) > 1 or source.count(match[1]) > 1:
            return 'Currencies are matching'
        return 'Currencies are not matching'
