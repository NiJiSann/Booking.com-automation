import time
from final_project.pages.airport_taxi_page import AirportTaxiDetailsPage
from final_project.steps.my_common_actions import MyCommonActions
import allure


class AirportTaxiDetailsStep(MyCommonActions, AirportTaxiDetailsPage):

    @allure.step("Assert that airport taxi search result page is opened")
    def airport_taxi_details_page_is_opened(self):
        time.sleep(60)
        return self.find(self.AIRPORT_TAXI_DETAILS_TITLE).is_displayed()

    @allure.step("Click second car type")
    def select_car_type(self):
        self.go_to_element(self.SECOND_CAR_TYPE)
        self.click(self.SECOND_CAR_TYPE)

    @allure.step("Open child car seat modal and add")
    def add_request_child_seat(self):
        self.go_to_element(self.ADD_REQUEST_CHILD_SEAT)
        self.click(self.ADD_REQUEST_CHILD_SEAT)
        self.click(self.PLUS_CHILD_SEAT)
        self.click(self.CONFIRM_BTN_CHILD_SEAT)

    @allure.step("Assert that child car seat visible")
    def child_car_seat(self):
        if self.find(self.CHILD_CAR_SEAT):
            return True
        else:
            return False

    @allure.step("Fill comment text area")
    def add_comment_for_driver(self, comment):
        self.go_to_element(self.COMMENT_TEXT_ARIA)
        self.fill(self.COMMENT_TEXT_ARIA, comment)

    @allure.step("Assert that comment text area filled")
    def comment_value(self):
        return self.get_value_element(self.COMMENT_TEXT_ARIA)

    @allure.step("Click continue button")
    def click_continue_button(self):
        self.go_to_element(self.CONTINUE_BTN)
        self.click(self.CONTINUE_BTN)
        time.sleep(2)