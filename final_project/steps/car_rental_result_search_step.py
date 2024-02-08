import time
import allure
from final_project.steps.my_common_actions import MyCommonActions
from final_project.pages.car_rental_page import CarRentalSearchResultPage


class CarRentalSearchResultStep(MyCommonActions, CarRentalSearchResultPage):
    @allure.step("Assert that car rental search result page is opened")
    def car_rental_result_search_is_opened(self):
        time.sleep(60)
        return self.wait_for(self.CAR_RENTAL_PAGE_TITLE).is_displayed()

    @allure.step("Click a premium car type")
    def select_car_type(self):
        self.click(self.PREMIUM_CAR)

    @allure.step("Premium car type is active")
    def is_selected_car_type(self):
        self._wait.until(lambda driver: driver.find_element(*self.PREMIUM_CAR).get_attribute('class').__contains__('activeTab'))
        is_active = "activeTab" in self.find(self.PREMIUM_CAR).get_attribute("class")
        return is_active

    @allure.step("Click first car")
    def select_first_car(self):
        self.click(self.FIRST_CAR)
        self.switch_to_next_tab()

    @allure.step("Car deal page is opened")
    def car_deal_page_is_opened(self):
        return self.find(self.DEAL_PAGE_TITLE).is_displayed()