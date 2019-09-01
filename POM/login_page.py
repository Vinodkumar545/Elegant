from Utilities import settings
import logging
from Utilities import test_base


LOGGER = logging.getLogger(settings.LOG_NAME)


def login_demo99(driver):

	test_base.open_url(driver,settings.APP_URL)
	test_base.set_page_load_timeout(driver)
	test_base.send_keys(driver, "LP_txtbx_username", settings.USER_NAME)
	test_base.send_keys(driver, "LP_txtbx_pwd", settings.PWD)
	test_base.click(driver, "LP_btn_submit")

	manager_id = test_base.get_text(driver,"LP_txt_Mgr_Id")
	#Manger Id : mngr220752
	manager_id = manager_id.replace("Manger Id : ", "")

	if manager_id == settings.USER_NAME:
		return True
	else:
		return False
