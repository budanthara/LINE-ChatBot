# -*- coding: utf-8 -*-

import urllib2
from uagents import *

"""
This is the constant place, do not edit if you are don't understand it.
"""

class Constants:
	def __init__(self):
		self.PATH_KATAMUTIARA = "kata/"
		self.WANCAK_RAND = urllib2.urlopen("http://api-1cak.herokuapp.com/random")
		self.YOUTUBE_CONVERTER = "http://youtubeinmp3.com/fetch/?api=advanced&format=JSON&video="
		#self.REFERER = "http://www.simsimi.com/talk.htm"
		#self.SIMI_REGISTER = "http://www.simsimi.com/func/register"
		self.SIMI_CHAT = "http://app.simsimi.com/app/aicr/request.p?"
		self.MOVIE_PLAYING = "http://apify.herokuapp.com/api/nowplaying21.json"
		self.USER_AGENT_SELECTED = UserAgents().user_agent()
		self.CONST_REFERER = {'Referer':'http://1cak.com/'}
