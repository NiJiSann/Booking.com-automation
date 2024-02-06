from selenium.common import NoSuchElementException

from final_project.steps.my_common_actions import MyCommonActions
from final_project.pages.airport_taxi_page import AirportTaxiPage
from selenium.webdriver.support.ui import Select
import time


class AirportTaxiStep(MyCommonActions, AirportTaxiPage):
    def open_airport_taxi_page(self):
        time.sleep(3)
        self.click(self.AIRPORT_TAXI)

    def change_currency(self):
        self.click(self.CURRENCY_PICKER)
        self.click(self.USD_CURRENCY)

    def current_currency(self):
        return self.get_text(self.CURRENCY_PICKER_NAME)

    def change_language_to_en(self):
        self.click(self.LANGUAGE_PICKER)
        self.click(self.ENGLISH_LANGUAGE)

    def search_form_is_visible(self):
        return self.find(self.SEARCH_FORM)

    def check_one_way(self):
        self.click(self.ONE_WAY_CHECKBOX)

    def is_checked_one_way(self):
        try:
            self.find(self.ONE_WAY_STATE)
            return False
        except NoSuchElementException:
            return True

    def enter_pick_up_location(self, pickup_location):
        self.fill(self.PICK_UP_LOCATION, pickup_location)
        self.wait_for(self.ITEM_LIST_PICK_UP)
        self.click(self.FIRST_ITEM)

    def pic_up_location_value(self):
        return self.get_value_element(self.PICK_UP_LOCATION)

    def enter_destination_location(self, destination_location):
        self.fill(self.DESTINATION_LOCATION, destination_location)
        self.wait_for(self.ITEM_LIST_PICK_DOWN)
        self.click(self.FIRST_ITEM)

    def destination_value(self):
        return self.get_value_element(self.DESTINATION_LOCATION)

    def enter_date(self, date):
        self.click(self.DATA_PICKER)
        day, month = date.split(" ")
        if day[0] == "0": day.replace("0", "")
        month_is_displayed = False
        while not month_is_displayed:
            if month == self.find(self.DATA_PICKER_MONTH_CAPTION).text.split(" ")[0]:
                month_is_displayed = True
            else:
                self.click(self.find(self.DATA_PICKER_MONTH_NEXT_BUTTON))
        self.element_with_text(self.DATA_PICKER_DAY, day).click()

    def selected_pick_up_date(self):
        return self.get_text(self.SELECTED_PICK_UP_DATE).split("/")[0].strip()

    def selected_pick_up_time(self):
        return self.get_text(self.PIC_UP_TIME_SELECT)

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

    def selected_passenger(self):
        passenger_select = Select(self.find(self.PASSENGERS_SELECTOR))
        return passenger_select.first_selected_option.text

    def click_search_button(self):
        self.click(self.SUBMIT_BUTTON)
        time.sleep(2)



