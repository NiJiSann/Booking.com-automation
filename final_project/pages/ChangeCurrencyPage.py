from selenium.webdriver.common.by import By


class ChangeCurrencyPage:
    CLOSE_BTN = (By.XPATH, '//button[@data-testid="selection-modal-close"]')

    @staticmethod
    def get_currency_locator(currency):
        return By.XPATH, f'//button[@data-testid="selection-item"]/div/div/span/div[text()="{currency}"]'
