from selenium.webdriver.common.by import By
from final_project.pages.CommopPage import CommonPage


class AirportTaxiPage(CommonPage):
    # Locators search airport taxi interface
    CURRENCY_PICKER_NAME = (By.XPATH, '//button[@data-testid = "header-currency-picker-trigger"]/span')
    SEARCH_FORM = (By.XPATH, "//*[@class='lp-hero__searchbox-container ']")
    ONE_WAY_CHECKBOX = (By.XPATH, '//span[@data-test="returnJourneyNegative-label"]')
    ONE_WAY_STATE = (By.XPATH, "//undefined['undefined']")
    ITEM_LIST_PICK_UP = (By.CSS_SELECTOR, "ul#pickupLocation-items")
    ITEM_LIST_PICK_DOWN = (By.CSS_SELECTOR, "ul#dropoffLocation-items")
    FIRST_ITEM = (By.CSS_SELECTOR, "[data-test='rw-dropdown-container'] li:nth-child(2) button")
    PICK_UP_LOCATION = (By.ID, 'pickupLocation')
    DESTINATION_LOCATION = (By.ID, 'dropoffLocation')
    DATA_PICKER = (By.XPATH, '//button[@aria-label="pickup date input field"]')
    DATA_PICKER_MONTH_NEXT_BUTTON = (By.XPATH, "//button[@data-test='rw-date-picker__btn--next']")
    DATA_PICKER_MONTH_CAPTION = (By.XPATH, "//*[@data-test='on-click-outside']//caption")
    SELECTED_PICK_UP_DATE = (By.XPATH, "//button[@data-test='rw-date-field__link--pickup']/span")
    DATA_PICKER_DAY = (By.XPATH, "//td/a[@class='rw-c-date-picker__calendar-cell--link']")
    TIME_PICKER = (By.XPATH, "//button[@aria-label='pickup time input field']")
    PIC_UP_TIME_SELECT = (By.XPATH, "//button[@data-test='rw-time-field--pickup']/span")
    HOURS_SELECTOR = (By.ID, "pickupHour")
    MINUTES_SELECTOR = (By.ID, "pickupMinute")
    CONFIRM_TIME_BTN = (By.XPATH, "//button[@data-test='rw-time-picker__confirm-button']")
    PASSENGERS_SELECTOR = (By.ID, "passengers")
    SUBMIT_BUTTON = (By.XPATH, "(//button[@name='searchButton'])[1]")


class AirportTaxiDetailsPage(CommonPage):
    # Locators details airport taxi page
    ADD_REQUEST_CHILD_SEAT = (By.XPATH, "//button[@data-testid='child-seat-cta__request-link']")
    CHILD_CAR_SEAT = (By.XPATH, "//*[@data-testid='child-seat-selection__count']")
    PLUS_CHILD_SEAT = (By.XPATH,
                       "//*[@data-testid='child-seat-modal']//*[@data-testid='child-seat-selector__stepper']["
                       "2]//button[2]")
    CONFIRM_BTN_CHILD_SEAT = (By.XPATH, "//*[@data-testid='child-seat-modal']"
                                        "//button[@data-testid='child-seat-modal__confirm']")
    COMMENT_TEXT_ARIA = (By.XPATH, "//textarea[@data-test='comments__input']")
    CONTINUE_BTN = (By.XPATH, "//button[@data-test='continue-action-bar__continue-button']")
    SECOND_CAR_TYPE = (By.XPATH, '(//*[@data-test="taxi-car-card-wrapper__car-card-container"]/div)[2]')



