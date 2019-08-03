
from selenium import webdriver
import time

import py_obj_property

URL = "https://www.ultimateqa.com/simple-html-elements-for-automation/"

# initialize Chrome Driver
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.maximize_window()
driver.get(URL)
driver.set_page_load_timeout(60)
driver.implicitly_wait(10)

try:

	# clear() - Clears the text if it’s a text entry element.
	# //span[@id='et_search_icon']


	# send_keys() - Simulates typing into the element. 
	# //input[@id='et_pb_contact_name_0']
	# //input[@id='et_pb_contact_email_0']
	# //button[@class='et_pb_contact_submit et_pb_button']
	# //div[contains(@class,'et-pb-contact-message')]


	# is displayed() - hether the element is visible to a user.
	# //h4[contains(text(),'Advanced Controls')]

	locator = py_obj_property.locator("HP_txt_advcont")
	d = driver.find_element(locator[0], locator[1]).is_displayed()
	print(d)

	# Highlight webelement
	# "arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');"


	# is selected() - Returns whether the element is selected.
	# //input[@type='radio' and @value='male']


	# is enabled() - Returns whether the element is enabled.
	# //button[@class='buttonClass']

	# get_attribute() - Gets the given attribute or property of the element.
	# //a[@data-shared='sharing-twitter-909']

	# location - The location of the element in the renderable canvas.
	# //button[@class='buttonClass']

	# scroll_into_view
	# //h4[contains(text(),'Checkboxes')]
	# driver.execute_script("arguments[0].scrollIntoView(true);", element)

	## Select from drop down
	# from selenium.webdriver.support.ui import Select
	# //div[contains(@class,'et_pb_blurb_description')]//select

	# checkout //input[contains(@value,'Bike')]


	# select.select_by_index()
	# select.select_by_value()
	# select.select_by_visible_text()

	# refresh page


	# iterate through the table


except Exception as e:
	print("Exception(): " + str(e))

finally:

	# close the web-browser
	driver.close()

	# Quit the driver
	driver.quit()


	# //input[@type='search' and @class='et-search-field']

	# //div[@id='left-area']//article
	# //div[@id='left-area']//article[1]//h2
