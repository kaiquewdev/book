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
	
	def set_file(self, filename='', addrs={}):
	    if filename and addrs:
	        my_book = open(filename)

            if not my_book or my_book.readline() == '':
                my_book = open(filename, 'w')
                pickle.dump(addrs, my_book)
                my_book.close()
                
                return True

	def set_book(self, filename=''):
	    if filename:
		        my_book = open(filename)
		        
		        if not my_book.readline() == '':
		        	my_book = open(filename)
		        	self.book = pickle.load(my_book)
		        	my_book.close()
		        	
		        	if not self.book == {}:
						return True
		        else:
		        	return False
		        	
	def read(self):
#		For sync with member book
		if self.book:
			if not self.book == {}:
				for i in self.book:
					if i == 'name':
						for j in self.book[str(i)]:
							print 'Name: {0}'.format(j)
					elif i == 'email':
						for j in self.book[str(i)]:
							print 'Email: {0}'.format(j)
					elif i == 'phone':
						for j in self.book[str(i)]:
							print 'Phone: {0}'.format(j)
	
	def save_in_file(self, filename='', addrs={}):
		if filename or addrs:
			my_book = open(filename, 'w')
			pickle.dump(addrs, my_book)
			my_book.close()
			
			return True
	
	def insertion(self, filename='', addrs={}):
		#For sync with member book
		addrs = addrs.split(',')
		addrs[1] = addrs[1].strip()
		addrs[2] = addrs[2].strip()
		
		import pdb; pdb.set_trace()
		if filename and addrs:
			if addrs[0].isalpha() and self.isemail(addrs[1]) and self.isphone(addrs[2]):
				if type(self.book) == dict:
					self.book['name'].append(addrs[0])
					self.book['email'].append(addrs[1])
					self.book['phone'].append(addrs[2])
					if self.save_in_file(self.filename, self.book):
						return True

if __name__ == '__main__':
	init = Book()
	init.set_file(init.filename, init.data_model)
	init.set_book(init.filename)
	#Arguments in CLI
	args = sys.argv

	if args[1]:
		if args[1] == '--insert':
			if args[2]:
				if init.insertion(init.filename, args[2]):
					print 'Insertion is Done!'
				else:
					print 'Error in insertion!'
			else:	
				print 'Oops, error for insertion!'

		if args[1] == '--read': 
			#Read book address
			init.read()






