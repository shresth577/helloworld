#! /usr/bin/python3
import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
	def test_list_int(self):
		"""
		Test case to add 2 nos
		"""
		data={23,22}
		result=summation(data)
		self.assertEqual(result,55)

if __name__ == '__main__':
	unittest.main()		
