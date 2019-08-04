
import platform
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""
About DesiredCapabilities: https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities

Basically, the DesiredCapabilities help to set properties for the WebDriver. 
A typical usecase would be to set the path for the FirefoxDriver 
if your local installation doesn't correspond to the default settings.
"""

# BROWSER = 'firefox'
BROWSER = 'chrome'

"""
Selenium Standalone

The Selenium Server is needed in order to run Remote Selenium WebDriver. 
"""
NODE_URL = "http://127.0.0.1:4444/wd/hub"

if BROWSER == 'chrome':

	desired_capabilities = DesiredCapabilities.CHROME.copy()
	options = webdriver.ChromeOptions()

	options.add_argument('--headless')
	# options.add_argument('--no-sandbox')
	options.add_argument("start-maximized")

	## To disable the pop-up blocks inorder to continue user action on the app/web-page
	options.add_argument("excludeSwitches")
	options.add_argument("disable-popup-blocking")

	## Below setting to automatically download files from the chrome browser to specified path
	options.add_experimental_option("prefs", {
		  "download.default_directory": r'{}'.format("C:\\Users\\Admin\\Elegant"),  # download file_path
		  "download.prompt_for_download": False,
		  "download.directory_upgrade": True,
		  "safebrowsing.enabled": False,
		  "safebrowsing.disable_download_protection": True,
		})

	desired_capabilities = options.to_capabilities()

	desired_capabilities['browser_version'] = "75.0.3770.142"
	desired_capabilities['platform'] = platform.system()
	desired_capabilities['version'] = platform.version()

	# Instantiate an instance of Remote WebDriver with the desired capabilities.
	driver = webdriver.Remote(command_executor=NODE_URL, desired_capabilities=desired_capabilities)

	driver.get("https://www.ultimateqa.com/simple-html-elements-for-automation/")

	driver.save_screenshot('1.png')


if BROWSER == 'firefox':

	desired_capabilities = DesiredCapabilities.FIREFOX.copy()
	options = webdriver.FirefoxOptions()

	# options.headless = True

	# To know more about set_preference: http://kb.mozillazine.org/Firefox_:_FAQs_:_About:config_Entries
	options.set_preference("browser.download.folderList", 2)
	options.set_preference("browser.download.manager.showWhenStarting", False)
	options.set_preference("browser.download.dir", r'{}'.format("C:\\Users\\Admin\\Elegant"))

	## MIME Type: for .xlsx download files, need to more MIME type as per the type of download
	## MIME Type URL: https://www.freeformatter.com/mime-types-list.html
	options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

	desired_capabilities = options.to_capabilities()

	desired_capabilities['browser_version'] = "68.0.1"
	desired_capabilities['platform'] = platform.system()
	desired_capabilities['version'] = platform.version()

	# Instantiate an instance of Remote WebDriver with the desired capabilities.
	driver = webdriver.Remote(command_executor=NODE_URL, desired_capabilities=desired_capabilities)

	driver.get("https://www.ultimateqa.com/simple-html-elements-for-automation/")

