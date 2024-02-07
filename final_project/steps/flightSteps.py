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
        csame.click()
        time.sleep(5)
        csame.send_keys(country)
        csame.send_keys(Keys.RETURN)

    def open_plan_dropdown(self):
        op = self.find(fmp.FLIGHT_CLASS_DROPDOWN)
        op.click()

    def select_plan_dropdown(self):
        sp = self.find(fmp.PLAN_BUSSINES)
        sp.click()
        time.sleep(5)
