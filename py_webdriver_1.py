
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

URL = "https://www.ultimateqa.com/simple-html-elements-for-automation/"

# initialize Chrome Driver
driver = webdriver.Chrome()
# driver = webdriver.Firefox()


def get_text_after_click_and_back_to_home_page(driver):

	try:
		print(driver.find_element_by_xpath("//h1[@class='entry-title']").text) # Button success
	except:
		print(driver.find_element_by_xpath("//h1[contains(text(),'World Class Courses')]").text) # World Class Courses

	# Goes one step backward in the browser history.
	driver.back()
	print("Home Page Text:", driver.find_element_by_tag_name('h3').text)


try:
	# print the driver
	print("Driver: " + str(driver))

	# know the session id of the Chrome driver
	print("Driver Session ID:" + str(driver.session_id))

	# Returns the name of the underlying browser for this instance.
	print("Driver Name: " + driver.name)

	# Maximizes the current window that webdriver is using
	driver.maximize_window()

	# Loads a web page in the current browser session.
	driver.get(URL)

	# Gets the URL of the current page.
	print("URL: " + driver.current_url)

	# Set the amount of time to wait for a page load to complete before throwing an error.
	driver.set_page_load_timeout(60)

	# Sets a sticky timeout to implicitly wait for an element to be found
	# This method only needs to be called one time per session
	driver.implicitly_wait(10)

	# Returns the title of the current page.
	print("Title: " + driver.title)

	# Get text of webelement
	print("Home Page Text:", driver.find_element_by_tag_name('h3').text)

	# Python sleep() is a method of python time module
	time.sleep(2)

	"""
	Location **Single Elements:

	find_element_by_id
	find_element_by_name
	find_element_by_xpath
	find_element_by_link_text
	find_element_by_partial_link_text
	find_element_by_tag_name
	find_element_by_class_name
	find_element_by_css_selector

	"""
	print("find_element_by_id()")
	driver.find_element_by_id('idExample').click()
	get_text_after_click_and_back_to_home_page(driver)

	# print("***********************")
	# print("find_elements_by_name()")
	# driver.find_element_by_name('button1').click()
	# get_text_after_click_and_back_to_home_page(driver)
	

	# print("***********************")
	# print('find_element_by_xpath')
	# driver.find_element_by_xpath("//button[@id='button2']").click()
	# get_text_after_click_and_back_to_home_page(driver)

	# print("**********************")
	# print("find_element_by_link_text()")
	# driver.find_element_by_link_text('Click me using this link text!').click()
	# get_text_after_click_and_back_to_home_page(driver)

	# print("***********************")
	# print("find_element_by_partial_link_text")
	# driver.find_element_by_partial_link_text('Clickable').click()
	# get_text_after_click_and_back_to_home_page(driver)

	# print("***********************")
	# print("find_element_by_tag_name")
	# print(driver.find_element_by_tag_name('h3').text)

	# print("************************")
	# print("find_element_by_class_name()")
	# print(driver.find_element_by_class_name('buttonClass').location)
	# try:
	# 	driver.find_element_by_class_name('buttonClass').click()
	# except:
	# 	driver.execute_script("arguments[0].click();", click_ele)
	
	# get_text_after_click_and_back_to_home_page(driver)

	# print("************************")
	# print("find_element_by_css_selector")
	# driver.find_element_by_css_selector('#idExample').click()
	# get_text_after_click_and_back_to_home_page(driver)


	print("*****************")
	submit_ele = driver.find_elements_by_xpath("//button[@type='submit']")

	print(type(submit_ele))
	print(len(submit_ele))

	# for ele in submit_ele:
	# 	# print(type(ele))
	# 	ele.click()
	# 	get_text_after_click_and_back_to_home_page(driver)

	"""
	Apart from the public methods given above, there are two private methods which might be useful with locators in page objects. 
	These are the two private methods: find_element and find_elements.
	
	ID = "id"
	XPATH = "xpath"
	LINK_TEXT = "link text" q
	PARTIAL_LINK_TEXT = "partial link text"
	NAME = "name"
	TAG_NAME = "tag name"
	CLASS_NAME = "class name"
	CSS_SELECTOR = "css selector"

	"""

	driver.find_element(By.XPATH, "//button[@id='button2']").click()
	driver.find_elements(By.XPATH, "//button[@type='submit']").click()
	locator = ['tag name', 'h3']
	
	# driver.find_elements(By.TAG_NAME, "h3")

	driver.find_elements(locator[0], locator[1])


except Exception as e:
	print("Exception(): " + str(e))

finally:

	# close the web-browser
	driver.close()

	# Quit the driver
	driver.quit()


"""
To find multiple elements (these methods will return a list):

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector

"""


