from unittest import TestCase
from happy_numbers_exercise.happy_numbers import play


class Test(TestCase):

    def test_happy(self):
        numbers = (1, 10, 100, 97, 130)
        for number in numbers:
            with self.subTest():
                self.assertEqual(True, play(number))

    def test_unhappy(self):
        numbers = (4,)
        for number in numbers:
            with self.subTest():
                self.assertEqual(False, play(number))