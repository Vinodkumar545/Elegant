__author__ = 'vinodkumar545'

import platform
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import py_obj_property as OP

import logging_conf
import logging

LOGGER = logging.getLogger('logs')


NODE_URL = "http://127.0.0.1:4444/wd/hub"

def activate_driver(brower_name, headless=False):

	if brower_name == 'chrome':
		desired_capabilities = DesiredCapabilities.CHROME.copy()
		options = webdriver.ChromeOptions()

		if headless:
			options.add_argument('--headless')

		desired_capabilities = options.to_capabilities()
		desired_capabilities['browser_version'] = "75.0.3770.142"
		desired_capabilities['platform'] = platform.system()
		desired_capabilities['version'] = platform.version()

	if brower_name == 'firefox':
		desired_capabilities = DesiredCapabilities.FIREFOX.copy()
		options = webdriver.FirefoxOptions()

		if headless:
			options.headless = True
		
		desired_capabilities = options.to_capabilities()
		desired_capabilities['browser_version'] = "68.0.1"
		desired_capabilities['platform'] = platform.system()
		desired_capabilities['version'] = platform.version()

	# Instantiate an instance of Remote WebDriver with the desired capabilities.
	driver = webdriver.Remote(command_executor=NODE_URL, desired_capabilities=desired_capabilities)

	LOGGER.info("%s Driver has been initiated successfully"%(brower_name))

	return driver


def maximize_window(driver):
	driver.maximize_window()
	LOGGER.info("Browser was maximized successfully.")

def open_url(driver, url):
	driver.get(url)
	LOGGER.info("Driver open the '%s' successfully"%(url))

def implicitly_wait(driver, sec=10):
	driver.implicitly_wait(sec)
	LOGGER.info("Driver to perform implicitly_wait of '%s' seconds."%(sec))

def set_page_load_timeout(driver, sec=60):
	driver.set_page_load_timeout(60)
	LOGGER.info("Driver has set the page load timeout of '%s' seconds."%(sec))

def get_title(driver):
	title = driver.title
	LOGGER.info("Title of the webpage is '%s'."%(title))
	return title

def click(driver, web_element):
	try:
		loc = OP.locator(web_element)
		click_element = driver.find_element(loc[0], loc[1])
		click_element.click()
		LOGGER.info("Clicked on '%s' successfully."%(web_element))

	except:
		try:
			driver.execute_script("arguments[0].click();", click_element)
			LOGGER.info("Clicked on '%s' successfully by execute_script."%(web_element))
		except Exception as e:
			LOGGER.exception("click() | Exception: %s"%(e))

	# try:
	# 	loc = OP.locator(web_element)
	# 	driver.find_element(loc[0], loc[1]).click()
	# 	LOGGER.info("Clicked on '%s' successfully."%(web_element))

	# except Exception as e:
	# 	LOGGER.exception("click() | Exception: %s"%(e))

def send_keys(driver, web_element, text):
	try:
		loc = OP.locator(web_element)
		driver.find_element(loc[0], loc[1]).clear()
		driver.find_element(loc[0], loc[1]).send_keys(text)
		LOGGER.info("%s is successfully simuated in %s."%(text, web_element))
	except Exception as e:
		LOGGER.exception("send_keys() | Exception: %s"%(e))


def back(driver):
	driver.back()
	LOGGER.info("Navigated to previous page successfully.")
