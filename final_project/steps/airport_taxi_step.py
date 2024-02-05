from final_project.steps.my_common_actions import MyCommonActions
from final_project.pages.airport_taxi_page import AirportTaxiPage
from selenium.webdriver.support.ui import Select
import time


class AirportTaxiStep(MyCommonActions, AirportTaxiPage):
    def open_airport_taxi_page(self):
        time.sleep(2)
        self.click(self.AIRPORT_TAXI)

    def change_currency(self):
        self.click(self.CURRENCY_PICKER)
        self.click(self.USD_CURRENCY)

    def enter_pick_up_location(self, pickup_location):
        self.fill(self.PICK_UP_LOCATION, pickup_location)
        self.wait_for(self.ITEM_LIST_PICK_UP)
        self.click(self.FIRST_ITEM)

    def enter_destination_location(self, destination_location):
        self.fill(self.DESTINATION_LOCATION, destination_location)
        self.wait_for(self.ITEM_LIST_PICK_DOWN)
        self.click(self.FIRST_ITEM)

    def enter_date(self, date):
        self.click(self.DATA_PICKER)
        day, month = date.split(" ")
        if day[0] == "0": day.replace("0", "")
        while True:
            if month == self.driver.find_element(*self.DATA_PICKER_MONTH_CAPTION).text.split(" ")[0]:
                break
            else:
                self.click(self.driver.find_element(*self.DATA_PICKER_MONTH_NEXT_BUTTON))
        self.element_with_text(self.DATA_PICKER_DAY, day).click()

    def select_time(self, time_t):
        hour, minute = time_t.split(":")
        self.click(self.TIME_PICKER)
        select_hours = Select(self.find(self.HOURS_SELECTOR))
        select_hours.select_by_value(hour)
        select_minutes = Select(self.find(self.MINUTES_SELECTOR))
        select_minutes.select_by_value(minute)
        self.click(self.CONFIRM_TIME_BTN)

    def select_passengers(self, passengers_count):
        select_passengers = Select(self.find(self.PASSENGERS_SELECTOR))
        select_passengers.select_by_value(passengers_count)

    def click_search_button(self):
        self.click(self.SUBMIT_BUTTON)





