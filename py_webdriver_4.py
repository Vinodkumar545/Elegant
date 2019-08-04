
import test_base

import logging_conf
import logging

LOGGER = logging.getLogger('logs')

URL = "https://www.mercurytravels.co.in/"

driver = test_base.activate_driver('chrome')

try:

	test_base.maximize_window(driver)

	test_base.open_url(driver, URL)

	test_base.implicitly_wait(driver)

	test_base.set_page_load_timeout(driver)

	test_base.get_title(driver)

	test_base.click(driver,"MHP_btn_flights")

	test_base.send_keys(driver,"MHP_txt_frmcity",'bangalore')

	test_base.send_keys(driver,"MHP_txt_tocity",'delhi')

	test_base.click(driver,"MHP_btn_srhflights")

except Exception as e:
	
	LOGGER.exception("PY_webdriver_4 | exception %s"%(e))

finally:

	driver.close()

	driver.quit()

	
