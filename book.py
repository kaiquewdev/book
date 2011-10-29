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
		#Addresses
		f = file('storage.data','rb')
		f = pickle.load(f)
		
		if f == {}:
			self.addrs = {'name': [], 'phone': [], 'email': []}
		#Patterns
		self.p = {
				'email': '^[a-z,.-_]+@([a-z]{3,})+([\.][a-z]{3})|([\.][a-z]{3}[\.][a-z]{2})$',
				'phone': '^(\(.[0-9]{2}\))|^([0-9]{4})+[\-][0-9]{4}$'
			}
	
	def isemail(self):		
		return re.search(self.p['email'], self.email) and True or False
	
	def isphone(self):
		return re.search(self.p['phone'], self.phone) and True or False
	
	def make_book(self):
		f = file('storage.data','w')
		if pickle.dump(self.addrs, f):
			f.close()
			return True
		
	def read_book(self):
		f = open('storage.data')
		book_addrs = pickle.load(f) 
		
		if book_addrs:
			return book_addrs  
	
	def insert(self, *information):
		self.name = information[0]
		self.email = information[1]
		self.phone = information[2]
		
		if self.name.isalpha() and self.isemail() and self.isphone():
			self.addrs['name'].append(self.name)
			self.addrs['email'].append(self.email)
			self.addrs['phone'].append(self.phone)
			
			if self.make_book():
				return True

if sys.argv[1] == '--insert' or sys.argv[1] == '-i':
	new_addrs = Book().insert('Caio','caio@teste.com','5555-5555')
	if new_addrs:
		print 'Name: {0}, Email: {1}, Phone: {2}, Inserted!'.format(new_addrs.name, new_addrs.email, new_addrs.phone)
		
if sys.argv[1] == '--read' or sys.argv[1] == '-r':
	book = Book()
	if book:
		book = book.read_book()		
		line = lambda x,n: x*n
		print 'Existent:'
		
		print line('-',45)
		
		for name in book['name']:
			print 'Name: {0},'.format(name)
		
		for email in book['email']:
			print 'Email: {0},'.format(email)
	
		for phone in book['phone']:
			print 'phone: {0}'.format(phone)
		
		
		
