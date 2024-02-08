import allure
from final_project.steps.my_common_actions import MyCommonActions
from final_project.pages.car_rental_page import CarRentalPage
from selenium.webdriver.support.ui import Select


class CarRentalStep(MyCommonActions, CarRentalPage):
    @allure.step("Click Car Rental Tab")
    def open_rental_page(self):
        self.click(self.CAR_RENTAL)

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

    @allure.step("Click checkbox drop off at different location")
    def check_drop_car_different_location(self):
        self.js_click(self.DROP_CAR_DIFFERENT_LOCATION_CHECKBOX)

    @allure.step("Assert that checkbox drop off at different location is checked")
    def is_checked_drop_car(self):
        if "dropoff-field-visible" in self.find(self.DROP_CAR_DIFFERENT_LOCATION_CHECKBOX_STATE).get_attribute("class"):
            return True
        else:
            return False

    @allure.step("Click Default Age checkbox")
    def uncheck_driver_age_between(self):
        self.js_click(self.DRIVERS_AGE_BETWEEN_CHECKBOX)

    @allure.step("Assert that default age checkbox is uncheck")
    def is_checked_age_between(self):
        if self.find(self.DRIVERS_AGE_NUMBER):
            return False
        else:
            return True

    @allure.step("Assert that input age visible")
    def age_input_is_visible(self):
        return self.find(self.DRIVERS_AGE_NUMBER)

    @allure.step("Fill in the driver's age:{age}")
    def enter_driver_age(self, age):
        self.fill(self.DRIVERS_AGE_NUMBER, age)

    @allure.step("Assert that driver's age filled")
    def age_value(self):
        return self.get_value_element(self.DRIVERS_AGE_NUMBER)

    @allure.step("Fill in the Pick-up location: {pic_up_location}")
    def enter_pic_up_location(self, pic_up_location):
        self.fill(self.PIC_UP_LOCATION_INPUT, pic_up_location)
        self.click(self.FIRST_ITEM)

    @allure.step("Assert that Pick Up location filled")
    def pic_up_location_value(self):
        return self.get_value_element(self.PIC_UP_LOCATION_INPUT)

    @allure.step("Fill in the Drop-off location: {drop_off_location}")
    def enter_drop_off_location(self, drop_off_location):
        self.fill(self.DROP_OFF_LOCATION_INPUT, drop_off_location)
        self.click(self.FIRST_ITEM)

    @allure.step("Assert that Drop-off location filled")
    def drop_off_location_value(self):
        return self.get_value_element(self.DROP_OFF_LOCATION_INPUT)

    @allure.step("Select {kind} date: {date} and time: {time_t}")
    def select_date_and_time(self, date, time_t, kind):
        day, month = date.split(" ")
        if day[0] == "0": day.replace("0", "")
        if kind == "pick_up":
            self.js_click(self.PIC_UP_DATA_PICKER)
        elif kind == "drop_off":
            self.js_click(self.DROP_OFF_DATA_PICKER)
        while True:
            if month == self.driver.find_element(*self.DATA_PICKER_FIRST_MONTH_HEADER).text.split(" ")[0]:
                break
            else:
                if len(self.driver.find_elements(*self.DATA_PICKER_MONTH_SLIDER_BUTTON)) == 1:
                    self.js_click(self.DATA_PICKER_MONTH_SLIDER_BUTTON)
                else:
                    self.driver.find_elements(*self.DATA_PICKER_MONTH_SLIDER_BUTTON)[1].click()
        self.element_with_text(self.DATA_PICKER_DAY, day).click()

        time_select = None
        if kind == "pick_up":
            time_select = Select(self.find(self.PIC_UP_TIME_SELECT))
        elif kind == "drop_off":
            time_select = Select(self.find(self.DROP_OFF_TIME_SELECT))
        time_select.select_by_value(time_t)

    @allure.step("Assert that pick-up date selected")
    def selected_pick_up_date(self):
        return self.get_text(self.SELECTED_PICK_UP_DATE).split(",")[1].strip()

    @allure.step("Assert that drop-off date selected")
    def selected_drop_off_date(self):
        return self.get_text(self.SELECTED_DROP_OFF_DATE).split(",")[1].strip()

    @allure.step("Assert that pick-up time selected")
    def selected_pick_up_time(self):
        time_select = Select(self.find(self.PIC_UP_TIME_SELECT))
        return time_select.first_selected_option.text

    @allure.step("Assert that drop-off time selected")
    def selected_drop_off_time(self):
        time_select = Select(self.find(self.DROP_OFF_TIME_SELECT))
        return time_select.first_selected_option.text

    @allure.step("Click search button")
    def click_search_button(self):
        self.js_click(self.SUBMIT_BUTTON)

    @allure.step("Assert that system displays 'Home page' interface")
    def main_page_is_opened(self):
        return self.find(self.MAIN_PAGE_TITLE).is_displayed()

    @allure.step("Assert that system displays 'Car rental' interface")
    def car_rental_is_opened(self):
        return self.find(self.RENTAL_PAGE_TITLE).is_displayed()
