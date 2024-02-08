from selenium.webdriver import Keys
from final_project.pages.flightPages import FlightMainPage as fmp
from final_project.pages.CommopPage import CommonPage as cp
from final_project.steps.common_actions import Common
import time

class FlightSteps(Common):
    def open_flight_page(self):
        self.click(fmp.FLIGHTS)

    def click_country(self):
        cname = self.find(fmp.TO_HOLDER)  # Use the correct input element
        cname.click()

    def fill_country(self, country:str):
        csame = self.find(fmp.TO_HOLDER_INPUT)
        csame.send_keys(country)
        csame.send_keys(Keys.ENTER)
        time.sleep(10)


    def searchBtn(self):
        btn = self.find(fmp.SEARCH_FLIGHT)
        btn.click()
        time.sleep(5)

    def check_best(self):
        bstbtn = self.find(fmp.Best)
        bstbtn.click()

    def check_cheapest(self):
        bstbtn = self.find(fmp.cheapest)
        bstbtn.click()

    def check_quickest(self):
        bstbtn = self.find(fmp.Quickest)
        bstbtn.click()