from unittest import TestCase
from leap_year_exercise.leap_year import play


class Test(TestCase):

    # True Tests
    def test_1600(self):
        self.assertEqual(play(1600), True)

    def test_1732(self):
        self.assertEqual(play(1732), True)

    def test_1888(self):
        self.assertEqual(play(1888), True)

    def test_1944(self):
        self.assertEqual(play(1944), True)

    def test_2008(self):
        self.assertEqual(play(2008), True)

    # False Tests
    def test_1742(self):
        self.assertEqual(play(1742), False)

    def test_1889(self):
        self.assertEqual(play(1889), False)

    def test_1951(self):
        self.assertEqual(play(1951), False)

    def test_2011(self):
        self.assertEqual(play(2011), False)