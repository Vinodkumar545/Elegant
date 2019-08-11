
import pytest

# scope - 'Function' - activate driver (different session) for each test case
# scope - 'module' - activate driver (same session) for all test case




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

