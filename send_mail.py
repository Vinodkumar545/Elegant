
# article: https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib

sent_from = 'testelegant@gmail.com'
to = ['vinodkumar.kouthal@gmail.com']
subject = 'test email worked'
body = "Hey, what's up? This is test email.\n\n- You"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

SMTP_USERNAME = "xxx@gmail.com"
SMTP_PASSWORD = "gmailpasswordhere"

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(sent_from, to, email_text)
    server.close()
except Exception as e:
    print('Something went wrong...'%(e))

# ## settings
# SMTP_HOST = "smtp.gmail.com"
# SMTP_PORT = 587
# SMTP_USERNAME = 'vinodkumar.kouthal@gmail.com'
# SMTP_PASSWORD = "Vinodk@14"


# subject = "Test Email"
# MAIL_TO = "vinodkumar.kouthal@stride.ai"
# MAIL_FROM = "testelegant@gmail.com"

# body = """
# Hello team,

# <p> this is an test email.</p>

# <p>Regards,</br>
# Test Team</p>
# """

# MESSAGE = MIMEMultipart('alternative')
# MESSAGE['subject'] = subject
# MESSAGE['To'] = ', '.join(MAIL_TO)
# MESSAGE['From'] = MAIL_FROM

# HTML_BODY = MIMEText(body, 'html')

# # Attach parts into message container.
# MESSAGE.attach(HTML_BODY)

# # The actual sending of the e-mail
# server = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
# # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.ehlo()

# # add attachment to the body
# # file_attachment = open(file_path, 'rb')
# # part = MIMEBase('application', 'octet-stream')
# # part.set_payload((file_attachment).read())
# # email.encoders.encode_base64(part)
# # part.add_header('Content-Disposition', "attachment; filename= %s" % new_filename)
# # MESSAGE.attach(part)


# server.starttls()
# server.login(SMTP_USERNAME, SMTP_PASSWORD)
# server.sendmail(MAIL_FROM, (MAIL_TO), MESSAGE.as_string())
# server.quit()
