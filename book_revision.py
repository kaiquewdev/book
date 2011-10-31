#! /usr/bin/env python
# -*- coding: utf8 -*-

'''
Address Book:
	- Name (Unique), Description: Name of person
	- email (List), Description: List of emails of the person
	- Number (List), Description: List of numbers of the person
'''

import re, pickle, sys

class Book(object):
	def __init__(self):
		#Patterns
		self.data_model = {'name': [], 'email':[], 'phone': []}
		self.book = {}
		self.filename = 'storage.data'
		self.p = {
				'email': '^[a-z,.-_]+@([a-z]{3,})+([\.][a-z]{3})|([\.][a-z]{3}[\.][a-z]{2})$',
				'phone': '^(\(.[0-9]{2}\))|^([0-9]{4})+[\-][0-9]{4}$'
			}
	
	def isemail(self, email):		
		return re.search(self.p['email'], email) and True or False
	
	def isphone(self, phone):
		return re.search(self.p['phone'], phone) and True or False
	
	def set_file(self):
		book = open(self.filename)
		
		if not book:
			book = open(self.filename, 'w')
			pickle.dump(self.data_model, book)
			book.close()
			
			return True
		else:
			return False
	
	def set_book(self):
		#Verifica se o arquivo existir retorna falso, e se não ele cria
		if self.set_file() or not self.set_file():
			book = open(self.filename, 'r')
			
			if book.readline() == '':
				book.close()
				
				book = open(self.filename, 'w')
				pickle.dump(self.data_model, book)
				book.close()
				
				book = open(self.filename)
				self.book = pickle.load(book)
				book.close()
				
				return self.book
			else:
				book = open(self.filename)
				
				if type(pickle.load(book)) == dict:
					book.close()
					
					book = open(self.filename)
					self.book = pickle.load(book)
					book.close()
					
					return self.book
	
	def read(self):
		#For sync with member book
		self.set_book()
		organize = lambda kname, kvalue: kname + ': {0}'.format(kvalue)
		
		if not self.book == {}:
			for i in self.book:
				if i == 'name':
					for j in self.book[str(i)]:
						print organize('Name',j)
				if i == 'email':
					for j in self.book[str(i)]:
						print organize('Email',j)
				if i == 'phone':
					for j in self.book[str(i)]:
						print organize('Phone Number',j)
		
	
	def insertion(self, info):
		#For sync with member book
		self.set_book()
		
		info = info.strip(',')
		
		self.book['name'].append(info[0])
		self.book['email'].append(info[1])
		self.book['phone'].append(info[2])
		
		if info[0].isalpha() and self.isemail(info[1]) and self.isphone(info[2]):
			book = open(self.filename, 'w')
		
			if pickle.dump(self.book, book):
				return True
		else:
			return False
		
		book.close()
		
#Arguments of cli
args = sys.argv

if args[1] == '--insert': 
	new_member = Book()
	
	if args[2]:
		new_member.insertion(args[2])
		print 'Insertion is Done!'
	else:	
		print 'Oops, error for insertion!'

if args[1] == '--read': 
	show_member = Book()
	
	show_member.read()






