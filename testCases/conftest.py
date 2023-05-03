from selenium import webdriver
import pytest
import time


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    # yield driver
    # time.sleep(2)
    # driver.quit()
    return driver


def pytest_addoption(parser):  # this will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
