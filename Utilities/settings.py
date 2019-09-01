
from logging.config import dictConfig
import logging
import os


APP_URL = "http://demo.guru99.com/V4/"

USER_NAME = "mngr220752"

PWD = "syzyrUz"

APP_NAME = "TESTING"

APP_VERSION = "7"

APP_DESCP = "description"

APP_AUTHOR = "Hina"

APP_EMAIL = "hinak406@gmail.com"

LOG_NAME = "testlogs.log"

NODE_URL = "http://127.0.0.1:4444/wd/hub"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OBJECT_REPO = os.path.join(BASE_DIR, "Utilities", "object_repo.ini")



###################Email Configuration#####################################

SMTP_HOST = "smtp.gmail.com"

SMTP_PORT = 587

SEND_FROM = ""

MAIL_TO = ['hinak406@gmail.com']

SMTP_USERNAME = "xxx@gmail.com"

SMTP_PASSWORD = "gmailpasswordhere"


###################Logging Configuration#######################################

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,

	'formatters': {
		'verbose': {
			'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
		}
	},

	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
			'level': 'DEBUG',
			'formatter': 'verbose',
		},
		'file': {
			'class': 'logging.FileHandler',
			'level': 'DEBUG',
			'formatter': 'verbose',
			'filename': LOG_NAME
			# 'mode': 'a'
		}
	},

	'loggers': {
		LOG_NAME: {
			'handlers': ['console', 'file'],
			'level': 'DEBUG',
			'propagate': True,
		}
	},
}

dictConfig(LOGGING)
logger = logging.getLogger(LOG_NAME)
