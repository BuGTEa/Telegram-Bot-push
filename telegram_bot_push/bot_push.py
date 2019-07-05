import requests as rq
from .small_functions import *


def bot_push_message(text, base_url, chat_id, proxy):
	url = base_url + "sendMessage"
	message = {'chat_id': chat_id, 'text': text}
	a = rq.get(url, message, proxies=proxy)
	return check_status(a, 'send text message')


def bot_push_photo_url(photo_url, base_url, chat_id, **kwargs):
	url = base_url + "sendPhoto"
	message = {'chat_id': chat_id, 'photo': photo_url}
	message.update(kwargs)
	a = rq.get(url, message)
	return a.json()


def bot_push_document_url(document_url, base_url, chat_id, **kwargs):
	url = base_url + "sendDocument"
	message = {'chat_id': chat_id, 'document': document_url}
	message.update(kwargs)
	a = rq.get(url, message)
	return a.json()

