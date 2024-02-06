from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from final_project.steps.common_actions import Common
from final_project.pages.stays_page import StaysPage
from final_project.utils import stays_utils as su
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time


class StaysStep(Common):
    @allure.step('Open Home page.')
    def open_home_page(self, home_page_url):
        self.open_page(home_page_url)

    @allure.step('Refresh the page.')
    def refresh_page(self):
        time.sleep(10)
        self.driver.refresh()
        return self

    @allure.step('Enter input for destination: {destination}.')
    def enter_destination(self, destination):
        time.sleep(5)
        self.find(StaysPage.DESTINATION_INPUT_FIELD).send_keys(destination)
        return self

    @allure.step('Click "check-in date" button.')
    def click_check_in_date_button(self):
        time.sleep(5)
        self.find(StaysPage.CHECK_IN_DATE_BUTTON).click()
        return self

    @allure.step('Select current date in the calendar: {current_date}.')
    def select_current_date_in_calendar(self, current_date: str):
        self.find(StaysPage.get_calendar_date_textbox(current_date)).click()
        return self

    @allure.step('Select stay duration: {stay_duration}.')
    def select_stay_duration(self, stay_duration: str):
        self.find(StaysPage.get_stay_duration_textbox(stay_duration)).click()
        return self

    @allure.step('Click the Search button.')
    def click_search_button(self):
        self.find(StaysPage.SEARCH_BUTTON).click()
        return self

    @allure.step('Click the Next page button.')
    def click_next_page_button(self):
        self.find(StaysPage.NEXT_PAGE_BUTTON).click()
        return self
    
    @allure.step('Get the number of stay options found for destination: {destination}')
    def get_number_of_options_found(self, destination):
        options_found_message = self.get_text(StaysPage.get_options_found_message(destination))
        number_of_options = su.get_number(options_found_message)
        return number_of_options

    @allure.step('Get the addresses for the found stay options.')
    def get_found_stay_options_addresses(self):
        return self.driver.find_elements(*StaysPage.STAY_OPTION_ADDRESS)

    @allure.step('Get the last page number after search is performed.')
    def get_last_page_number(self):
        return int(self.find(StaysPage.LAST_PAGE_TEXTBOX).text)

    @allure.step('Close "Sign in Info" window.')
    def close_sign_in_info_window(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(StaysPage.DISMISS_SIGN_IN_INFO_BUTTON)).click()
        except NoSuchElementException:
            print('>>> LOG: SIGN IN window is not displayed. NoSuchElementException.')
        except TimeoutException:
            print('>>> LOG: SIGN IN window is not displayed. TimeoutException')
