from unittest import TestCase
from find_phone_exercise.find_phone import convert

class Test(TestCase):

    def test_home_sweet_home(self):
        self.assertEqual('1-4663-79338-4663', convert('1-HOME-SWEET-HOME'))

    def test_my_miserable_job(self):
        self.assertEqual('69-647372253-562', convert('MY-MISERABLE-JOB'))

    def test_my_love(self):
        self.assertEqual('69-5683', convert('MY-LOVE'))