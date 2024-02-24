from selenium.webdriver.common.by import By


class ChangeCurrencyPage:
    CLOSE_BTN = (By.XPATH, '//button[@data-testid="selection-modal-close"]')

    @staticmethod
    def get_currency_locator(currency):
        return By.XPATH, f'//button[@data-testid="selection-item"]/div/div/span/div[text()="{currency}"]'

    # Stays
    STAY_LOCATION_INPUT = (By.XPATH, '//input[@placeholder="Where are you going?"]')
    STAY_PRICE = (By.XPATH, '//span[@data-testid="price-and-discounted-price"]')
    DATES = (By.XPATH, '//div[@data-testid="searchbox-dates-container"]')
    FLEXIBLE = (By.XPATH, '//nav[@data-testid="datepicker-tabs"]/div/ul/li[2]')
    A_WEEKEND = (By.XPATH, '//div[@data-testid="flexible-dates-day"][1]')
    MONTH = (By.XPATH, '//label[@data-testid="flexible-dates-month"]')
    SELECT = (By.XPATH, '//span[@data-testid="flexible-dates-footer"]/../button')
    # Car Rental
    PICK_UP_LOCATION_INPUT = (By.XPATH, '//*[@id="searchbox-toolbox-fts-pickup"]')
    SEARCH_CAR = (By.XPATH, '//button[@data-testid="searchbox-toolbox-submit-button"]')
    CAR_PRICE = (By.XPATH, '//div[@aria-label="Product Card"]/div[6]/div/div/div[2]/div')
    AVAILABLE_TEXT = (By.XPATH, '//h1[contains(text(),"available")]')
    # Airport Taxi
    FROM_LOCATION_INPUT = (By.XPATH, '//*[@id="pickupLocation"]')
    TO_LOCATION_INPUT = (By.XPATH, '//*[@id="dropoffLocation"]')
    SEARCH_TAXI = (By.XPATH, '//button[@data-test="rw-form__search-btn"]')
    TAXI_PRICE = (By.XPATH, '//div[@data-test="taxi-card-wrapper__car-card--standard-taxi-price"]')
    JOURNEY_TEXT = (By.XPATH, '//h3[contains(text(),"journey")]')
    # Flights
    TO_HOLDER = (By.XPATH, '//div[text()="To?"]')
    TO_INPUT = (By.XPATH, '//input[@placeholder="To?"]')
    SEARCH_FLIGHT = (By.XPATH, '//span[text()="Search"]/../../..')
    FLIGHT_PRICE = (By.XPATH, '//span[@class="price-text"]')
    BEST_TEXT = (By.XPATH, '//span[contains(text(),"Best")]')
