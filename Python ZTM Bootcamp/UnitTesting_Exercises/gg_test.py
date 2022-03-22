import unittest
import guessing_game
from unittest.mock import patch
import random
from guessing_game import guesse_the_number, start, end

class TestMain(unittest.TestCase):
    def testing_correct_answer(self):
        '''testing what happens if correct answer is given'''
        result = guessing_game.guesse_the_number(7, 7)
        self.assertTrue(result, "You sir are a genius - you have won the game.  Goodbye!")

    def testing_incorrect_answer(self):
        '''testing what happens if correct answer is given'''
        result = guessing_game.guesse_the_number(7, 8)
        self.assertFalse(result, 'Trump says, "wrong!"')

    def testing_out_of_range(self):
        '''testing what happens if guesse is out of the given range'''
        result = guessing_game.guesse_the_number(1,7)
        self.assertTrue("Oh no!\nSorry that is out of your choosen range.  Idiot\n")

    @patch('builtins.input', side_effect=['invalid_input'])
    def test_guess_with_invalid_input(self, mock_input):
        with self.assertRaises(ValueError):
            guesse_the_number('invalid_input', 7)

    def testing_string_input(self):                                     #I gave up at this point.  I need to learn more on my own
        '''testing what happens if input is a string'''
        result = guessing_game.guesse_the_number('hello', 7)
        self.assertRaises(ValueError)

    # def testing_empty_string(self):
    #     pass

    # def testing_none_value(self):
    #     pass

if __name__ == '__main__':
    unittest.main()