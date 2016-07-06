#!/usr/bin/python2
# coding:utf-8

# by ins3c7
# 5 july 2016

# I.A. 02 [Creuza]

import json, os, re, time
from requests import get
from random import choice
from unidecode import unidecode as uni

os.system('clear')

class iabot:
	def __init__(self):
		self.questioned = []
		self.filedb = 'db.ai'

	def add(self):
		print '\n+ put: question /// answer1 # answer2 (...)'
		learn = raw_input('+ ')
		with open(self.filedb, 'a') as w:
			w.write(learn+'\n')
		w.close()

	def learn(self):
		dbase = []
		with open(self.filedb, 'r') as f:
			data = f.readlines()
		for question in data:
			dbase.append([question.split('///')[0], question.split('/// ')[1].split(' # ')])
		return dbase

	def say(self):
		words = []
		dbase = self.learn()
		put = uni(raw_input('> ').decode('utf-8')).upper()
		put = re.sub('[.,?!]', '', put)
		# if put in self.questioned:
		# 	print 'Creuza: de novo?'
		# 	return
		self.questioned.append(put)
		if len(put.split()) < 2:
			if put.find('#ADD') != -1:
				self.add()
				print
			if put.find('KKK') != -1 or put.find('HAHA') != -1:
				print 'Creuza: ha ha ha'
			if put.find('OI') != -1 or put.find('OLA') != -1:
				print 'Creuza: Oi, tudo bem?'
			if put.find('OBRIGAD') != -1:
				print 'Creuza: por nada :)'
			if put.find('PRAZER') != -1:
				print 'Creuza: o prazer é todo seu..'
			if put.find('TCHAU') != -1:
				print 'Creuza: vaza!!'
			if put.find('PORQUE') != -1:
				print 'Creuza: não enche..'
			return
		for question in dbase:
			words = []
			q = question[0].upper()
			q = re.sub('[.,?!]', ' ', q)
			answer = question[1]
			# text = re.split('\W+', q)
			text = q.split()
			for w in text:
				words.append(w)
			confirm = set(put.split()) & set(words)
			if len(confirm) == len(put.split()):
				time.sleep(1)
				print 'Creuza:', choice(answer).rstrip()
				return

bot = iabot()
while True:	bot.say()