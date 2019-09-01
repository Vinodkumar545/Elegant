import json
import pytest

def get_parameters(tc_id):

	with open('test_data.json', 'r') as readfile:
		data = json.load(readfile)

	list_of_tc_params = []
	for params, value in data[tc_id].items():
		# print(params, value)
		list_of_tc_params.append(value)

	# output return format
	"""
	[
		[tc1_params], 
		[tc2_params], 
		[tc3_params]
	]
	"""
	print(list_of_tc_params)
	return list_of_tc_params

# get_parameters("tc_05")	

def test_01():
	assert True

def test_02():
	assert False

def test_03():
	pytest.skip("Skip this test_03")

def test_04():
	pytest.xfail("This test_04 was expected to fail.")

@pytest.mark.parametrize('a', [2])
def test_05_parameter(a):

	if a > 5:
		assert True

	else:
		assert False

# @pytest.mark.parametrize('a, b', [
# 	(2, 4)
# ])
# def test_02_parameter(a, b):

# 	if a + b > 5:
# 		assert True

# 	else:
# 		assert False

# @pytest.mark.parametrize('a, b', [
# 	(2, 4), 
# 	(5, 6), 
# 	(1, 1)
# ])
# def test_03_parameter(a, b):

# 	if a + b > 5:
# 		assert True

# 	else:
# 		assert False


@pytest.mark.parametrize('a, b', get_parameters('tc_01'))
def test_05_parameter(a, b):

	if a + b > 5:
		assert True

	else:
		assert False



