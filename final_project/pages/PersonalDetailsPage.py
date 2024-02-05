from selenium.webdriver.common.by import By


class PersonalDetailsPage:
    SET_PROFILE_IMAGE_MODAL = (By.XPATH, '//button[@data-test-id="mysettings-avatar-btn-open"]')
    IMAGE_INPUT = (By.XPATH, '//button[@data-test-id="mysettings-avatar-input"]')
    STATUS_NOTE = (By.XPATH, '/html/body/div[4]/div/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div/div/div/div/p')
    SAVE_IMAGE = (By.XPATH, '//button[@data-test-id="mysettings-avatar-btn-save"]')
