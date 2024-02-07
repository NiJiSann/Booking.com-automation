from selenium.webdriver.common.by import By
from final_project.pages.CommopPage import CommonPage


class SavedPage(CommonPage):
    SAVED_STAYS = (By.XPATH, '//h1[@class="bui-card__title"]//a')
    REMOVE_STAY_BUTTON = (By.XPATH, '//a[@data-action="remove"]')
