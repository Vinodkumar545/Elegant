

from selenium.webdriver.common.touch_actions import TouchActions
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
	# print(driver.find_element_by_xpath("//h4[contains(text(),'Advanced Controls')]").is_displayed())	

	# # locator = py_obj_property.locator("HP_txt_advcont")
	# # d = driver.find_element(locator[0], locator[1]).is_displayed()
	# # print(d)

	# # Highlight webelement
	# highlight_ele = driver.find_element_by_xpath("//h4[contains(text(),'Click button using ClassName')]")
	# driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", highlight_ele)


	# # is selected() - Returns whether the element is selected.
	# driver.find_element_by_xpath("//input[@type='radio' and @value='male']").click()
	# print(driver.find_element_by_xpath("//input[@type='radio' and @value='male']").is_selected())

	# # is enabled() - Returns whether the element is enabled.
	# print(driver.find_element_by_xpath("//button[@class='buttonClass']").is_enabled())

	# # get_attribute() - Gets the given attribute or property of the element.
	# print(driver.find_element_by_xpath("//a[@data-shared='sharing-twitter-909']").get_attribute('title'))

	# # location - The location of the element in the renderable canvas.
	# l = driver.find_element_by_xpath("//h4[contains(text(),'Dropdown')]").location
	# dd_ele = driver.find_element_by_xpath("//h4[contains(text(),'Dropdown')]")

	# xoffset = l['x']
	# yoffset = l['y']
	# print('xoffset: ' + str(xoffset))
	# print('yoffset: ' + str(yoffset))

	# try:
	# 	# TouchActions(driver).scroll_from_element(dd_ele, xoffset, yoffset)
	# 	driver.execute_script("arguments[0].scrollIntoView(true);", dd_ele)
	# 	print("Scroll sucessfully.")
	# except Exception as e:
	# 	print("scroll exceptiion" + str(e))

	# time.sleep(10)

	# scroll_into_view
	# //h4[contains(text(),'Checkboxes')]
	

	## Select from drop down
	# from selenium.webdriver.support.ui import Select
	
	# ele = driver.find_element_by_xpath("//div[contains(@class,'et_pb_blurb_description')]//select")
	# driver.execute_script("arguments[0].scrollIntoView(true);", ele)

	# time.sleep(3)

	# select = Select(ele)
	# select.select_by_index(1)

	# time.sleep(5)


	# select.select_by_value('opel')
	
	# time.sleep(5)

	# select.select_by_visible_text('Audi')

	# time.sleep(5)


	# # checkout //input[contains(@value,'Bike')]


	# # select.select_by_index()
	# # select.select_by_value()
	# # select.select_by_visible_text('Opel')

	# # refresh page
	# driver.refresh()


	# iterate through the table

	no_of_rows = driver.find_elements_by_xpath("//table[@id='htmlTableId']//tr")
	no_of_cols = driver.find_elements_by_xpath("//table[@id='htmlTableId']//tr[1]//th")

	print("no_of_rows: " + str(len(no_of_rows)))
	print('no_of_cols: ' + str(len(no_of_cols)))

	for i in range(1, len(no_of_rows) + 1):

		for j in range(1, len(no_of_cols) + 1):

			if i == 1:

				print(driver.find_element_by_xpath("//table[@id='htmlTableId']//tr[%s]//th[%s]"%(i, j)).text)


			else:

				print(driver.find_element_by_xpath("//table[@id='htmlTableId']//tr[%s]//td[%s]"%(i, j)).text)


		print("******************************************")


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
