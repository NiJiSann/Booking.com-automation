from selenium.webdriver.common.by import By
from final_project.pages.CommopPage import CommonPage


class CarRentalPage(CommonPage):
    # Locators car rental interface
    DROP_CAR_DIFFERENT_LOCATION_CHECKBOX = (By.CSS_SELECTOR, "label[for='searchbox-toolbox-drop-off-checkbox-desktop']")
    DRIVERS_AGE_BETWEEN_CHECKBOX = (By.CSS_SELECTOR, "label[for='drivers-age-checkbox']")
    DRIVERS_AGE_NUMBER = (By.ID, "drivers-age-input-text")
    FIRST_ITEM = (By.XPATH, "(//*[@data-testid='suggestion'])[1]")
    PIC_UP_LOCATION_INPUT = (By.ID, "searchbox-toolbox-fts-pickup")
    DROP_OFF_LOCATION_INPUT = (By.ID, "searchbox-toolbox-drop-off-fts")
    PIC_UP_DATA_PICKER = (By.ID, "searchbox-toolbox-date-picker-pickup-date")
    DROP_OFF_DATA_PICKER = (By.ID, "searchbox-toolbox-date-picker-dropoff-date")
    PIC_UP_TIME_SELECT = (By.ID, "searchbox-toolbox-pickup-time")
    DROP_OFF_TIME_SELECT = (By.ID, "searchbox-toolbox-dropoff-time")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid='searchbox-toolbox-submit-button']")
    DATA_PICKER_MONTH_SLIDER_BUTTON = (By.XPATH, "//*[@data-testid='bui-calendar']//button")
    DATA_PICKER_FIRST_MONTH_HEADER = (By.XPATH, "(//*[@data-testid='bui-calendar']//h3)[1]")
    DATA_PICKER_DAY = (By.XPATH, "(//*[@data-testid='bui-calendar']//tbody)[1]//td")
