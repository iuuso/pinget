import urllib.request
import logging
import setup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
					level=logging.INFO)

try:
	from telegram.ext import Updater
	from telegram.ext import CommandHandler
except ImportError:
	print("Err: Requirements are missing. Install them with pip:")
	print("'pip3 install -r requirements.txt'")

def get_public_ip():
	return(urllib.request.urlopen('http://ident.me').read().decode('utf8'))

def start(bot, update):	
	message_text = "My public address is " + get_public_ip()
	bot.send_message(chat_id=update.message.chat_id, text=message_text)

def main():
	if setup.bot_token == "":
		print("Your setup.py file is missing the bot token.")
		print("Here are the instructions for acrquiring the token:")
		print("https://core.telegram.org/bots")
		return
	else:
		updater = Updater(token=setup.bot_token)
		dispatcher = updater.dispatcher

		start_handler = CommandHandler('start', start)
		dispatcher.add_handler(start_handler)
		updater.start_polling()

if __name__ == "__main__": main()