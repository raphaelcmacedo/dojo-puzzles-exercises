from unittest import TestCase
from fizzbuzz_exercise.fizzbuzz import play


class Test(TestCase):
    def test_return_number(self):
        numbers = (1, 2, 4)
        for number in numbers:
            with self.subTest():
                self.assertEqual(str(number), play(number))

    def test_return_fizz(self):
        numbers = (3, 6, 9)
        for number in numbers:
            with self.subTest():
                self.assertEqual('fizz', play(number))

    def test_return_buzz(self):
        numbers = (5, 10, 20)
        for number in numbers:
            with self.subTest():
                self.assertEqual('buzz', play(number))

    def test_return_fizzbuzz(self):
        numbers = (15, 30, 45)
        for number in numbers:
            with self.subTest():
                self.assertEqual('fizzbuzz', play(number))
