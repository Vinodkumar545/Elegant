import pytest
from POM import login_page


def test_to_verify_login_to_demo99(driver):
	assert login_page.login_demo99(driver) == True

	

		