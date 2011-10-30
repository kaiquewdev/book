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
		pass
	
	def insert(self, name, email, phone):
		pass
		
		
		
