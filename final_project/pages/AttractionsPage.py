from selenium.webdriver.common.by import By


class AttractionsPage:
    INPUT_CITY_COUNTRY = (By.XPATH, '//*[@data-testid="search-input-field"]')
    SHOW_MORE_BTN = (By.XPATH, '//*[@id="attr-search-results-page-main-content"]/div[2]/button')
    ALL_VIEWED = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div')
    DESTINATION = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[3]/div/div/div/div[2]/ul[1]/li[1]/div')

    @staticmethod
    def get_attraction_locator(attraction_name: str):
        return By.XPATH, f'//h4[@data-testid="card-title" and contains(text(), "{attraction_name}")]'
