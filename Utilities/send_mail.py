
# article: https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from xml.dom import minidom
import smtplib
from Utilities import settings

def trigger_email():
	subject = 'test email worked'
	body = "Hey, what's up? This is test email.\n\n- You"

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)

	try:
	    server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
	    server.ehlo()
	    server.starttls()
	    server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
	    server.sendmail(settings.SEND_FROM, settings.MAIL_TO, email_text)
	    server.close()

    # # add attachment to the body
# # file_attachment = open(file_path, 'rb')
# # part = MIMEBase('application', 'octet-stream')
# # part.set_payload((file_attachment).read())
# # email.encoders.encode_base64(part)
# # part.add_header('Content-Disposition', "attachment; filename= %s" % new_filename)
# # MESSAGE.attach(part)
except Exception as e:
    print('Something went wrong...'%(e))

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





