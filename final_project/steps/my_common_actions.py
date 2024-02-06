import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from final_project.steps.common_actions import Common


class MyCommonActions(Common):
    def fill(self, locator, value):
        self.js_click(locator)
        self.find(locator).send_keys(value)

    def js_click(self, locator):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*locator))

    def close_dialog_modal(self):
        try:
            self.click(("css selector", "[role='dialog'] [type='button']"))
        except TimeoutException:
            pass

    def element_with_text(self, locator, text):
        elements = self.driver.find_elements(*locator)
        for element in elements:
            if element.text == text:
                return element

    def get_value_element(self, locator):
        return self.find(locator).get_attribute("value")

    def go_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self._wait.until(ec.presence_of_element_located(locator)))

    def current_url(self):
        time.sleep(2)
        return self.driver.current_url

    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])