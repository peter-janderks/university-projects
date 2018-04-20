# -*- coding: utf-8 -*-
#
# Homework 11
# Filename:  slices
#
#
# Name: Peter-Jan Derks
#

pi = '314159'
e = '271'

# Example problem (problem 1):
# Creating the string '259' from pi and e
answer0 = e[0] + pi[-2:]     
print answer0

# problem 2:
# Creating the string '71' from e 
answer1 = e[-2:]
print answer1

# problem 3
# Creating the string '911' from pi and e
answer2 = pi[-1] + pi[1] + e[2]
print answer2

# problem 4 
# Creating the string '14159' from pi 
answer3 = pi[1:]
print answer3

# problem 5
# Creating the string '12345' from pi and e
answer4 = e[-1] + e[0] + pi[0] + pi[2] + pi[-2]
print answer4

