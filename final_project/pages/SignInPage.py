from selenium.webdriver.common.by import By


class SignInPage:
    EMAIL_INPUT = (By.ID, 'username')
    ERROR_NOTE = (By.ID, 'username-note')
    SUBMIT_SIGN_IN = (By.XPATH, '//form[@class="nw-signin"]')
    PASSWORD = (By.ID, 'password')
    PASSWORD_NOTE = (By.ID, 'password-note')
