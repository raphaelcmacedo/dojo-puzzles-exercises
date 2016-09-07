from unittest import TestCase
from leap_year_exercise.leap_year import play


class Test(TestCase):

    def test_true(self):
        years = (1600, 1732, 1888, 1944, 2008)
        for year in years:
            with self.subTest():
                self.assertEqual(True, play(year))

    def test_false(self):
        years = (1742, 1889, 1951, 2011)
        for year in years:
            with self.subTest():
                self.assertEqual(False, play(year))
