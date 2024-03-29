import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Common:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self._wait = WebDriverWait(self.driver, 20)

    def wait_for(self, locator) -> WebElement:
        return self._wait.until(ec.visibility_of_element_located(locator))

    def find(self, locator) -> WebElement:
        time.sleep(1)
        return self.driver.find_element(*locator)

    def click(self, locator):
        time.sleep(1)
        self._wait.until(ec.element_to_be_clickable(locator)).click()

    def submit(self, locator):
        time.sleep(1)
        self._wait.until(ec.element_to_be_clickable(locator)).submit()

    def get_text(self, locator):
        elem = self.find(locator)
        return elem.text

    def wait_for_page(self):
        self._wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def open_page(self, url):
        self.driver.get(url)
        self.wait_for_page()

    def close_dialog_modal(self):
        try:
            self.click(("css selector", "[role='dialog'] [type='button']"))
        except:
            pass

    def scroll_to_elem(self, locator):
        visible = False
        while not visible:
            try:
                visible = self.driver.find_element(*locator).is_displayed()
                return
            except:
                self.driver.execute_script("window.scrollBy(0, 500);")
