import pytest

from selenium import webdriver
from Utilities import test_base

@pytest.fixture(scope='function')
def driver(request):
    # Initialize the driver before each test case
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(10)

    driver = test_base.activate_driver("chrome")
    test_base.maximize_window(driver)
    test_base.implicitly_wait(driver)


    # Close the driver after each test case
    def close_driver():
        driver.close()
        driver.quit()

    request.addfinalizer(close_driver)

    return driver

