# -*- coding: utf-8 -*-
#
# Homework 11
# Filename: wordgames
#
#
# Name: Peter-Jan Derks
#

import random
import string


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = { 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10 }

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Some functions to get you started
# Make sure you understand what they do and how they work!

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    number_of_vowels = n / 3
    
    for _ in range(number_of_vowels):
        letter = VOWELS[random.randrange(0, len(VOWELS))]
        hand[letter] = hand.get(letter, 0) + 1
        
    for _ in range(number_of_vowels, n):    
        letter = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[letter] = hand.get(letter, 0) + 1
        
    return hand

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter, frequency in hand.items():
        for _ in range(frequency):
             print letter,
    print ''

# -----------------------------------


def load_words():
    """
    Reads the file in the WORDLIST_FILENAME variable and returns a list of 
    words in that file, in lowercase. The file should contain valid english
    words, each placed on a new line. Depending on the size of the word list,
    this function may take a while to finish.

    return: list of strings
    """

    words = []

    # puts the words from the file words.txt in a list.
    words_file = open('words.txt')
    for line in words_file:
        # rstrip returns a copy of the string in which all default whitespace
        # characters have been stripped and lower converts the string to 
        # lowercase
        words.append((line.lower()).rstrip())

    return words

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word multiplied by the length of the word, plus 50
    points if all n letters are used on the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0

    if word == '':
        return 0

    else:

        # loops through the word and adds the value of each character
        for character in word:
            score += SCRABBLE_LETTER_VALUES[character]
        
        # score gets multiplied by amount of letters in the word
        score = score * len(word)

        # bonus score of 50 if all letters are used
        if len(word) == n:
            score += 50

        return score

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # need to use copy function other wise the hand gets modified aswell
    # according references theorem
    new_hand = hand.copy()

    # takes the value of the letter used down by one
    for character in word:
        new_hand[character] -= 1

    return new_hand

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    if word in word_list:
        word_in_word_list = True
    else: 
        word_in_word_list = False

    # cannot be put in the "for char in word:" loop down below because it's
    # only true if it's true for every char in the word
    word_in_hand = True

    # checks if each character used in the word is also in the hand and the
    # if a character is not used more often than it occurs in the hand
    for char in word:
        if char not in hand or word.count(char) > hand[char]:
            word_in_hand = False   

    if word_in_word_list == False or word_in_hand == False:
        return False
    else: 
        return True

def play_hand(hand, words):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    hand: dictionary (string -> int)
    words: list of lowercase strings
    """
    total_score = 0

    # Shouldn't ask for a word if the user has an empty hand
    while not all(hand[char] == 0 for char in hand):

        print 'Current hand: ',
        display_hand(hand)
        word_input = raw_input('Enter word, or a "." to indicate that you are finished: \n') 

        # game can be stopped by user entering "."
        if word_input == '.':
            break

        if is_valid_word(word_input, hand, words) == True:

            # calculates and adds the score of the word to total
            score_word = get_word_score(word_input, HAND_SIZE)
            total_score += score_word

            print '%s earned %d. Total: %d ' % (word_input, score_word, total_score)
            hand = update_hand(hand, word_input)

        else:
            print 'Invalid word, please try again. \n'

    print 'Total score: %d' %(total_score)

def play_game():
    """
    Load the words, deal a hand and play the game with that hand
    """
    hand = deal_hand(HAND_SIZE)
    words = load_words()
    play_hand(hand, words)

if __name__ == '__main__':
    play_game()


