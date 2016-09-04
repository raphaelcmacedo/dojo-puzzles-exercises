from unittest import TestCase
from happy_numbers_exercise.happy_numbers import play


class Test(TestCase):

    def test_1(self):
        self.assertEqual(play(1), True)