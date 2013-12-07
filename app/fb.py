#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
import time
import facebook
from facebook import GraphAPIError
import locale

__author__ = 'Marcus Sümnick <marcus@suemnick.com>'

class FB():

	__page_access_token = None
	__page_access_token_timeout = None
	__fb_page = None

	user_id = ""
	access_token = ""
	page_id = ""
	album_id = ""

	def __init__(self,user_id,access_token,page_id,album_id):
		self.user_id = user_id
		self.page_id = page_id
		self.album_id = album_id
		self.access_token = access_token

	def __connect_user(self):
		return facebook.GraphAPI(self.access_token)

	def __get_access_token_to_page(self):

		if not self.__is_token_timed_out():
			return self.__page_access_token

		res = self.__connect_user().request("/%s"%self.user_id,{"fields":"accounts"})
		accounts = res['accounts']['data']

		for account in accounts:
			if account['id'] == self.page_id:
				self.__page_access_token = account['access_token']
				self.__page_access_token_timeout = datetime.now()+timedelta(minutes=60)
				return self.__page_access_token

	def __is_token_timed_out(self):
		if not self.__page_access_token_timeout:
			return True
		return datetime.now() < self.__page_access_token_timeout

	def __connect_fb_page(self):
		if self.__is_token_timed_out():
			self.__fb_page = facebook.GraphAPI(self.__get_access_token_to_page())
		return self.__fb_page

	def post_menu(self,menu_path,msg=None):

		locale.setlocale(locale.LC_ALL,"de_DE")

		if not msg:
			img_msg = "%s %s" % (time.strftime("Speiseplan für den %A, den %d. %B."),"Guten Appetit!")
		else:
			img_msg = msg

		try:
			self.__connect_fb_page().put_photo(image=open(menu_path), message=img_msg, album_id=self.album_id)
		except GraphAPIError,e:
			print e.message

fb = FB("user_id",
		"token"
		"page_id",
		"album_id")

fb.post_menu("./static/pics/startup/kleineulme/apple-touch-startup-image-640x1096.png")
