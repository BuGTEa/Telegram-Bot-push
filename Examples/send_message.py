from telegram_bot_push.bot import BOT


def main(token):
	bot = BOT(token, proxy=True)
	bot.send_text_message('Your Code')


if __name__ == "__main__":
	main("Your Code")
