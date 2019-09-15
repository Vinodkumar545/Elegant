import pytest

from selenium import webdriver
from Utilities import test_base,settings
from random import randint
import os


@pytest.fixture(scope='function')
def driver(request):
    global driver
    driver = test_base.activate_driver("chrome")
    test_base.maximize_window(driver)
    test_base.implicitly_wait(driver)
    
    # Close the driver after each test case
    def close_driver():
        driver.close()
        driver.quit()

    request.addfinalizer(close_driver)

    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        filename = "screenshot_" + str(randint(4000,9999)) + ".png"
        driver.get_screenshot_as_file(os.path.join(settings.SCREENSHOT,filename))
        html = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%os.path.join(settings.SCREENSHOT,filename)
        extra.append(pytest_html.extras.html(html))
        report.extra = extra

