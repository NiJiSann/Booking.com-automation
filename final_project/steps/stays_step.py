from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from final_project.steps.common_actions import Common
from final_project.pages.stays_page import StaysPage
from final_project.utils import stays_utils as su


class StaysStep(Common):
    def open_home_page(self, home_page_url):
        self.open_page(home_page_url)

    def enter_destination(self, destination):
        destination_input = self.find(StaysPage.DESTINATION_INPUT_FIELD)
        destination_input.send_keys(destination)
        return self

    def click_check_in_date_button(self):
        self.find(StaysPage.CHECK_IN_DATE_BUTTON).click()
        return self

    def click_current_date_in_calendar(self, current_date: str):
        self.find(StaysPage.get_calendar_date_textbox(current_date)).click()
        return self

    def click_stay_duration(self, stay_duration: str):
        self.click(StaysPage.get_stay_duration_textbox(stay_duration))
        return self

    def click_search_button(self):
        self.click(StaysPage.SEARCH_BUTTON)
        return self

    def click_next_page_button(self):
        self.click(StaysPage.NEXT_PAGE_BUTTON)
        return self

    def get_number_of_options_found(self, destination):
        options_found_message = self.get_text(StaysPage.get_options_found_message(destination))
        print(f'>>>>> LOG: STEPS options_found_message = {options_found_message}')
        number_of_options = su.get_number(options_found_message)
        print(f'>>>>> LOG: STEPS number_of_options = {number_of_options}')
        return number_of_options

    def get_found_stay_options_addresses(self):
        return self.driver.find_elements(*StaysPage.STAY_OPTION_ADDRESS)

    def get_last_page_number(self):
        return int(self.find(StaysPage.LAST_PAGE_TEXTBOX).text)

    def close_sign_in_info_window(self):
        try:
            self.wait_for(StaysPage.DISMISS_SIGN_IN_INFO_BUTTON).click()
        except NoSuchElementException:
            print('>>> LOG: SIGN IN window is not displayed.')
        except TimeoutException:
            print('>>> LOG: SIGN IN window is not displayed.')
