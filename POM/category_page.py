from Utilities import settings
import logging
from Utilities import test_base
import time


LOGGER = logging.getLogger(settings.LOG_NAME)


def selecting_dresses(driver,quantity):

	test_base.click(driver,"CP_btn_women")
	test_base.click(driver,"CP_link_casual_dresses")
	test_base.click(driver,"CP_chkbx_medium")
	test_base.click(driver,"CP_img_picture")
	test_base.send_keys(driver,"CP_txtbx_qty",quantity)
	test_base.click(driver,"CP_btn_add_to_cart")
	test_base.click(driver,"CP_btn_proceed_chk_out_first_page")
	test_base.click(driver,"CP_btn_proceed_chk_out_second_page")
	test_base.click(driver,"CP_btn_proceed_chk_out_third_page")
	test_base.click(driver,"CP_chkbx_terms_of_service")
	test_base.click(driver,"CP_btn_proceed_chk_out_fourth_page")
	test_base.click(driver,"CP_link_payment_option")
	test_base.click(driver,"CP_btn_confirm_order")