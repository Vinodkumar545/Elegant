__author__ = 'vinodkumar545'

import platform
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import Select

import py_obj_property as OP

import logging_conf
import logging
import time

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

def element_selected(driver,web_element):
	try:
		loc = OP.locator(web_element)
		selected_element = driver.find_element(loc[0],loc[1])
		selected_element.click()
		if selected_element.is_selected():
			LOGGER.info("element '%s'  is selected successfully."%(web_element))
			return True
		else:
			LOGGER.info("element '%s' is not selected."%(web_element))
			return False

	except Exception as e:
		LOGGER.exception("element_selected_radio_button() | Exception: %s"%(e))
		return False

# def element_selected_check_box(driver,web_element):
# 	try:
# 		loc = OP.locator(web_element)
# 		selected_elements = driver.find_element(loc[0],loc[1])
		
# 			LOGGER.info("element '%s'  is selected successfully."%(web_element))
# 			selected_elements.click()
# 		else:
# 			LOGGER.info("element '%s' is not selected."%(web_element))

# 	except Exception as e:
# 		LOGGER.exception("element_selected_check_box() | Exception: %s"%(e))

def element_enabled(driver,web_element):
	try:
		loc = OP.locator(web_element)
		ele_enabled = driver.find_element(loc[0],loc[1])
		if ele_enabled.is_enabled():
			LOGGER.info("element '%s'  is enabled."%(web_element))
			return True
		else:
			LOGGER.info("element '%s'  is not enabled."%(web_element))
			return False

	except Exception as e:
		LOGGER.exception("element_enabled() | Exception: %s"%(e))
		return False

def get_attr_prpty(driver,web_element,attribute_value):
	try:
		loc = OP.locator(web_element)
		got_element = driver.find_element(loc[0],loc[1])
		attr_value = got_element.get_attribute(attribute_value)
		LOGGER.info("Title value of %s is %s." %(web_element,attr_value))
		return attr_value

	except Exception as e:
		LOGGER.exception("get_attr_prpty() | Exception: %s"%(e)) 


def element_selected_drop_down(driver, web_element,select_options,select_value): 
	"""
	Description: function to select the drop down values

	Args: driver-
		webelement-
		select Options: 
			by_index - to perform select_by_index function
			by_value - to perform select_by_value function
			by_visible_text - to perform select_by_visible_text function

		select Values:
			Values are sent as an arguments to all the three select function
	"""
	try:
		loc = OP.locator(web_element)
		ele = driver.find_element(loc[0],loc[1])
		LOGGER.info("%s"%(ele))
		driver.execute_script("arguments[0].scrollIntoView(true);", ele)
		time.sleep(3)
		select = Select(ele)

		if select_options == "by_index":
			select.select_by_index(select_value)
			LOGGER.info("selected value is '%s' " %(web_element))
			time.sleep(5)

		if select_options == "by_value":
			select.select_by_value(select_value)
			LOGGER.info("selected value is '%s' " %(web_element))
			time.sleep(5)

		if select_options == "by_visible_text":
			select.select_by_visible_text(select_value)
			LOGGER.info("selected value is '%s' " %(web_element))
			time.sleep(5)

	except Exception as e:
		LOGGER.exception("element_selected_drop_down() | Exception: %s"%(e)) 













def back(driver):
	driver.back()
	LOGGER.info("Navigated to previous page successfully.")
