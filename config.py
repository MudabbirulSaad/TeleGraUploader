from os import environ

class Config(object):
	BOT_TOKEN = environ.get("BOT_TOKEN")

class Text(object):
	WELCOME_TEXT = environ.get("WELCOME_TEXT")
	HELP_TEXT = environ.get("HELP_TEXT")
	MAINTAINER = environ.get("MAINTAINER")