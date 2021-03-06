
from selenium.webdriver.common.by import By
import configparser
from Utilities import settings

def locator(web_element_value):

	try:
		global web_element
		config = configparser.ConfigParser()
		config.read(settings.OBJECT_REPO)
		for section in config.sections():
			for line in config.items(section):
				if line[0].strip().lower() == web_element_value.strip().lower():
					web_element = line[1]

		locator_type = web_element.split(":>:")[0].strip().lower()
		locator_value = web_element.split(":>:")[1]

		if locator_type == 'id':
			return [By.ID, locator_value]
		elif locator_type == 'xpath':
			return [By.XPATH, locator_value]
		elif locator_type == 'linktext':
			return [By.LINKTEXT, locator_value]
		elif locator_type == 'partiallinktext':
			return [By.PARTIAL_LINK_TEXT, locator_value]
		elif locator_type == 'name':
			return [By.NAME, locator_value]
		elif locator_type == 'tagname':
			return [By.TAG_NAME, locator_value]
		elif locator_type == 'classname':
			return [By.CLASS_NAME, locator_value]
		elif locator_value == 'css':
			return [By.CSS_SELECTOR, locator_value]
	
	except Exception as e:
		print("locator() | Exception: " + str(e))

