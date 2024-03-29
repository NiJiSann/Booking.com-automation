from datetime import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from seleniumbase import Driver
from API.GSpread.allure_report_texts import Table


def pytest_addoption(parser):
    # Parameters passed to the command line when running test
    parser.addoption("--mode", action="store", help="Choose mode run (ci, local)", default="local")


@pytest.fixture(scope="session")
def driver(request):
    mode = request.config.getoption("--mode")
    service = Service(executable_path=EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    options.add_experimental_option('detach', True)
    # Change run mode
    if mode == "ci":
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    download_path = r'downloads'
    prefs = {
        "download.default_directory": download_path,
        'intl.accept_languages': 'en'
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Edge(options=options, service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def driver_undetected(request):
    mode = request.config.getoption("--mode")
    options = {
        'browser': 'edge',
        'disable_gpu': True,
        'undetectable': True,
        'agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                 '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3',
        'd_width': 1920,
        'd_height': 1080
    }
    # Change run mode
    if mode == 'ci':
        options['headless2'] = True

    m_driver = Driver(**options)
    yield m_driver
    m_driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    Table.load()


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
            allure.attach(driver.page_source, name='source HTML', attachment_type=allure.attachment_type.HTML)
        except:
            pass
        try:
            driver = item.funcargs['cross_driver']
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f'{item.nodeid}_{now}.png'.replace('/', '_').replace('::', '__')
            allure.attach(driver.get_screenshot_as_png(), name=filename, attachment_type=allure.attachment_type.PNG)
            allure.attach(driver.page_source, name='source HTML', attachment_type=allure.attachment_type.HTML)
        except:
            pass
