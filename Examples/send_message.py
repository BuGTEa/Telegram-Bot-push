from telegram_bot_push.bot import BOT


def main(token):
	bot = BOT(token, proxy=True)
	bot.send_text_message('840262289:AAGWIerrFsDTle1nO_tjRT9_N93LyOFB5OU')


if __name__ == "__main__":
	main("840262289:AAGWIerrFsDTle1nO_tjRT9_N93LyOFB5OU")
