# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:50:08 2013

@author: akels
"""
class Person:
	def __init__(self, name):
		self._name = name
		print(self.name.setter)
	
	@property
	def name(self):
		"name property docs"
		print('fetch...')
		return self._name
		

	@name.setter
	def name(self, value):
		print('change...')
		self._name = value
	
	@name.deleter
	def name(self):
		print('remove...')
		del self._name

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-'*20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)
# name = property(name)
# name = name.setter(name)
# name = name.deleter(name)
# bob has a managed attribute
# Runs name getter (name 1)
# Runs name setter (name 2)
# Runs name deleter (name 3)
# sue inherits property too
# Or help(Person.name)