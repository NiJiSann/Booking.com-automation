# from final_project.steps.common_actions import Common
import time

from final_project.steps.my_common_actions import MyCommonActions
from final_project.pages.car_rental_page import CarRentalPage
from selenium.webdriver.support.ui import Select


class CarRentalStep(MyCommonActions, CarRentalPage):
    def open_rental_page(self):
        time.sleep(2)
        self.click(self.CAR_RENTAL)

    def change_currency(self):
        self.click(self.CURRENCY_PICKER)
        self.click(self.USD_CURRENCY)

    def check_drop_car_different_location(self):
        self.click(self.DROP_CAR_DIFFERENT_LOCATION_CHECKBOX)

    def uncheck_driver_age_between(self):
        self.click(self.DRIVERS_AGE_BETWEEN_CHECKBOX)

    def enter_driver_age(self, age):
        self.fill(self.DRIVERS_AGE_NUMBER, age)

    def enter_pic_up_location(self, pic_up_location):
        self.fill(self.PIC_UP_LOCATION_INPUT, pic_up_location)
        self.click(self.FIRST_ITEM)

    def enter_drop_off_location(self, pic_down_location):
        self.fill(self.DROP_OFF_LOCATION_INPUT, pic_down_location)
        self.click(self.FIRST_ITEM)

    def select_date_and_time(self, date, time_t, kind):
        day, month = date.split(" ")
        if day[0] == "0": day.replace("0", "")
        if kind == "pick_up":
            self.click(self.PIC_UP_DATA_PICKER)
        elif kind == "drop_off":
            self.click(self.DROP_OFF_DATA_PICKER)
        while True:
            if month == self.driver.find_element(*self.DATA_PICKER_FIRST_MONTH_HEADER).text.split(" ")[0]:
                break
            else:
                if len(self.driver.find_elements(*self.DATA_PICKER_MONTH_SLIDER_BUTTON)) == 1:
                    self.click(self.driver.find_element(*self.DATA_PICKER_MONTH_SLIDER_BUTTON))
                else:
                    self.driver.find_elements(*self.DATA_PICKER_MONTH_SLIDER_BUTTON)[1].click()
        self.element_with_text(self.DATA_PICKER_DAY, day).click()

        time_select = None
        if kind == "pick_up":
            time_select = Select(self.find(self.PIC_UP_TIME_SELECT))
        elif kind == "drop_off":
            time_select = Select(self.find(self.DROP_OFF_TIME_SELECT))
        time_select.select_by_value(time_t)

    def click_search_button(self):
        self.click(self.SUBMIT_BUTTON)