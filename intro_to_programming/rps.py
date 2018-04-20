# -*- coding: utf-8 -*-
#
# Homework 9
# Filename:  rock-paper-scissors
#
#
# Name: Peter-Jan Derks
#

import random

# while true loop that makes it possible to play the game multiple times
while True:
    print "Still running..."
    response = raw_input("Would you like to play a game, yes or no? ")
    if response == 'no':
        break
    elif response == 'yes':
        user = raw_input("Choose your weapon: ")
        comp = random.choice(['rock','paper','scissors'])

        print 'the user (you) chose', user
        print 'the comp (I) chose', comp

        if user == 'rock':
            print 'Ha! I really chose paper -- I WIN!'

        elif user == 'paper':
            print ' I chose scissors LOSER'

        elif user == 'scissors':
            print 'Oww  Yeah I win again'

