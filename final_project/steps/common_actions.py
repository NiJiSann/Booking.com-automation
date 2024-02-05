import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Common:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self._wait = WebDriverWait(self.driver, 20)
        self.driver.implicitly_wait(5)

    def wait_for(self, locator) -> WebElement:
        return self._wait.until(ec.presence_of_element_located(locator))

    def find(self, locator) -> WebElement:
        time.sleep(1)
        return self.driver.find_element(*locator)

    def click(self, locator):
        time.sleep(1)
        self._wait.until(ec.element_to_be_clickable(locator)).click()

    def submit(self, locator):
        self._wait.until(ec.element_to_be_clickable(locator)).submit()

    def get_text(self, locator):
        time.sleep(2)
        elem = self.find(locator)
        return elem.text

    def open_page(self, url):
        self.driver.get(url)
        self._wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        time.sleep(1)

    def scroll_to_elem(self, locator):
        visible = False
        while not visible:
            try:
                visible = self.driver.find_element(*locator).is_displayed()
                return
            except:
                self.driver.execute_script("window.scrollBy(0, 500);")
