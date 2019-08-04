
import test_base

URL = "https://www.ultimateqa.com/simple-html-elements-for-automation/"

driver = test_base.activate_driver('chrome')

test_base.maximize_window(driver)

test_base.open_url(driver, URL)

test_base.implicitly_wait(driver)

test_base.set_page_load_timeout(driver)

test_base.get_title(driver)

test_base.click(driver, "HP_btn_id1")

test_base.back(driver)

test_base.send_keys(driver, "HP_txtbx_name", 'john')

test_base.send_keys(driver, "HP_txtbx_email", 'john.beatles@gmail.com')

test_base.click(driver, "HP_btn_emailme")

