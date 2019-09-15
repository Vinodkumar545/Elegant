from Utilities import settings
import logging
from Utilities import test_base
import time


LOGGER = logging.getLogger(settings.LOG_NAME)


def login_your_logo(driver,user_name,password):

	test_base.open_url(driver,settings.APP_URL)
	test_base.set_page_load_timeout(driver)
	test_base.click(driver,"LP_link_signin")
	test_base.send_keys(driver, "LP_txtbx_email_id",user_name)
	test_base.send_keys(driver, "LP_txtbx_pwd",password)
	test_base.click(driver, "LP_btn_signin")
	time.sleep(10)
 
	if test_base.get_text(driver,"LP_txt_myacnt") == "MY ACCOUNT":
		return True
	else:
		return False