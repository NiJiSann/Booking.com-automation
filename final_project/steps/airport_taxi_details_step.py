import time

from final_project.pages.airport_taxi_page import AirportTaxiDetailsPage
from final_project.steps.my_common_actions import MyCommonActions


class AirportTaxiDetailsStep(MyCommonActions, AirportTaxiDetailsPage):
    def select_car_type(self):
        self.go_to_element(self.SECOND_CAR_TYPE)
        self.click(self.SECOND_CAR_TYPE)

    def add_request_child_seat(self):
        self.scroll_to_elem(self.ADD_REQUEST_CHILD_SEAT)
        self.click(self.ADD_REQUEST_CHILD_SEAT)
        self.click(self.PLUS_CHILD_SEAT)
        self.click(self.CONFIRM_BTN_CHILD_SEAT)

    def child_car_seat(self):
        if self.find(self.CHILD_CAR_SEAT):
            return True
        else:
            return False

    def add_comment_for_driver(self, comment):
        self.scroll_to_elem(self.COMMENT_TEXT_ARIA)
        self.fill(self.COMMENT_TEXT_ARIA, comment)

    def comment_value(self):
        return self.get_value_element(self.COMMENT_TEXT_ARIA)

    def click_continue_button(self):
        self.scroll_to_elem(self.CONTINUE_BTN)
        self.click(self.CONTINUE_BTN)
        time.sleep(2)