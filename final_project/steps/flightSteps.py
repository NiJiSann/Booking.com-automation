from selenium.webdriver import Keys
from final_project.pages.flightPages import FlightMainPage as fmp
from final_project.steps.common_actions import Common
import time

class FlightSteps(Common):
    def open_flight_page(self):
        self.click(fmp.FLIGHTS)

    def click_country(self):
        cname = self.find(fmp.TO_HOLDER)
        cname.click()

    def fill_country(self, country: str):
        cname = self.find(fmp.DESTINATION_CITY_INPUT)
        cname.send_keys(country)
        cname.send_keys(Keys.ENTER)
        time.sleep(10)

    def submit_country(self) -> str:

        return "Success"

    def searchBtn(self):
        btn = self.find(fmp.SEARCH_FLIGHT)
        btn.click()
        time.sleep(5)

    def check_best(self):
        best_btn = self.find(fmp.Best)
        best_btn.click()

    def check_cheapest(self):
        cheap_btn = self.find(fmp.cheapest)
        cheap_btn.click()

    def check_quickest(self):
        quick_btn = self.find(fmp.Quickest)
        quick_btn.click()
