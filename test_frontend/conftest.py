import os
import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options



# Set this flag to True to use WebDriver.Remote
USE_REMOTE_DRIVER = False

@pytest.fixture(scope="function")
def get_chrome_options():
    """Get Chrome options."""
    options = chrome_options()
    options.headless = True  # Use headless if you do not need a browser UI
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1650,900")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


@pytest.fixture(scope="function")
def get_webdriver(get_chrome_options):
    """Get WebDriver"""
    options = get_chrome_options
    if USE_REMOTE_DRIVER:
        # Using WebDriver.Remote
        driver = webdriver.Remote(
            command_executor=os.getenv("WEBDRIVER_URL"),
            options=options
        )
    else:
        # Using WebDriver.Chrome
        driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(autouse=False, scope="function")
def setup(request, get_webdriver):
    """When called, creates a new invoice"""
    driver = get_webdriver
    url = "URL_WEB_SITE"
    logger.debug(f"URL {url}")
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True, scope="function")
def setup_not_invoice(request, get_webdriver):
    """Doesn't create an invoice."""
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()