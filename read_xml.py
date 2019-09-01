from xml.dom import minidom

# # read the xml fie
# mydoc = minidom.parse('xml_output.xml')

# # get the tag name
# # <testsuite errors="0" failures="2" name="pytest" skipped="2" tests="7" time="1.375">
# items = mydoc.getElementsByTagName('testsuite')

# errors = int(items[0].attributes['errors'].value)
# failures = int(items[0].attributes['failures'].value)
# skips = int(items[0].attributes['skipped'].value)
# tests = int(items[0].attributes['tests'].value)
# time_taken = items[0].attributes['time'].value
# print(tests, failures, skips, errors, time_taken)


def get_xml_info(return_info):

	mydoc = minidom.parse('xml_output.xml')
	items = mydoc.getElementsByTagName('testsuite')

	errors = int(items[0].attributes['errors'].value)
	failures = int(items[0].attributes['failures'].value)
	skips = int(items[0].attributes['skipped'].value)
	tests = int(items[0].attributes['tests'].value)
	time_taken = items[0].attributes['time'].value

	if return_info == 'tot_testcases':
		return tests


	if return_info == 'pass_result':
		if failures != 0 and errors != 0 and skips != 0:
			return tests
		else:
			pass_test = tests - failures - errors - skips
			return pass_test

	if return_info == 'fail_result':
		return failures

	if return_info == 'error_result':
		return errors

	if return_info == 'time_taken':
		return time_taken

	if return_info == 'status':
		if errors == 0 and failures == 0:
			return "PASS"

		if failures != 0:
			return "FAIL"

		if errors != 0:
			return "ERROR"

		if skips != 0:
			return "SKIPS"

		else:
			return "NA"

	if return_info == 'subject':
		if errors == 0 and failures == 0:
			return "PASS"

		if failures != 0:
			return "FAIL - " + str(failures) + " tests"

		if errors != 0:
			return "ERROR"

		if skips != 0:
			return "SKIPS"

		else:
			return "NA"

print(get_xml_info("tot_testcases"))
print(get_xml_info("pass_result"))
print(get_xml_info("fail_result"))





