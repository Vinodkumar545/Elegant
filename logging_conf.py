
from logging.config import dictConfig
import logging


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
			'filename': 'logs',
			# 'mode': 'a'
		}
	},

	'loggers': {
		'logs': {
			'handlers': ['console', 'file'],
			'level': 'DEBUG',
			'propagate': True,
		}
	},
}

dictConfig(LOGGING)
logger = logging.getLogger("logs")

