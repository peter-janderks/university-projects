# -*- coding: utf-8 -*-
#
# Homework 12
# Filename:  branching
#
#
# Name: Peter-Jan Derks
#

import unittest

def blsort(L):
	
	# empty list is the base case
	if L == []:
		return L

	# if the first binary digit is 0, it's returned infront of the list of which
	# the numbers will be returned one by one recursivly.
	elif L[0] == 0:
		return [0] + blsort(L[1:])

	# if the first binary digit is 1, it's returned behind the list of which
	# numbers will be returned one by one recursivly.
	else:
		return blsort(L[1:]) + [1] 

def gensort(L):

	# empty list is the base case
	if L == []:
		return L

	# finds the maximum integer in the list, removes it from the list and then
	# and returns it behind the list that is yet to be formed recursivly. 
	# (this goes on untill the list is empty)
	else:
		i = max(L)
		L.remove(i)
		return gensort(L) + [i]


def jscore(S, T):

	# one of the two or both strings being empty is the base case
	if S == '' or T == '':
		return 0

	# if the first letter of S is in T than it's returned in front of the list
	# that is yet to be formed recursivly
	elif S[0] in T:
		return 1 + jscore(S[1:], T.replace(S[0], '', 1))

	# if the first letter of S is in T than it's returned behind the list that
	# is yet to be formed recursivly
	else:
		return 0 + jscore(S[1:], T)

def exact_change(target_amount, L):

	# you always have enougth change if the target_amount is zero
	if target_amount == 0:
		return True

	# negative change can't be given
	elif target_amount < 0:
		return False

	# If you don't have any coins, but target_amount is higher than 0 you
	# don't have the exact change
	elif L == []:
		return False

	# two recursive steps, the first one using the first number in the list
	# and the second one not using the first number in the list
	else:
		useit = exact_change(target_amount - L[0], L[1:])
		loseit = exact_change(target_amount, L[1:])

		# exact_change is True if either recursive steps lead to a basecase
		# that corresponds to True
		return loseit or useit

class TestStringMethods(unittest.TestCase):

	def test_blsort(self):
		self.assertEqual(blsort([0,1,0,1]), [0,0,1,1])
		self.assertEqual(blsort([1,1]), [1,1])
		self.assertEqual(blsort([0,0,1,1,]), [0,0,1,1])

	def test_gensort(self):
		self.assertEqual(gensort([2,0]), [0,2])
		self.assertEqual(gensort([5,-3, 4 ]), [-3, 4, 5])
		self.assertEqual(gensort([5,4.9, 5.1]), [4.9,5,5.1])

	def test_jscore(self):
		self.assertEqual(jscore('hi', 'pie'), 1)
		self.assertEqual(jscore('aaa', 'abcabc'), 2)
		self.assertEqual(jscore('programming', 'programming'), 11)

	def test_exact_change(self):
		self.assertTrue(exact_change(42, [25, 1, 25, 10, 5, 1]))
		self.assertFalse(exact_change(50, [25, 3, 7, 11, 5]))
		self.assertFalse(exact_change(-30, [10,12,18]))
		self.assertTrue(exact_change(0, []))
		self.assertFalse(exact_change(19, []))

if __name__ == '__main__':
	unittest.main()


