from setuptools import setup

with open("README.md", "r", encoding='utf-8') as fh:
	long_description = fh.read()

setup(
	name='tele-bot-push',
	version='0.0.2',
	author='BuGTEa',
	author_email='noreply@sir7878.com',
	url='https://github.com/BuGTEa/Telegram-Bot-push',
	long_description=long_description,
	long_description_content_type="text/markdown",
	description='Telegram机器人发送消息',
	packages=['telegram_bot_push'],
	install_requires=['requests'],
)
