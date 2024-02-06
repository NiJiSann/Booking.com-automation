import time

from final_project.steps.my_common_actions import MyCommonActions
from final_project.pages.car_rental_page import CarRentalSearchResultPage


class CarRentalSearchResultStep(MyCommonActions, CarRentalSearchResultPage):
    def car_rental_result_search_is_opened(self):
        time.sleep(2)
        return self.find(self.CAR_RENTAL_PAGE_TITLE).is_displayed()

    def select_car_type(self):
        self.click(self.PREMIUM_CAR)

    def is_selected_car_type(self):
        self._wait.until(lambda driver: driver.find_element(*self.PREMIUM_CAR).get_attribute('class').__contains__('activeTab'))
        is_active = "activeTab" in self.find(self.PREMIUM_CAR).get_attribute("class")
        return is_active

    def select_first_car(self):
        self.click(self.FIRST_CAR)
        self.switch_to_next_tab()

    def car_deal_page_is_opened(self):
        return self.find(self.DEAL_PAGE_TITLE).is_displayed()