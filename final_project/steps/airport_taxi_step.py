from final_project.steps.my_common_actions import MyCommonActions
from final_project.pages.airport_taxi_page import AirportTaxiPage
from selenium.webdriver.support.ui import Select
import time
import allure


class AirportTaxiStep(MyCommonActions, AirportTaxiPage):
    @allure.step("Assert that system displays 'Home page' interface")
    def main_page_is_opened(self):
        return self.find(self.MAIN_PAGE_TITLE).is_displayed()

    @allure.step("Click Airport Taxis Tab")
    def open_airport_taxi_page(self):
        time.sleep(3)
        self.click(self.AIRPORT_TAXI)

    @allure.step("Assert that system displays 'Airport taxi' interface")
    def airport_taxi_page_is_opened(self):
        return self.find(self.AIRPORT_PAGE_TITLE).is_displayed()

    @allure.step("Change currency")
    def change_currency(self):
        self.click(self.CURRENCY_PICKER)
        self.click(self.USD_CURRENCY)

    @allure.step("Assert that currency is equal to USD")
    def current_currency(self):
        return self.get_text(self.CURRENCY_PICKER_NAME)

    def change_language_to_en(self):
        self.click(self.LANGUAGE_PICKER)
        self.click(self.ENGLISH_LANGUAGE)

    @allure.step("Assert that search form visible")
    def search_form_is_visible(self):
        return self.find(self.SEARCH_FORM)

    @allure.step("Fill in the Pick-up location: {pickup_location}")
    def enter_pick_up_location(self, pickup_location):
        self.fill(self.PICK_UP_LOCATION, pickup_location)
        self.wait_for(self.ITEM_LIST_PICK_UP)
        self.click(self.FIRST_ITEM)

    @allure.step("Assert that Pick Up location filled")
    def pic_up_location_value(self):
        return self.get_value_element(self.PICK_UP_LOCATION)

    @allure.step("Fill in the Destination: {destination_location}")
    def enter_destination_location(self, destination_location):
        self.fill(self.DESTINATION_LOCATION, destination_location)
        self.wait_for(self.ITEM_LIST_PICK_DOWN)
        self.click(self.FIRST_ITEM)

    @allure.step("Assert that Destination filled")
    def destination_value(self):
        return self.get_value_element(self.DESTINATION_LOCATION)

    @allure.step("Select date: {date}")
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

    @allure.step("Assert that date selected")
    def selected_pick_up_date(self):
        return self.get_text(self.SELECTED_PICK_UP_DATE).split("/")[0].strip()

    @allure.step("Assert that time selected")
    def selected_pick_up_time(self):
        return self.get_text(self.PIC_UP_TIME_SELECT)

    @allure.step("Select time: {time_t}")
    def select_time(self, time_t):
        hour, minute = time_t.split(":")
        self.click(self.TIME_PICKER)
        select_hours = Select(self.find(self.HOURS_SELECTOR))
        select_hours.select_by_value(hour)
        select_minutes = Select(self.find(self.MINUTES_SELECTOR))
        select_minutes.select_by_value(minute)
        self.click(self.CONFIRM_TIME_BTN)

    @allure.step("Select passengers: {passengers_count}")
    def select_passengers(self, passengers_count):
        select_passengers = Select(self.find(self.PASSENGERS_SELECTOR))
        select_passengers.select_by_value(passengers_count)

    @allure.step("Assert that passengers selected")
    def selected_passenger(self):
        passenger_select = Select(self.find(self.PASSENGERS_SELECTOR))
        return passenger_select.first_selected_option.text

    @allure.step("Click search button")
    def click_search_button(self):
        self.click(self.SUBMIT_BUTTON)
        time.sleep(2)



