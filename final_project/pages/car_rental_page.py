from selenium.webdriver.common.by import By
from final_project.pages.CommopPage import CommonPage


class CarRentalPage(CommonPage):
    # Locators car rental interface
    CURRENCY_PICKER_NAME = (By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]/span')
    SEARCH_FORM = (By.XPATH, "//*[@data-testid='cars-searchbox-envelope']")
    DROP_CAR_DIFFERENT_LOCATION_CHECKBOX = (By.XPATH,
                                            "//input[@data-testid='searchbox-toolbox-drop-off-checkbox-desktop']")
    DROP_CAR_DIFFERENT_LOCATION_CHECKBOX_STATE = (By.XPATH, "//*[@data-testid='searchbox-container']")
    DRIVERS_AGE_BETWEEN_CHECKBOX = (By.XPATH, "//input[@data-testid='drivers-age-checkbox']")
    DRIVERS_AGE_NUMBER = (By.ID, "drivers-age-input-text")
    FIRST_ITEM = (By.XPATH, "(//*[@data-testid='suggestion'])[1]")
    PIC_UP_LOCATION_INPUT = (By.ID, "searchbox-toolbox-fts-pickup")
    DROP_OFF_LOCATION_INPUT = (By.ID, "searchbox-toolbox-drop-off-fts")
    PIC_UP_DATA_PICKER = (By.ID, "searchbox-toolbox-date-picker-pickup-date")
    SELECTED_PICK_UP_DATE = (By.CSS_SELECTOR, "[data-testid='searchbox-toolbox-date-picker-pickup-date-value']")
    DROP_OFF_DATA_PICKER = (By.ID, "searchbox-toolbox-date-picker-dropoff-date")
    SELECTED_DROP_OFF_DATE = (By.CSS_SELECTOR, "[data-testid='searchbox-toolbox-date-picker-dropoff-date']")
    PIC_UP_TIME_SELECT = (By.ID, "searchbox-toolbox-pickup-time")
    DROP_OFF_TIME_SELECT = (By.ID, "searchbox-toolbox-dropoff-time")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid='searchbox-toolbox-submit-button']")
    DATA_PICKER_MONTH_SLIDER_BUTTON = (By.XPATH, "//*[@data-testid='bui-calendar']//button")
    DATA_PICKER_FIRST_MONTH_HEADER = (By.XPATH, "(//*[@data-testid='bui-calendar']//h3)[1]")
    DATA_PICKER_DAY = (By.XPATH, "(//*[@data-testid='bui-calendar']//tbody)[1]//td")
    LANGUAGE_PICKER = (By.XPATH, "//button[@data-modal-id='language-selection']")
    ENGLISH_LANGUAGE = (By.XPATH, "(//*[@lang='en-gb'])[1]")
    MAIN_PAGE_TITLE = (By.XPATH, "//span[@data-testid='herobanner-title1']")
    RENTAL_PAGE_TITLE = (By.XPATH, "//*[@data-capla-component-boundary='b-cars-cars-lp/indexPage']//h1")



class CarRentalSearchResultPage:
    CAR_RENTAL_PAGE_TITLE = (By.XPATH, "//h1[@data-testid='page-title']")
    DEAL_PAGE_TITLE = (By.XPATH, "//h1[@data-testid='progress-title']")
    PREMIUM_CAR = (By.XPATH, "//button[@aria-label='Show premium cars']")
    FIRST_CAR = (By.XPATH, "(//button[@aria-label='View deal'])[1]")