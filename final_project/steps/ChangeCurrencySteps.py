import re
import time

from selenium.webdriver import Keys
from final_project.steps.BookAttractionSteps import AttractionSteps
from final_project.pages.CommopPage import CommonPage as cp
from final_project.pages.ChangeCurrencyPage import ChangeCurrencyPage as ccp
from final_project.steps.common_actions import Common
from final_project.pages.AttractionsPage import AttractionsPage


class ChangeCurrencySteps(Common):
    def choose_currency(self, currency):
        self.wait_for(cp.CURRENCY_PICKER).click()
        self.click(ccp.get_currency_locator(currency))

    def get_stays_price_currency(self) -> str:
        time.sleep(1)
        self.click(ccp.DATES)
        self.click(ccp.FLEXIBLE)
        self.click(ccp.A_WEEKEND)
        self.click(ccp.MONTH)
        self.click(ccp.SELECT)
        try:
            input_loc = self.wait_for(ccp.STAY_LOCATION_INPUT)
            input_loc.click()
            input_loc.clear()
            time.sleep(1)
            input_loc.send_keys('Japan')
            time.sleep(2)
            input_loc.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
        self.wait_for(ccp.STAY_PRICE)
        price = self.get_text(ccp.STAY_PRICE).replace('.', '')
        price = re.sub(r'\d', '', price)
        return price

    def get_attraction_price_currency(self) -> str:
        attrs = AttractionSteps(self.driver)
        attrs.open_attractions_page()
        time.sleep(1)
        attrs.enter_city_country('Tokyo')
        attrs.search_attractions()
        price = self.wait_for(AttractionsPage.PRICE).text.replace('.', '')
        price = re.sub(r'\d', '', price)
        return price

    def get_car_rental_price_currency(self) -> str:
        time.sleep(1)
        self.click(cp.CAR_RENTAL)
        try:
            input_loc = self.wait_for(ccp.PICK_UP_LOCATION_INPUT)
            input_loc.click()
            input_loc.send_keys('Florida')
            time.sleep(2)
            input_loc.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
        self.click(ccp.SEARCH_CAR)
        try:
            self.wait_for(ccp.CAR_PRICE)
        except:
            pass
        price = self.get_text(ccp.CAR_PRICE).replace('.', '')
        price = re.sub(r'\d', '', price)
        return price

    def get_taxi_price_currency(self) -> str:
        time.sleep(1)
        self.click(cp.AIRPORT_TAXI)
        time.sleep(1)
        try:
            input_loc = self.wait_for(ccp.FROM_LOCATION_INPUT)
            input_loc.click()
            input_loc.send_keys('Haneda')
            time.sleep(2)
            input_loc.send_keys(Keys.ENTER)
            input_dest = self.wait_for(ccp.TO_LOCATION_INPUT)
            input_dest.click()
            input_dest.send_keys('Shibuya')
            time.sleep(2)
            input_dest.send_keys(Keys.ENTER)
        except:
            pass
        self.click(ccp.SEARCH_TAXI)
        time.sleep(1)
        try:
            self.wait_for(ccp.TAXI_PRICE)
        except:
            pass
        price = self.get_text(ccp.TAXI_PRICE).replace('.', '')
        price = re.sub(r'\d', '', price)
        return price

    def get_flight_price_currency(self) -> str:
        time.sleep(1)
        self.click(cp.FLIGHTS)
        try:
            self.click(ccp.TO_HOLDER)
            input_loc = self.wait_for(ccp.TO_INPUT)
            input_loc.clear()
            input_loc.send_keys('Tokyo')
            time.sleep(2)
            input_loc.send_keys(Keys.ENTER)
        except:
            pass

        self.click(ccp.SEARCH_FLIGHT)
        time.sleep(5)
        try:
            self.wait_for(ccp.FLIGHT_PRICE)
        except:
            pass
        price = self.get_text(ccp.FLIGHT_PRICE).replace('.', '')
        price = re.sub(r'\d', '', price)
        return price
