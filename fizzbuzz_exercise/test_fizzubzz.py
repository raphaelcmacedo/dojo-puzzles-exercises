from unittest import TestCase
from fizzbuzz_exercise.fizzbuzz import play


class Test(TestCase):
    def test_1(self):
        self.assertEqual(play(1), '1')