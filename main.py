#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
from myPath import *
sys.path.insert(0, applicationPath())

from myLib import *
from sysclass import *

class Crawler():
	def __init__(self):
		connection = DBConnection()
		self.db = connection.db
		self.collection = None
		self.doc = None
		pass

	def crawlWordAudio(self):
		self.collection = self.db.stardict
		word_num = self.collection.count()
		for i in xrange(word_num):
			self.doc = self.collection.find().limit(1).skip(i).next()
			if self.doc["status"] == 1:
				continue
			word = self.doc["word"]
			print '=========> i = ', i, word
			wordData = Audio(word).crawlIspeechAudio()
			###################################
			collection = self.db.audio
			collection.insert_one(wordData)
			self.doc["status"] = 1
			self.collection.replace_one({"word":word},self.doc)

class Audio():
	def __init__(self, word):
		self.word = word
		self.data = {}
		self.status = 0
		self.audio = None
		self.audioSpeed = 0

	def crawlIspeechAudio(self):
		self.audio = downloadIspeechAudio(self.word, self.audioSpeed)
		self.dataBuilder()
		return self.data

	def dataBuilder(self):
		self.data["word"] = self.word
		self.data["status"] = self.status
		self.data["audio"] = self.audio
		self.data["speed"] = self.audioSpeed

if __name__ == "__main__":
	crawler = Crawler()
	crawler.crawlWordAudio()
	pass