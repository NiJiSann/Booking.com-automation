from selenium.webdriver.common.by import By
from final_project.pages.CommopPage import CommonPage


class StaysPage(CommonPage):
    DESTINATION_INPUT_FIELD = (By.XPATH, '//input[@name="ss" or @placeholder="Where are you going?"]')
    CHECK_IN_DATE_BUTTON = (By.XPATH, '//button[@data-testid="date-display-field-start"]')
    DISMISS_SIGN_IN_INFO_BUTTON = (By.XPATH, '//button[@aria-label="Dismiss sign in information."]')
    SEARCH_BUTTON = (By.XPATH, '//span[text()="Search"]')
    FOUND_STAY_OPTIONS = (By.XPATH, '//div[@data-testid="property-card"]')
    STAY_OPTION_ADDRESS = (By.XPATH, '//span[@data-testid="address"]')
    NEXT_PAGE_BUTTON = (By.XPATH, '//button[@aria-label="Next page"]')
    LAST_PAGE_TEXTBOX = (By.XPATH, '//div[@data-testid="pagination"]//ol//li[last()]')
    STAY_OPTION_TITLE = (By.XPATH, '//div[@data-testid="title"]')
    STAY_SAVE_BUTTON = (By.XPATH, '//button[@data-testid="wishlist-button"]')
    STAY_DESTINATION_INPUT_CLEAR_BUTTON = (By.XPATH, '//span[@data-testid="input-clear"]')
    ACCOUNT_PROFILE = (By.XPATH, '//button[@data-testid="header-profile"]')

    @staticmethod
    def get_calendar_date_textbox(date: str):
        return By.XPATH, f'//span[@data-date="{date}"]'

    @staticmethod
    def get_stay_duration_textbox(duration: str):
        return By.XPATH, f'//span[text()="{duration}"]'

    @staticmethod
    def get_options_found_message(destination: str):
        return By.XPATH, f'//h1[contains(text(), "{destination}")]'
