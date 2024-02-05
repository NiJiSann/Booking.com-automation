from datetime import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
ua = UserAgent()


def pytest_addoption(parser):
    parser.addoption("--mode", action="store", help="Choose mode run (ci, local)", default="local")


@pytest.fixture(scope="session")
def driver(request):
    mode = request.config.getoption("--mode")
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    if mode == "ci":
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={ua.random}")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    download_path = r'downloads'
    prefs = {
        "download.default_directory": download_path,
        'intl.accept_languages': 'en'
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def cross_driver(request):
    driver = ...
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        driver = webdriver.Chrome(options=options)

    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        try:
            driver = item.funcargs['driver']
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f'{item.nodeid}_{now}.png'.replace('/', '_').replace('::', '__')
            allure.attach(driver.get_screenshot_as_png(), name=filename, attachment_type=allure.attachment_type.PNG)
        except:
            pass
