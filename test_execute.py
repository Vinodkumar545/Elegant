import pytest
from POM import login_page
from POM import category_page
from Utilities import xlsx,settings
import logging


LOGGER = logging.getLogger(settings.LOG_NAME)

def get_test_data():
	col_tc_id = 1
	col_tc_desc = 2
	col_tc_user_name = 3
	col_tc_pwd = 4
	col_tc_category = 5
	col_tc_dresses = 6
	col_tc_size = 7
	col_tc_quantity = 8
	col_tc_prize = 9
	workbook = xlsx.load_excel("testdata.xlsx")
	sheet_name = "Scenarios"
	row_length = xlsx.get_row_length(workbook,sheet_name)

	testdata_info = []

	for row in range(2,row_length+1):
		tc_id = xlsx.read_cell(workbook,sheet_name,row,col_tc_id)
		tc_desc = xlsx.read_cell(workbook,sheet_name,row,col_tc_desc)
		tc_user_name = xlsx.read_cell(workbook,sheet_name,row,col_tc_user_name)
		tc_pwd = xlsx.read_cell(workbook,sheet_name,row,col_tc_pwd)
		tc_category = xlsx.read_cell(workbook,sheet_name,row,col_tc_category)
		tc_dresses = xlsx.read_cell(workbook,sheet_name,row,col_tc_dresses)
		tc_size = xlsx.read_cell(workbook,sheet_name,row,col_tc_size)
		tc_quantity = xlsx.read_cell(workbook,sheet_name,row,col_tc_quantity)
		tc_prize = xlsx.read_cell(workbook,sheet_name,row,col_tc_prize)

		testdata_info.append({
			"tc_id" : tc_id,
			"tc_desc" : tc_desc,
			"tc_user_name" : tc_user_name,
			"tc_pwd" : tc_pwd,
			"tc_category" : tc_category,
			"tc_dresses" : tc_dresses,
			"tc_size" : col_tc_size,
			"tc_quantity" : tc_quantity,
			"tc_prize" : tc_prize
			#category
			})
	return testdata_info

#print(get_test_data())

@pytest.mark.parametrize("testdata",get_test_data())
def test_login_to_automation_practice(driver,testdata):
	LOGGER.info("%s"%(testdata))
	assert login_page.login_your_logo(driver,testdata['tc_user_name'],testdata['tc_pwd']) is True
	#write another function to select cateogory to accpt arguments

@pytest.mark.parametrize("testdata",get_test_data())
def test_select_the_dresses_from_automation_practice(driver,testdata):
	LOGGER.info("%s"%(testdata))
	category_page.selecting_dresses(driver)