import pytest

from selenium import webdriver

@pytest.fixture(scope='function')
def driver(request):
	# Initialize the driver before each test case
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.implicitly_wait(10)

	# Close the driver after each test case
	def close_driver():
		driver.close()
		driver.quit()

	request.addfinalizer(close_driver)

	return driver

