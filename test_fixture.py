
from selenium import webdriver
import pytest

# scope - 'Function' - activate driver (different session) for each test case
# scope - 'module' - activate driver (same session) for all test case

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


def test_01_selenium(driver):

	# driver = webdriver.Chrome()

	print(driver)

	driver.get('https://www.google.co.in/')

	assert driver.title == 'Google'


def test_02_selenium(driver):

	# driver = webdriver.Chrome()

	print(driver)

	driver.get('https://www.w3schools.com/')

	assert driver.title == 'W3Schools Online Web Tutorial'

	driver.close()

