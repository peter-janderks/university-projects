# -*- coding: utf-8 -*-

import csv
import random
import copy

def readfile(inputcsvfile):
	with open(inputcsvfile) as csv_file:
		reader = csv.reader(csv_file)
		students = []
		for row in reader:
			student = row[0]
			students.append([student])
	return(students)


def createfile(OUTPUT,groups,numberofassignments,numberofcolumns):
	with open(OUTPUT, 'w') as csvfile:
		writer = csv.writer(csvfile)
		for x in range(0,numberofassignments):
			assignment = groups[x]
			#for x in xrange(1,10):
				#writer.writerow(groups)


def first_assignment(numberofgroups,names):
	blabla = []

	for a in range(0,numberofgroups):
		blabla.append([])
	
	b = 0
	while True:
		for c in range(0,numberofgroups):
			blabla[c].append(names[b])
			b = b + 1
		if b == len(names):
			return(blabla)


def next_assignment(this,numberofgroups,var):
	for i in range(1,numberofgroups):
		rotate(this[i],i)
	print('SSShouldbedifferent')
	print(var)
	print(rotate)
	return this


def rotate(lst, x):
		lst[:] =  lst[-x:] + lst[:-x]
		return(lst)


def assign_teams(numberofassignments,groupsize,inputcsvfile,outputcsvfile):

	#
	names = readfile(inputcsvfile)
	numberofgroups = int(round((len(names)/groupsize)))

	#randomizes
	random.shuffle(names)

	#
	empty = numberofgroups * groupsize - len(names)  
	for x in range(0,empty):
		names.append([])
	
	#
	first_assignment_groups = first_assignment(numberofgroups,names)

	#creates a 2D array in which the the assigned groups are stored
	groups = []
	rotatethis = []
	rotatethis = copy.copy(first_assignment_groups)
	#inserts the groups of the first assignment into the final assignment array, because the groups 
	#of the first assignment is 2D the array becomes 4D
	groups += first_assignment_groups
	

	#write in csv file first_assignment groups
	print('first assignment')
	print(groups)

	#inserts the groups of the second, third, etc... into the final assignment
	for i in range(1,numberofassignments):
		print(groups)
		rotated = next_assignment(rotatethis,numberofgroups,first_assignment_groups)
		print('shouldbedifferent')
		print(groups)
		print(rotated)

		groups += [rotated]
		print(groups)

	createfile('hi',groups,numberofassignments,numberofgroups)


assign_teams(2,5,'students.csv','nogniks')