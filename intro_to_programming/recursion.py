# -*- coding: utf-8 -*-
#
# Homework 12
# Filename:  recursion
#
#
# Name: Peter-Jan Derks
#
import unittest

def mult(n, m):
	# n and m are two integers
	if m == 0 or n == 0:
		zero = int(0)
		return zero

	# Dealing with a negitive m and postive n
	elif m < 0 and n > 0:
		return - n + mult(n, m + 1)

	# Dealing with two negative integers
	elif n < 0 and m < 0:
		return -n + mult(n, m + 1)

	# Dealing with two positive integers and a negative n with a positive m
	else:
		return n + mult(n,m-1)


# calculates the dot product of two lists
def dot(L,K):
	# L and K are two lists

	# can only calculate dot product if functions have the same length or 
	# aren't empty
 	if len(L) != len(K) or len(L) == 0:
 		return 0.0
 
 	# calculates the dot product of the first two integers in the list and then 
 	# does the same using the recursive step for the folllowing numbers
 	else:
 		return K[0] * L[0] + dot(L[1:], K[1:])

# finds when a character first shows up in string, if the character doesn't show up
# returns the length of the string
def ind(e, L):
	# e is a character and L is a list or a string

	if e not in L:
		return len(L)

	elif e == L[0]:
		return 0

	# using recursion goes through L one by one adding one to the returned
	# value everytime
	elif e != L[0]:
		return 1 + ind(e, L[1:])

# determines the scrabble score of a letter
def letterScore(let):

	# split the letters of the alfabet up according to the scrabble score they
	# have
	if let in 'aeilnorstu':
		return 1
	elif let in 'dg':
		return 2
	elif let in 'bcmp':
		return 3
	elif let in 'fhvwy':
		return 4
	elif let == 'k':
		return 5
	elif let in 'jx':
		return 8
	elif let in 'qz':
		return 10

	# no score returned 
	else:
		return 0


def scrabbleScore(S):
	if len(S) == 1:
		return letterScore(S[0])

	else:
		return letterScore(S[0]) + scrabbleScore(S[1:])


# Converts a single character c from DNA to RNA
def one_dna_to_rna(c):

	# converts the nucleotides in DNA to the corresponding nucleotides in RNA
	if c == 'A': 
		return 'U'
	elif c == 'C': 
		return 'G'
	elif c == 'G': 
		return 'C'
	elif c == 'T': 
		return 'A'

	# returns an empty string (if c is not a nucleotide)
	else: 
		return ''

def transcribe(S):

	# Calculates the score of the only letter
	if len(S) == 1:
		return one_dna_to_rna(S[0])


	# Concatenates the string of the RNA nucleotide and the string of all DNA 
	# nucleotides yet to be transcribed
	else:
		return one_dna_to_rna(S[0]) + transcribe(S[1:])

class TestStringMethods(unittest.TestCase):

	# Tests for a multiplaction of: two integers with one being zero, two
	# positive integers, two negative integers and two integers with opposite signs
	def test_mult(self):
		self.assertEqual(mult(3,0), 0)
		self.assertEqual(mult(3,2), 6)
		self.assertEqual(mult(-3,-3), 9)
		self.assertEqual(mult(-5,6), -30)
		self.assertEqual(mult(8,-3), -24)

	def test_dot(self):
		# Tests if the dot funtion works for two positive numbers, negative
		# numbers and returns 0.0 for two empty strings
		self.assertEqual(dot([3],[2]), 6)
		self.assertEqual(dot([-2, -2],[2,-1]), -2)
		self.assertEqual(dot([],[]), 0.0)

	def test_ind(self):
		self.assertEqual(ind('chicken',['chicken','nuggets']), 0)
		self.assertEqual(ind(55, range(0,100)), 55)
		self.assertEqual(ind(' ', 'programming is fun'), 11)

	def test_scrabbleScore(self):
		self.assertEqual(scrabbleScore('quetzal'), 25)
		self.assertEqual(scrabbleScore('jonquil'), 23)
		self.assertEqual(scrabbleScore('syzygy'), 25)

	def test_transcribe(self):
		self.assertEqual(transcribe('ACAA GTAC'), 'UGUUCAUG')
		self.assertEqual(transcribe('gat'), '')
		self.assertEqual(transcribe('GTA   G'), 'CAUC')

if __name__ == '__main__':
    unittest.main()
	

