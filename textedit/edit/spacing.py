#!/usr/bin/env python

"""Changes spacing from single to double space for a given file.
Outputs the new file as filename_double_spaced.txt or
filename_single_spaced.txt as needed. 
"""
import sys
import re

class Spacing(object):


	def __init__(self, filename):

		self.filename = filename


	def open_file(self,filename):
		"""Opens a file object to be used across the class"""
		with open(filename,'r') as f:
			file_contents = f.read()
			return file_contents

	def single_to_double(self):
		"""Converts from single to double space after a period"""
		try: 
			file_contents = self.open_file(self.filename)
			with open('%s_double_spaced.txt' % filename,  'w')  as output:
				output.write(file_contents.replace(r'\.\s{1}', r'\.\s{2}'))
		except AssertionError:
			print("Single space not found")

	def double_to_single(self):
		"""Converts from double to single space after a period"""
		try: 
			file_contents = self.open_file(self.filename)
			with open('%s_single_spaced.txt' % filename , 'w') as output:
				output.write(file_contents.replace(r'\.\s{2}', r'\.\s{1}'))
		except AssertionError:
			print("Double space not found")

	def spacking_check(self):
		"""simple check to see if file is single or double spaced and refereces it to the opposite"""	
		if len(re.findall(r'\.\s{2}', self.filename)) > 1 :
			self.double_to_single()
		else:
			self.single_to_double()

if __name__ == '__main__':
	filename = sys.argv[1]
	sp = Spacing(filename)
	Spacing.spacking_check(sp)
