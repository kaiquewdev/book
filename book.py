#! /usr/bin/env python
# -*- coding: utf8 -*-

'''
Address Book:
	- Name (Unique), Description: Name of person
	- email (List), Description: List of emails of the person
	- Number (List), Description: List of numbers of the person
'''
import os, sys, pickle, re

class Book(object):
	'''
	Init pattern variables.
	'''
	def __init__(self):
		self.data_model = {'name': [], 'email':[], 'phone': []}
		self.book = {}
		self.filename = 'storage.data'
		self.p = {
				'email': '^[a-z,.-_]+@([a-z]{3,})+([\.][a-z]{3})|([\.][a-z]{3}[\.][a-z]{2})$',
				'phone': '^(\(.[0-9]{2}\))|^([0-9]{4})+[\-][0-9]{4}$'
			}
	
	'''
	Verify if is a email address.
	'''
	def isemail(self, email):		
		return re.search(self.p['email'], email) and True or False
	
	'''
	Verify if is a phone number.
	'''
	def isphone(self, phone):
		return re.search(self.p['phone'], phone) and True or False
	
	'''
	Create a file if no exit in three folder of program.
	'''
	def create_file(self, filename=''):
		if filename:		
			if not os.path.exists(filename):
				my_file = open(filename, 'w')
				my_file.close()
				return True
			else:
				return False
	
	'''
	Set the file with content default, for manipulating.
	'''
	def set_file(self, filename='', addrs={}):
		if filename and addrs:
			my_book = open(filename)

			if my_book or my_book.readline() == '':
				my_book = open(filename, 'w')
				pickle.dump(addrs, my_book)
				my_book.close()
				return True
			
	'''
	Set the book object with file data.
	'''
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
		        	
	'''
	Read all members registered in book.
	'''
	def read(self):
		if self.book:
			if not self.book == {}:
				name = self.book['name']
				email = self.book['email']
				phone = self.book['phone']
				c = 0
				
				print '| Name | Email | Phone |'
				print '-'*30
				print ''
				while True:
					# Print member
					print '[ {0}, {1}, {2} ]'.format(name[c], email[c], phone[c])
					c += 1
					if c == len(name) and c == len(email) and c == len(phone):
						break
	'''
	Find a item in you book of contact.
	'''
	def find(self, keyword=None):
		if keyword:
			if self.book:
				if not self.book == {}:
					name = self.book['name']
					email = self.book['email']
					phone = self.book['phone']
					c = 0
					itens = []
					
					while True:
						if (keyword in name[c]) or (keyword in email[c]) or (keyword in phone[c]):
							print '[ {0}, {1}, {2} ]'.format(name[c], email[c], phone[c])
							#return True
						c += 1		
	'''
	Refresh the file with content of book
	'''
	def save_in_file(self, filename='', addrs={}):
		if filename or addrs:
			my_book = open(filename, 'w')
			pickle.dump(addrs, my_book)
			my_book.close()
			
			return True
	
	'''
	Inesert a member in or book and update file.
	'''
	def insertion(self, filename='', addrs={}):
		addrs = addrs.split(',')
		name = self.book['name']
		email = self.book['email']
		phone = self.book['phone']
		
		addrs[1] = addrs[1].strip()
		addrs[2] = addrs[2].strip()

		if filename and addrs:
			if addrs[0].isalpha() and self.isemail(addrs[1]) and self.isphone(addrs[2]):
				if type(self.book) == dict:
					name.append(addrs[0])
					email.append(addrs[1])
					phone.append(addrs[2])
					
					if self.save_in_file(self.filename, self.book):
						return True

'''
Init all methods for execute program.
'''
if __name__ == '__main__':
	init = Book()
	# if file was created and formated
	if init.create_file(init.filename):
		init.set_file(init.filename, init.data_model)
		
	init.set_book(init.filename)
	# Arguments of system.
	args = sys.argv
	
	if len(args) > 1:
		if args[1]:
			if args[1] == '--insert':
				if len(args) < 3:	
					print 'Oops, error for insertion!'
				elif args[2]:
					if init.insertion(init.filename, args[2]):
						print 'Insertion is Done!'
					else:
						print 'Error in insertion!'

			if args[1] == '--read': 
				#Read book address
				print '-'*30
				print 'Your book of contacts:'
				print '-'*30
				init.read()
			if args[1] == '--find':
				if len(args) < 3:
					print 'Try input the keyword!'
				elif args[2]:
					print 'Searched by: {0}'.format(args[2])
					print '-'*30
					init.find(args[2])






