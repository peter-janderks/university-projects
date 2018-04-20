import unittest

from wordgames import *

class TestWordGames(unittest.TestCase):

    def test_1_deal_hand(self):
        hand = deal_hand(HAND_SIZE)
        self.assertEqual(type(hand), dict,
            msg='Function should return a dictionary of letters')

        for key, value in hand.items():
            self.assertIs(type(key), str,
                msg='Dicionary should have letters as the keys')
            self.assertIs(type(value), int,
                msg='Dictionary should have numbers as the values')
            self.assertIn(key, string.lowercase,
                msg='Dictionary keys should be lowercase')
        
        self.assertEqual(sum(hand.values()), HAND_SIZE,
            msg='Function should deal "n" number of letters')
        
        print "\n.: deal_hand() tests successful!\n"

    def test_2_load_words(self):
        words = load_words()
        
        self.assertIs(type(words), list,
            msg='Function should return the words in a list')
        self.assertEqual(len(words), 83667,
            msg='Function should load all the words from words.txt')
        
        for i in [0, 83666]:
            self.assertNotEqual(words[i][-1], '\n',
                msg='Function should remove the whitespace from the words')
            self.assertEqual(words[i].lower(), words[i],
                msg='Function should ensure the words are lowercase')
        
        print ": load_words() tests successful!\n"

    def test_3_get_word_score(self):
        words = {'': 0, 'it': 4, 'was': 18, 'scored': 54, 'waybill': 155,
            'outgnaw': 127}
        
        for word, score in words.items():
            computed = get_word_score(word, HAND_SIZE)
            self.assertEqual(computed, score,
                msg='The word "%s" scored %s points but should score %s points'
                % (word, computed, score))
        
        print ': get_word_score() tests successful!\n'

    def test_4_update_hand(self):
        words = [
            ({'a':1, 'q':1, 'l':1, 'm':1, 'u':1, 'i':1}, 'quail', {'m':1}),
            ({'e':1, 'v':2, 'i':1, 'l':2}, 'evil', {'v':1, 'l':1}),
            ({'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'hello', {})]

        for start, word, end in words:
            hand = start.copy()
            result = update_hand(hand, word)
            self.assertIs(type(result), dict,
                msg='Function should return the new hand')
            self.assertEqual(self.clean_hand(result), end,
                msg='For hand %s with word %s got new hand %s but expected %s'
                % (start, word, result, end))
            self.assertEqual(hand, start, 
                msg='Function should not modify the original hand')
        
        print ': update_hand() tests successful!\n'

    def test_5_is_valid_word(self):
        wordlist = load_words()
        words = [
            ({'h': 1, 'e': 1, 'o': 1}, 'hello', False),
            ({'h': 1, 'e': 1, 'l': 1, 'o': 1}, 'hello', False),
            ({'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'hello', True),
            ({'w': 3, 'o': 1, 'r': 1, 'l': 1, 'd': 1}, 'world', True),
            ({'w': 1, 'o': 1, 'n': 1, 'r': 1, 'l': 1, 'd': 1}, 'world', True),
            ({'w': 0, 'o': 1, 'r': 1, 'l': 0, 'd': 1}, 'world', False),
            ({'a': 2}, 'aa', True),
            ({'a': 1, 'c': 1}, 'ac', False),
            ({'a': 1, 'z': 1}, 'az', False)]
        
        for hand, word, result in words:
            computed = is_valid_word(word, hand, wordlist)
            self.assertEqual(computed, result,
                msg='For word %s with hand %s got %s but expected %s'
                % (word, hand, computed, result))

        print ': is_valid_word() tests successful!\n'
    
    @staticmethod
    def clean_hand(hand):
       for k, v in hand.items():
           if v == 0:
               del hand[k]
       return hand

if __name__ == '__main__':
    unittest.main()
