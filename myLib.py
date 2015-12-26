#!/usr/bin/python
#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib2, requests, datetime, urllib
import re, codecs

def saveLog(word, r_type, error):
	f = codecs.open('log.txt','a','utf-8')
	time = datetime.datetime.now()
	f.write(str(time)+'\t'+unicode(word)+'\t'+unicode(r_type)+'\t'+unicode(error)+'\n')
	f.close()

def makeListData(listData):
	result_list = []
	for i in xrange(len(listData)):
		result_list.append(listData[i].strip())
	return result_list

def downloadImg(img):
	web_url = 'http://nhgo.net/resource/soda-utf8-hex/'+img+'.gif'
	local_url = 'image/'+img+'.gif'
	urllib.urlretrieve(web_url, local_url)
	return local_url

def downloadIspeechAudio(word, speed):
	"""speed = 0 => normal, speed > 0 => fast"""
	web_url = 'http://www.ispeech.org/p/generic/getaudio?text='+word.encode('utf-8')+'&voice=jpjapanesefemale&speed='+str(speed)+'&action=convert'
	local_url = 'audio/speed_'+str(speed)+'/'+word+'.mp3'
	urllib.urlretrieve(web_url, local_url)
	return local_url