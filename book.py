#! /usr/bin/env python
# -*- coding: utf8 -*-

'''
Address Book:
	- Name (Unique), Description: Name of person
	- email (List), Description: List of emails of the person
	- Number (List), Description: List of numbers of the person
'''

import re

class Book(object):
	def __init__(self, name, email, number):
		self.name = name
		self.email = email
		self.phone = number
		#Addresses
		self.addrs = {'name': [], 'phone': [], 'email': []}
		#Patterns
		self.p = {
				'email': '^[a-z,.-_]+@([a-z]{3,})+([\.][a-z]{3})|([\.][a-z]{3}[\.][a-z]{2})$',
				'phone': '^(\(.[0-9]{2}\))|^([0-9]{4})+[\-][0-9]{4}$'
			}
	
	def isemail(self, email):		
		return re.search(self.p['email'], email) and True or False
	
	def isphone(self, phone):
		return re.search(self.p['phone'], phone) and True or False
	
	def insert(self):
		if self.name and self.email and self.phone:
			if self.name.isalpha() and self.isemail(self.name) and self.isphone(self.phone):
				self.addrs['name'].append(self.name)
				self.addrs['email'].append(self.email)
				self.addrs['phone'].append(self.phone)
				
				print 'Name: {0}, Email: {1}, Phone: {2}, Inserted!'.format(self.name, self.email, self.phone)
				return True
			elif self.name:
				print 'Field name is necessary!'
				return False
			elif self.isemail(self.email):
				print 'Field not corresponding correctly with a email!'
				return False
			elif self.isphone(self.phone):
				print 'Field not corresponding correctly with a phone number!'
				return False
		elif self.email:
			print 'Field email is necessary!'
			return False
		elif self.phone:
			print 'Field phone number is necessary!'
			return False
			
