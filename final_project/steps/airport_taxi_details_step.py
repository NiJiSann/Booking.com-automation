import time

from final_project.pages.airport_taxi_page import AirportTaxiDetailsPage
from final_project.steps.my_common_actions import MyCommonActions


class AirportTaxiDetailsStep(MyCommonActions, AirportTaxiDetailsPage):
    def select_car_type(self):
        self.go_to_element(self.SECOND_CAR_TYPE)
        self.click(self.SECOND_CAR_TYPE)

    def add_request_child_seat(self):
        self.go_to_element(self.ADD_REQUEST_CHILD_SEAT)
        self.click(self.ADD_REQUEST_CHILD_SEAT)
        self.click(self.PLUS_CHILD_SEAT)
        self.click(self.CONFIRM_BTN_CHILD_SEAT)

    def add_comment_for_driver(self, comment):
        self.go_to_element(self.COMMENT_TEXT_ARIA)
        self.fill(self.COMMENT_TEXT_ARIA, comment)

    def click_continue_button(self):
        self.go_to_element(self.CONTINUE_BTN)
        self.click(self.CONTINUE_BTN)