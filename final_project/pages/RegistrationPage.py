from selenium.webdriver.common.by import By


class RegistrationPage:
    EMAIL_INPUT = (By.ID, 'username')
    ERROR_NOTE = (By.ID, 'username-note')
    SUBMIT_REGISTER = (By.XPATH, '//form[@class="nw-register"]')
    NEW_PASSWORD = (By.ID, 'new_password')
    CONFIRM_PASSWORD = (By.ID, 'confirmed_password')
    NEW_PASSWORD_NOTE = (By.ID, 'new_password-note')
    CONFIRM_PASSWORD_NOTE = (By.ID, 'confirmed_password-note')
