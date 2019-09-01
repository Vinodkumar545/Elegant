
from setuptools import setup
from Utilities import settings

setup(
	name = settings.APP_NAME,
	version = settings.APP_VERSION,
	description = settings.APP_DESCP,
	author = settings.APP_AUTHOR,
	author_email = settings.APP_EMAIL,
	url = settings.APP_URL,
	packages =['POM', 'Utilities'],
)