import time
from selenium.webdriver import Keys
from final_project.steps.BookAttractionSteps import AttractionSteps
from final_project.pages.CommopPage import CommonPage as cp
from final_project.pages.ChangeCurrencyPage import ChangeCurrencyPage as ccp
from final_project.steps.common_actions import Common


class ChangeCurrencySteps(Common):
    def choose_currency(self, currency):
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
        self.click(cp.CAR_RENTAL)
        input_loc = self.wait_for(ccp.PICK_UP_LOCATION_INPUT)
        input_loc.click()
        input_loc.send_keys('Florida')
        time.sleep(2)
        input_loc.send_keys(Keys.ENTER)
        self.click(ccp.SEARCH_CAR)
        self.wait_for(ccp.AVAILABLE_TEXT)
        source = self.driver.page_source
        if source.count(match[0]) > 1 or source.count(match[1]) > 1:
            return 'Currencies are matching'
        return 'Currencies are not matching'

    def get_taxi_price_currency(self, match) -> str:
        self.click(cp.AIRPORT_TAXI)
        input_loc = self.wait_for(ccp.FROM_LOCATION_INPUT)
        input_loc.send_keys('Haneda')
        time.sleep(2)
        input_loc.send_keys(Keys.ENTER)
        input_dest = self.wait_for(ccp.TO_LOCATION_INPUT)
        input_dest.send_keys('Shibuya')
        time.sleep(2)
        input_dest.send_keys(Keys.ENTER)
        self.click(ccp.SEARCH_TAXI)
        self.wait_for(ccp.JOURNEY_TEXT)
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
        self.wait_for(ccp.BEST_TEXT)
        source = self.driver.page_source
        if source.count(match[0]) > 1 or source.count(match[1]) > 1:
            return 'Currencies are matching'
        return 'Currencies are not matching'
