
from selenium import webdriver
import time

URL = "https://www.ultimateqa.com/simple-html-elements-for-automation/"

# initialize Chrome Driver
driver = webdriver.Chrome()

# print the driver


# know the session id of the Chrome driver


# Returns the name of the underlying browser for this instance.


# Maximizes the current window that webdriver is using


# Loads a web page in the current browser session.


# Gets the URL of the current page.


# Set the amount of time to wait for a page load to complete before throwing an error.


# Sets a sticky timeout to implicitly wait for an element to be found
# This method only needs to be called one time per session


# Returns the title of the current page.


# Get text of webelement


# Clicks the element idExample


# Python sleep() is a method of python time module


# Goes one step backward in the browser history.

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

# By Name button1
driver.find_element_by_name('button1').click()
driver.back()

# By Xpath
xpath_ele = "//div[contains(@class,'et_pb_row et_pb_row_3')]//div[contains(@class,'et_pb_css_mix_blend_mode_passthrough et-last-child')]//div[1]//div[1]//div[1]//div[1]//form[1]//button[1]"


# By Link Text Click Me

# By Partial Link Clickable


# By Tag Name h3


# By Class Name buttonClass


# By CSS selector
# css=<HTML tag><#><Value of ID attribute>    button[class='buttonClass']
# tab.classname
# Docs: https://saucelabs.com/resources/articles/selenium-tips-css-selectors



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



"""
Apart from the public methods given above, there are two private methods which might be useful with locators in page objects. 
These are the two private methods: find_element and find_elements.

from selenium.webdriver.common.by import By


ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

"""


# clear() - Clears the text if it’s a text entry element.


# send_keys() - Simulates typing into the element.


# is displayed() - hether the element is visible to a user.


# is selected() - Returns whether the element is selected.


# is enabled() - Returns whether the element is enabled.


# get_attribute() - Gets the given attribute or property of the element.


# location - The location of the element in the renderable canvas.

## Select from drop down
# from selenium.webdriver.support.ui import Select

