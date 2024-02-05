import time

from selenium.webdriver import Keys

from final_project.pages.AttractionsPage import AttractionsPage as ap
from final_project.pages.CommopPage import CommonPage as cp
from final_project.steps.common_actions import Common


class AttractionSteps(Common):
    def open_attractions_page(self):
        time.sleep(2)
        self.click(cp.ATTRACTIONS)

    def enter_city_country(self, city_country):
        self.wait_for(ap.INPUT_CITY_COUNTRY).send_keys(city_country + Keys.ENTER)

    def search_attractions(self):
        self.wait_for(ap.DESTINATION)
        self.find(ap.INPUT_CITY_COUNTRY).send_keys(Keys.ENTER)

    def show_all_attractions(self):
        attempts = 0
        while attempts < 4:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                self.click(ap.SHOW_MORE_BTN)
            except:
                attempts += 1

    def find_attraction(self, attraction_name) -> str:
        try:
            self.get_text(ap.get_attraction_locator(attraction_name))
            return 'Attraction is found'
        except:
            return 'Attraction is not found'
