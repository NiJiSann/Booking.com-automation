from selenium.webdriver.common.by import By


class CommonPage:
    STAYS = (By.ID, 'accommodations')
    FLIGHTS = (By.ID, 'flights')
    CAR_RENTAL = (By.ID, 'cars')
    ATTRACTIONS = (By.ID, 'attractions')
    AIRPORT_TAXI = (By.ID, 'airport_taxis')
    REGISTER = (By.XPATH, '//a[@data-testid = "header-sign-up-button"]')
    SIGN_IN = (By.XPATH, '//a[@data-testid = "header-sign-in-button"]')
    CURRENCY_PICKER = (By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]')
    YOUR_ACCOUNT = (By.XPATH, '//*[@id="b2indexPage"]/div[3]/div/div/header/nav[1]/div[2]/div/span/button')
    SAVED = (By.XPATH, '//*[@id=":rc:"]/div/div/div/div/ul/li[6]')
    MANAGE_ACCOUNT = (By.XPATH, '//*[@id=":rc:"]/div/div/div/div/ul/li[1]')
