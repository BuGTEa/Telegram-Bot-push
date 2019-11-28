import requests as rq
import sqlite3
from .bot_push import *


class BOT:
	def __init__(self, token=None, proxy=False, proxy_ip='127.0.0.1', proxy_port=10808, proxy_type='socks5'):
		self.proxy = proxy
		self.proxy_dict = dict()
		self._generate_proxy_settings(proxy_ip, proxy_port, proxy_type)
		self.token = token
		self.base_url = "https://api.telegram.org/bot"
		self.chat_id = None
		try:
			self._get_chat_id_by_file()
		except:
			self._get_chat_id(self.token)

	def _get_chat_id(self, token=None):
		if token is None:
			token = self.token
		url = f"{self.base_url}{token}/getUpdates"
		a = rq.get(url, proxies=self.proxy_dict)
		if a.status_code != 200:
			return EnvironmentError('cannot get the chat id, please contact support!')
		a = a.json()
		if not a['ok']:
			return ValueError('Get Chat ID Wrong! Please send a message to bot and try it again.')
		else:
			if len(a['result']) == 0:
				return ValueError('Get Chat ID Wrong! Please send a message to bot and try it again.')
			else:
				self.chat_id = a['result'][0]['message']['chat']['id']
				self.save_chat_id_to_sql(self.chat_id)

	def _generate_proxy_settings(self, proxy_ip, proxy_port, proxy_type):
		if self.proxy:
			self.proxy_type = self._validate_proxy_type(proxy_type)
			self.proxy_dict['http'] = f"{self.proxy_type}://{proxy_ip}:{proxy_port}"
			if self.proxy_type == 'socks5':
				self.proxy_dict['https'] = self.proxy_dict['http']
			else:
				self.proxy_dict['https'] = f"https://{proxy_ip}:{proxy_port}"

	update_chat_id = _get_chat_id

	def send_text_message(self, text):
		base_url = f'{self.base_url}{self.token}/'
		result = bot_push_message(text, base_url, self.chat_id, self.proxy_dict)
		return result

	def _get_chat_id_by_file(self):
		with open('chat_id.txt', 'r') as f:
			self.chat_id = f.read()

	@staticmethod
	def save_chat_id_to_sql(chat_id):
		with open('chat_id.txt', 'w+') as f:
			f.write(chat_id)

	@staticmethod
	def _validate_proxy_type(proxy_type):
		if proxy_type.lower() not in ['socks5', 'http']:
			raise TypeError('Proxy Type is not allowed.')
		else:
			return proxy_type.lower()
