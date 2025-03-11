import pytest
from loguru import logger
from playwright.sync_api import sync_playwright

from demo.pages.login_page import LoginPage
from framework.helpers.allure_helper import AllureHelper
from framework.helpers.browser_helper import BrowserHelper
from framework.helpers.logger_helper import LoggerHelper
from framework.pages.page_objects import PageObjects


@pytest.fixture(scope="session")
def browser():
    """Fixture to initialize playwright browser"""
    with sync_playwright() as playwright:
        browser_type = BrowserHelper.get_browser_type()
        launch_options = BrowserHelper.get_launch_options()
        browser = getattr(playwright, browser_type).launch(**launch_options)

        yield browser

        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Fixture to initialize playwright page object"""
    page = browser.new_page(no_viewport=True)  # no_viewport - to run maximized browser
    page.goto("https://auth.snappykraken.app/")

    yield page  # Provide the page object to the test

    page.close()



@pytest.fixture()
def po(page):
    return PageObjects(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Fixture to attach allure screenshot and testrail results"""
    # Execute the test and get the result
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.failed:
            AllureHelper.take_screenshot(item)  # Capture screenshot if the test fails


@pytest.fixture(scope="session", autouse=True)
def global_logger():
    LoggerHelper.configure_logger()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logstart(nodeid):
    logger.info(f"Starting test: {nodeid}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logfinish(nodeid):
    logger.info(f"Finished test: {nodeid}")
