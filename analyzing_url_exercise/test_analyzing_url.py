from unittest import TestCase
from analyzing_url_exercise.analyzing_url import analyze
from analyzing_url_exercise.models import Url


class Test(TestCase):

    def test_gmail(self):
        url = Url(protocol='http', host='www', domain='google.com', path='mail', parameters='user=foo')
        self.assertEqual(analyze('http://www.google.com/mail?user=foo'), url)

    def test_ssh_git(self):
        url = Url(protocol='ssh', user='foo', password='senha', domain='git.com')
        self.assertEqual(analyze('ssh://foo%senha@git.com/'), url)

    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            analyze("invalid url")

