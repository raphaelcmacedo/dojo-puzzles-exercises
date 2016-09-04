from unittest import TestCase
from poker_exercise.poker import play


class Test(TestCase):

    def test_pairs(self):
        self.assertEqual(play('5H 5C 6S 7S KD', '2C 3S 8S 8D TD'), 'Player 2')

    def test_higher_card(self):
        self.assertEqual(play('5D 8C 9S JS AC', '2C 5C 7D 8S QH'), 'Player 1')

    def test_crack(self):
        self.assertEqual(play('2D 9C AS AH AC', '3D 6D 7D TD QD'), 'Player 2')

    def test_higher_pairs(self):
        self.assertEqual(play('4D 6S 9H QH QC', '3D 6D 7H QD QS'), 'Player 1')

    def test_full_house(self):
        self.assertEqual(play('2H 2D 4C 4D 4S', '3C 3D 3S 9S 9D'), 'Player 1')